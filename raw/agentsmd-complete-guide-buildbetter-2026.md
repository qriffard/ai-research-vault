[AGENTS.md](https://blog.buildbetter.ai/tag/agents-md/){.gh-article-tag}

# AGENTS.md Complete Guide for Engineering Teams in 2026 {#agents.md-complete-guide-for-engineering-teams-in-2026 .gh-article-title}

::: gh-author-image-list
[![Spencer
Shulem](https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/2024/01/IMG_5068-1-1.png)](/author/spencer/){.gh-author-image}

::: gh-author-name-list
#### [Spencer Shulem](/author/spencer/) {#spencer-shulem .gh-author-name}

:::: gh-article-meta
::: gh-article-meta-inner
May 13, 2026 []{.gh-article-meta-sep} [8 min]{.gh-article-length}

AGENTS.md has become the de facto standard for instructing AI coding
agents. This guide covers structure, examples, monorepo patterns, and
best practices for engineering teams adopting agents at scale in 2026.

<figure class="gh-article-image">
<img
src="https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w1200/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png"
srcset="https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w300/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png 300w,
                    https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w720/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png 720w,
                    https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w960/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png 960w,
                    https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w1200/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png 1200w,
                    https://storage.ghost.io/c/4f/50/4f50536c-6dc6-4a92-8ff1-e707b209e265/content/images/size/w2000/2026/05/agents-md-complete-guide-for-engineering-teams-in-2026.png 2000w"
sizes="(max-width: 1200px) 100vw, 1200px"
alt="AGENTS.md Complete Guide for Engineering Teams in 2026" />
</figure>

AGENTS.md has become the default way engineering teams give AI coding
agents the context they need to write correct, convention-aligned code.
By early 2026, it is read natively by Claude Code, OpenAI Codex CLI,
Cursor, Aider, Devin, GitHub Copilot, Gemini CLI, Windsurf, and Amazon Q
--- making it the closest thing the industry has to a universal agent
instruction format. [BuildBetter CLI\'s open-source
BB-Skills](https://github.com/buildbetter-app/BB-Skills?ref=blog.buildbetter.ai)
extends AGENTS.md with composable, conditional skill packs that load
only when relevant, so your team\'s playbook reaches every agent without
bloating context windows.

This guide covers what AGENTS.md is, how to structure it, real examples,
monorepo patterns, common mistakes, and how to get your first one
shipped in 30 minutes.

## What Is AGENTS.md? {#what-is-agentsmd}

**AGENTS.md is a standardized markdown file at the root of a repository
that gives AI coding agents instructions, context, and conventions for
working in that codebase.** Think of it as a README written for LLMs:
human-readable, but optimized for machine consumption and prescriptive
enough to drive consistent agent behavior.

The format was formalized at *agents.md* in mid-2025 and co-promoted by
OpenAI, Google, Sourcegraph, Cursor, Factory, JetBrains, and Anthropic
as a unified alternative to fragmented per-tool config files like
`.cursorrules`, `.clinerules`, `.github/copilot-instructions.md`, and
`CLAUDE.md`. At launch, OpenAI reported AGENTS.md files were already
present in 28,000+ repositories.

Key characteristics:

- **Lives at the repo root** alongside `README.md` and `CONTRIBUTING.md`
- **Plain markdown** --- no required schema, only a recommended set of
  sections
- **Loaded into the agent\'s context** automatically when the tool
  starts a session
- **Walked hierarchically** --- most agents read the nearest AGENTS.md
  to the file being edited, enabling per-package overrides in monorepos

It functions as a living interface contract between humans and agents
--- not documentation, but operational instructions.

## Why Engineering Teams Need AGENTS.md in 2026 {#why-engineering-teams-need-agentsmd-in-2026}

**AI coding agents now produce a meaningful share of new code, and
without explicit guidance they drift toward generic patterns instead of
your team\'s conventions.** The numbers tell the story:

- 76% of developers used AI coding assistants in 2025, up from 44% in
  2023 (Stack Overflow Developer Survey 2025)
- GitHub Copilot generates an average of 46% of code in files where it
  is enabled (GitHub Octoverse 2025)
- 39% of developers report little to no trust in AI-generated code, with
  convention mismatches cited as a top concern (Google DORA 2025)
- Anthropic\'s internal benchmarks show CLAUDE.md / AGENTS.md context
  can reduce wrong-pattern rewrites by 40--60%

Without an AGENTS.md, agents make inconsistent architectural choices,
violate conventions, and quietly accumulate tech debt. Code review
cycles balloon as humans catch the same drift over and over. With one,
agents produce mergeable PRs faster, tribal knowledge that previously
lived in Slack threads gets centralized, and behavior stays consistent
across teammates using different tools.

This is exactly the wall most teams hit: individual-agent productivity
stops compounding because context isn\'t shared. AGENTS.md is the first
lever; [BuildBetter
CLI](https://buildbetter.sh/?ref=blog.buildbetter.ai) and BB-Skills
extend it with cross-agent memory and reusable skill packs.

## The Standard AGENTS.md Structure {#the-standard-agentsmd-structure}

**A high-quality AGENTS.md follows a recommended set of sections, even
though the format imposes no required schema.** The community-converged
structure looks like this:

- **Project Overview** --- 2--3 sentences on what the codebase does and
  who uses it
- **Tech Stack** --- Languages, frameworks, key libraries with version
  pins (Node 20.11, pnpm 9.x, Python 3.12)
- **Setup Commands** --- Exact commands to install, build, test, and run
  locally
- **Code Style** --- Formatter, linter rules, naming conventions, file
  organization patterns
- **Testing Instructions** --- How to run tests, coverage expectations,
  test naming conventions
- **Architecture Notes** --- Key patterns (hexagonal, MVC, DDD), folder
  structure logic, module boundaries
- **PR and Commit Guidelines** --- Branch naming, commit format
  (Conventional Commits), PR description template
- **Security Considerations** --- Secrets handling, dependencies to
  avoid, auth patterns
- **Things to Avoid** --- Anti-patterns, deprecated paths, banned
  dependencies

The highest-leverage section is *Setup Commands*. Agents waste enormous
context guessing how to build and test; documenting canonical commands
is the fastest ROI you can get from this file.

## Complete AGENTS.md Example (Annotated) {#complete-agentsmd-example-annotated}

**Here is a working AGENTS.md for a TypeScript/Node.js B2B SaaS
application, with annotations on why each section matters to an agent.**

    # AGENTS.md

    ## Project Overview
    Acme is a B2B SaaS billing platform serving mid-market finance teams.
    Monorepo: apps/api (Node/Fastify), apps/web (Next.js 14), packages/shared.

    ## Tech Stack
    - Node 20.11 (pinned via .nvmrc)
    - pnpm 9.x (DO NOT use npm or yarn)
    - TypeScript 5.4, strict mode
    - Fastify 4, Prisma 5, PostgreSQL 16
    - Next.js 14 App Router, React 18, Tailwind 3
    - Vitest for unit tests, Playwright for E2E

    ## Setup Commands
    ```bash
    pnpm install
    pnpm db:migrate
    pnpm dev          # runs api + web concurrently
    pnpm test:unit    # always run before opening a PR
    pnpm test:e2e     # required for changes to apps/web
    pnpm lint         # must pass with zero warnings
    ```

    ## Code Style
    - Use Zod for ALL input validation at API boundaries
    - Prefer named exports; default exports only for Next.js pages
    - Async/await only — no .then() chains
    - File names: kebab-case.ts; React components: PascalCase.tsx

    ## Testing
    - Co-locate unit tests as `*.test.ts` next to source
    - Minimum 80% coverage on packages/shared
    - E2E tests live in apps/web/e2e

    ## Things to Avoid
    - DO NOT use the legacy /lib/utils/date.ts — use date-fns
    - DO NOT introduce class components in apps/web
    - DO NOT add new dependencies without updating this file
    - DO NOT use `any` — use `unknown` and narrow

**Why this works:** every line is imperative and command-oriented.
Compare \"We prefer pnpm\" (vague) to \"DO NOT use npm or yarn\"
(actionable). LLMs follow explicit instructions far more reliably than
soft preferences.

## AGENTS.md vs README.md vs CONTRIBUTING.md {#agentsmd-vs-readmemd-vs-contributingmd}

**The three files serve different audiences and should not duplicate
each other.**

  File                  Audience                  Purpose                                              Tone
  --------------------- ------------------------- ---------------------------------------------------- ------------------------------
  **README.md**         Humans (new to project)   Project introduction, quickstart, links              Welcoming, narrative
  **CONTRIBUTING.md**   Human contributors        Process: how to file issues, open PRs, run reviews   Procedural
  **AGENTS.md**         AI coding agents          Operational instructions to produce correct code     Imperative, command-oriented

**Decision rule:** if an AI agent needs it to write correct code, it
belongs in AGENTS.md. Cross-reference rather than duplicate --- README
can link to AGENTS.md for setup commands, and AGENTS.md can link to
architecture docs in your wiki.

## AGENTS.md Best Practices for 2026 {#agentsmd-best-practices-for-2026}

**The patterns that separate high-signal AGENTS.md files from bloated,
ignored ones are consistent across teams.**

- **Be imperative and specific.** \"Use pnpm, not npm\" beats \"We
  prefer pnpm.\"
- **Include exact commands, not descriptions.** Paste the literal shell
  command an agent should run.
- **Keep it under 500 lines.** AGENTS.md is loaded into the context
  window; token economy matters. 200--500 lines is the practical sweet
  spot.
- **Treat it as code.** Update AGENTS.md in the same PR that changes the
  convention. Assign an owner.
- **Use negative examples liberally.** \"DO NOT use class components in
  /web\" prevents an entire class of agent mistakes.
- **Pin tool versions.** Without pins, agents drift to whatever pattern
  is most common in their training data.
- **Add a Definition of Done checklist** agents can self-verify against
  before declaring a task complete.
- **Layer with skills.** AGENTS.md sets the baseline;
  [BB-Skills](https://github.com/buildbetter-app/BB-Skills?ref=blog.buildbetter.ai)
  add composable, conditional skill packs (`/bb-specify`, `/bb-plan`,
  `/bb-review`, `/trust-but-verify`) that load only when relevant ---
  keeping AGENTS.md lean while making your team\'s full playbook
  available to every agent.

## AGENTS.md in Monorepos and Large Codebases {#agentsmd-in-monorepos-and-large-codebases}

**In monorepos, a thin root AGENTS.md plus rich per-package AGENTS.md
files scales better than one giant root file.** Most agents walk up the
directory tree from the file being edited and load the nearest
AGENTS.md, which means you can scope context precisely to what the agent
is working on.

Recommended pattern:

- **Root /AGENTS.md** --- org-wide standards: language versions, package
  manager, commit format, security rules, monorepo layout
- **/apps/api/AGENTS.md** --- service-specific: Fastify conventions,
  Prisma patterns, API versioning
- **/apps/web/AGENTS.md** --- frontend-specific: component conventions,
  state management, Tailwind tokens
- **/packages/shared/AGENTS.md** --- shared types, public API
  constraints, deprecation policy

Document cross-service contracts (shared types, API schemas, event
payloads) in the package that owns them, and link from consumers. This
keeps each file under the 500-line ceiling while giving agents exactly
the context they need for the file they\'re editing.

## How AGENTS.md Connects to Customer-Led Development {#how-agentsmd-connects-to-customer-led-development}

**AGENTS.md tells agents *how* to build; customer evidence tells your
team *what* to build.** Engineering velocity from AI agents only
translates to business value when teams ship the right things.

This is where BuildBetter CLI\'s evidence layer becomes a multiplier.
With an optional BuildBetter API key, BB-Skills pulls customer signals
--- feature requests, pain points, support themes --- directly into
specs (`/bb-specify`), plans (`/bb-plan`), and PR reviews
(`/bb-review`). The loop looks like this:

1.  **Customer signal** surfaces in BuildBetter from calls and
    conversations
2.  **Prioritized work** flows into PRDs and specs with evidence
    attached
3.  **AGENTS.md conventions** guide the agent\'s implementation
4.  **BB-Skills** carry your team\'s playbook into every PR review
5.  **Faster validated delivery** --- you ship what customers actually
    asked for

No other context layer combines all three: cross-agent session memory,
team-conventional skills, and customer evidence. AGENTS.md is the
foundation; BuildBetter CLI is the layer that makes it compound across
teammates and across agents.

## Common AGENTS.md Mistakes to Avoid {#common-agentsmd-mistakes-to-avoid}

**Most failed AGENTS.md files share a small set of recurring mistakes.**

- **Copy-pasting README content.** README is narrative; AGENTS.md is
  imperative. They serve different consumers.
- **Vague guidance.** \"Write clean code\" provides zero decision
  support. Replace with specific rules.
- **Letting it drift.** Agents follow AGENTS.md literally. Stale
  guidance produces stale code.
- **Omitting build and test commands.** The single highest-ROI section.
  Don\'t make agents guess.
- **Over-stuffing.** A 2,000-line AGENTS.md crowds out the agent\'s
  working context. Move detail into per-package files or skills.
- **No negative examples.** Telling agents what to do is half the job;
  telling them what not to do prevents recurring failures.

## Getting Started: Your First AGENTS.md in 30 Minutes {#getting-started-your-first-agentsmd-in-30-minutes}

**You can ship a useful AGENTS.md in a single focused session.** Follow
these steps:

1.  **Copy the template** from agents.md or use the example above as a
    starting point.
2.  **Fill in setup, test, and build commands first.** This alone
    delivers most of the value.
3.  **Document your top 5 conventions and top 5 anti-patterns.**
    Imperative language, specific examples.
4.  **Test with an agent on a small task.** Watch where it deviates ---
    those gaps tell you what to add.
5.  **Commit and iterate.** Refine in subsequent PRs as new gaps
    surface.
6.  **Layer in BB-Skills.** Install [BuildBetter
    CLI](https://buildbetter.sh/?ref=blog.buildbetter.ai) and pull in
    skill packs like `/bb-specify`, `/bb-review`, and
    `/trust-but-verify` to extend AGENTS.md with composable workflows
    that work across Claude Code, Cursor, Codex, Copilot, Gemini CLI,
    Windsurf, and Amazon Q.

## Frequently Asked Questions

### Is AGENTS.md an official standard? {#is-agentsmd-an-official-standard}

It is a community-driven open specification published at agents.md,
co-promoted by OpenAI, Google, Sourcegraph, Cursor, Factory, Anthropic,
and others. It is not an ISO/IETF standard, but it has become the de
facto convention adopted across major AI coding tools in 2025--2026.

### Which AI coding tools read AGENTS.md? {#which-ai-coding-tools-read-agentsmd}

As of 2026, AGENTS.md is read by Claude Code, OpenAI Codex CLI, Cursor,
Aider, Devin, Sourcegraph Amp, Google Jules, Zed AI, Continue, Roo Code,
Factory Droids, GitHub Copilot, Gemini CLI, Windsurf, and Amazon Q. Most
tools that previously used proprietary files (CLAUDE.md, .cursorrules)
now also read AGENTS.md, often as a fallback or primary.

### Should AGENTS.md be committed to the repo? {#should-agentsmd-be-committed-to-the-repo}

Yes. AGENTS.md should live at the repository root and be
version-controlled like any source file. Treat it as code: review
changes, update it in the same PR that introduces a new convention, and
assign an owner.

### Can AGENTS.md replace internal engineering wikis? {#can-agentsmd-replace-internal-engineering-wikis}

No. AGENTS.md should be the source of truth for code-level conventions
and operational commands. Higher-level architecture decisions, RFCs,
runbooks, and product context still belong in your wiki --- though
AGENTS.md can link to them.

### How often should AGENTS.md be updated? {#how-often-should-agentsmd-be-updated}

Update it whenever a convention changes, in the same PR. Conduct a
quarterly review to remove stale guidance. A useful signal: when an
agent repeatedly produces incorrect output, that\'s a gap in AGENTS.md.

## Ship at the Speed of Insight

AGENTS.md is the foundation. BuildBetter CLI is the layer that makes it
scale across teammates and across agents --- with cross-agent session
memory, open-source BB-Skills that carry your team\'s playbook into
every PR, and customer evidence pulled directly into specs and reviews.
Used by Brex, Rappi, PostHog, AppFolio, Clay, Lufthansa, Procore, and
Macmillan.

[**Install BuildBetter CLI
→**](https://buildbetter.sh/?ref=blog.buildbetter.ai)

