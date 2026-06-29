#!/usr/bin/env python3
"""Extract an arXiv paper's LaTeX source and convert to markdown.

Usage:
    python extract-arxiv.py <arxiv-url-or-id> [OUTPUT.md]

Examples:
    python extract-arxiv.py 2402.14207 raw/storm-paper.md
    python extract-arxiv.py https://arxiv.org/abs/2402.14207 raw/storm-paper.md

Downloads the LaTeX source tarball from arXiv, finds the main .tex file,
converts it to markdown via pandoc (preserving LaTeX math as $...$ / $$...$$),
and writes the result.

Requires: pandoc
"""
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path


def parse_arxiv_id(source: str) -> str:
    """Extract the arXiv ID from a URL or bare ID."""
    # https://arxiv.org/abs/2402.14207 or https://arxiv.org/pdf/2402.14207
    m = re.search(r"arxiv\.org/(?:abs|pdf|e-print)/([0-9]+\.[0-9]+(?:v\d+)?)", source)
    if m:
        return m.group(1)
    # bare ID like 2402.14207 or 2402.14207v2
    m = re.match(r"^([0-9]+\.[0-9]+(?:v\d+)?)$", source.strip())
    if m:
        return m.group(1)
    raise ValueError(f"Cannot parse arXiv ID from: {source}")


def download_source(arxiv_id: str, dest_dir: Path) -> Path:
    """Download and extract the e-print tarball. Returns the extraction directory."""
    url = f"https://arxiv.org/e-print/{arxiv_id}"
    tarball = dest_dir / "source.tar.gz"

    req = urllib.request.Request(url, headers={"User-Agent": "llm-wiki-extract/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(tarball, "wb") as f:
        f.write(resp.read())

    extract_dir = dest_dir / "source"
    extract_dir.mkdir()

    # arXiv e-prints are usually gzipped tar, but sometimes just a single .tex
    try:
        with tarfile.open(tarball, "r:*") as tar:
            tar.extractall(path=extract_dir, filter="data")
    except tarfile.ReadError:
        # Not a tarball — likely a single gzipped .tex file
        import gzip
        with gzip.open(tarball, "rb") as gz:
            content = gz.read()
        single_tex = extract_dir / "main.tex"
        single_tex.write_bytes(content)

    return extract_dir


def find_main_tex(extract_dir: Path) -> Path:
    """Find the main .tex file in the extracted source."""
    tex_files = list(extract_dir.rglob("*.tex"))
    if not tex_files:
        raise FileNotFoundError(f"No .tex files found in {extract_dir}")
    if len(tex_files) == 1:
        return tex_files[0]

    # Heuristic: look for \documentclass — that's the main file
    for tex in tex_files:
        content = tex.read_text(errors="replace")
        if r"\documentclass" in content:
            return tex

    # Fallback: common names
    for name in ["main.tex", "paper.tex", "article.tex", "ms.tex"]:
        candidate = extract_dir / name
        if candidate.exists():
            return candidate

    # Last resort: largest .tex file
    return max(tex_files, key=lambda p: p.stat().st_size)


def fetch_metadata(arxiv_id: str) -> dict:
    """Fetch basic metadata from the arXiv API."""
    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "llm-wiki-extract/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml = resp.read().decode("utf-8")
    except Exception:
        return {}

    def extract_tag(tag: str) -> str:
        m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", xml, re.DOTALL)
        return m.group(1).strip() if m else ""

    # Extract authors (arXiv API uses <author><name>...</name></author>)
    authors = re.findall(r"<author>\s*<name>(.*?)</name>", xml)

    title = extract_tag("title")
    # The API returns two <published> tags; the entry-level one is after <entry>
    published = ""
    entry_match = re.search(r"<entry>(.*?)</entry>", xml, re.DOTALL)
    if entry_match:
        pub_match = re.search(r"<published>(.*?)</published>", entry_match.group(1))
        if pub_match:
            published = pub_match.group(1)[:10]

    return {
        "title": title,
        "authors": authors,
        "published": published,
        "arxiv_id": arxiv_id,
        "url": f"https://arxiv.org/abs/{arxiv_id}",
    }


def convert_to_markdown(tex_path: Path, meta: dict) -> str:
    """Convert LaTeX to markdown via pandoc, prepend metadata header."""
    result = subprocess.run(
        [
            "pandoc",
            str(tex_path),
            "-f", "latex",
            "-t", "markdown",
            "--wrap=none",
            "--markdown-headings=atx",
        ],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(tex_path.parent),
    )

    if result.returncode != 0:
        print(f"pandoc warning (exit {result.returncode}): {result.stderr[:500]}", file=sys.stderr)

    body = result.stdout
    if not body.strip():
        raise RuntimeError(f"pandoc produced empty output. stderr: {result.stderr[:500]}")

    # Build a metadata header
    header_parts = []
    if meta.get("title"):
        header_parts.append(f"# {meta['title']}")
    if meta.get("authors"):
        header_parts.append(f"\n**Authors:** {', '.join(meta['authors'])}")
    if meta.get("published"):
        header_parts.append(f"**Published:** {meta['published']}")
    if meta.get("url"):
        header_parts.append(f"**arXiv:** {meta['url']}")
    header_parts.append("")
    header_parts.append("---")
    header_parts.append("")

    return "\n".join(header_parts) + body


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <arxiv-url-or-id> [OUTPUT.md]", file=sys.stderr)
        sys.exit(1)

    source = sys.argv[1]
    arxiv_id = parse_arxiv_id(source)

    meta = fetch_metadata(arxiv_id)
    title = meta.get("title", arxiv_id)

    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
        output_path = Path(f"{slug}.md")

    print(f"Fetching arXiv source for {arxiv_id} ({title})...")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        extract_dir = download_source(arxiv_id, tmpdir)
        main_tex = find_main_tex(extract_dir)
        print(f"Main .tex file: {main_tex.name}")

        md = convert_to_markdown(main_tex, meta)

    output_path.write_text(md)
    print(f"Extracted {len(md):,} chars → {output_path}")


if __name__ == "__main__":
    main()
