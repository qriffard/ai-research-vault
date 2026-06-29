# Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations

**Authors:** Yucheng Jiang, Yijia Shao, Dekun Ma, Sina J. Semnani, Monica S. Lam
**Published:** 2024-08-27
**arXiv:** https://arxiv.org/abs/2408.15232

---


*Equal Contributionfootnote

## Abstract

While language model (LM)-powered chatbots and generative search engines excel at answering concrete queries, discovering information in the terrain of unknown unknowns remains challenging for users. 
To emulate the common educational scenario where children/students learn by listening to and participating in conversations with their parents/teachers, we create Collaborative STORM (). [Our resources and code are released at <https://github.com/stanford-oval/storm>.]
Unlike QA systems that require users to ask all the questions, lets users observe and occasionally steer the discourse among several LM agents. The agents ask questions on the user's behalf, allowing the user to discover unknown unknowns serendipitously. To facilitate user interaction, assists users in tracking the discourse by organizing the uncovered information into a dynamic mind map, ultimately generating a comprehensive report as takeaways. For automatic evaluation, we construct the dataset by collecting real information-seeking records with user goals. outperforms baseline methods on both discourse trace and report quality. In a further human evaluation [A live research preview is now available publicly at <https://storm.genie.stanford.edu>], 70% of participants prefer over a search engine, and 78% favor it over a RAG (Retrieval Augmented Generation) chatbot.


## Introduction


    !
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/comparison.pdf)
    
    Comparison of different paradigms for learning and information seeking. enables humans to observe and participate in a collaborative discourse among LM agents with different roles. Users can request the system to generate a full-length cited report based on the discourse history and the information collected.
    


Recent advancements in language models (LMs) [cite:bai2022constitutional, gpt4technicalreport, geminiteam2024gemini] and retrieval-augmented generation (RAG) [cite:lewis2021retrievalaugmented] have led to more capable chatbots and emerging generative search engines [cite:liu-etal-2023-evaluating]. 
Compared to traditional search engines and information retrieval (IR) models [cite:Robertson1977THEORIESAM], these systems fulfill user queries by generating direct responses, effectively addressing known unknowns, where users are aware of their information needs. 

However, a gap remains in using these systems for complex information-seeking scenarios, such as academic research, market analysis, and decision-making, where the system should expose users to their unknown unknowns to facilitate knowledge discovery. While the concept of unknown unknowns originally referred to unexpected risks in the military, it is linked to the serendipitous discovery of information in the information research context [cite:foster2003serendipity,agarwal2015towards]. Specifically, 
[cite:kirzner1997entrepreneurial] directly contrasts such discovery (“the realization that one had overlooked something in fact readily available”) with successful search (“the deliberate production of information which one knew one had lacked”).


Prior work on automated expository writing attempts to help readers  navigate the terrain of unknown unknowns by curating information from various sources into unified articles with substantial breadth and depth [cite:shen2023summarization]. 
In particular, the STORM writing system demonstrates that LMs paired with search engines can automatically generate a high-quality draft of Wikipedia-like articles on arbitrary topics [cite:shao2024assisting]. However, producing the static report as the final outcome, STORM does not support any user interaction which is crucial in complex information seeking 
where there is no single, gold query, but queries evolve dynamically towards a goal [cite:Bates1989TheDO]. This dynamic and exploratory nature makes designing assistance systems challenging. Traditional search engines and RAG chatbots passively react to users' search queries or conversational questions, often inducing echo chamber effects [cite:sharma2024generative] or high cognition load as users with limited prior knowledge may even struggle to formulate questions [cite:kuhlthau1991inside,belkin1982ask].


To surface unknown unknowns and better support user interaction, we propose Collaborative STORM (), an information-seeking assistance system that supports collaborative discourse among users and multiple LM agents. Unlike the one-question-one-answer mode of interaction, allows users to learn by observing and participating occasionally in the discourse, emulating a common educational scenario [cite:nussbaum2008collaborative]. 
To facilitate a thought-provoking discourse and serendipitous discovery, simulates two agent types grounded in the search engine:  who participate by asking or answering questions with different perspectives and a , a non-expert who knows enough to ask good questions and steers the discourse. The user can jump in at any time to steer the discourse and inject questions and opinions according to their interest.  maintains a dynamic, hierarchical mind map to ensure they can easily follow and engage [cite:buzan1974noting]. 

Upon the conclusion of the discourse, users can request the system to generate a cited report based on the mind map. 


For evaluation, we introduce WildSeek, a dataset of topics and user goals from real users engaged in complex information-seeking across multiple domains. We propose automatic metrics to assess both discourse trace and final report quality. Our results show that significantly outperforms RAG chatbots in surfacing in-depth and serendipitous information while providing a more engaging learning experience.


We further conduct a human evaluation by inviting 20 users with diverse backgrounds to compare with a search engine and a RAG chatbot. 70% preferred over the search engine, and 78% preferred it over the RAG chatbot for the overall information-seeking experience. Participants find that facilitates serendipitous discovery and requires less mental effort.


Our main contributions include:


    
  * We propose , a novel system that combines collaborative discourse emulation, human interaction, and information organization to assist learning and complex information seeking.
 
    
  * We construct the dataset from real-world human information-seeking records to evaluate information-seeking assistance tools.

    
  * Results from both automatic and human evaluation show that can help humans discover unknown unknowns with less mental effort required.


## Complex Information Seeking


## Human Learning and Information Seeking


### Complex Information Seeking


### Task Setup


### Problem Formulation


[cite:pirolli2009powers] defines complex information-seeking as part of the broader sensemaking process, involving collecting, sifting, understanding, and organizing information from large collections to generate a knowledge product. Prevalent in domains such as investigative journalism, scientific research, and market analysis, this task has the following properties: (1) it requires seeking information from multiple sources to address various facets of a topic rather than retrieving a document that best matches a query; (2) it involves ongoing user interaction rather than processing a single query; (3) it produces report-like curated information product rather than a single short-form answer. As shown in table:setup_comparison, 

none of the existing information-seeking assistance systems <cit.> can  fully support this task.


!
 
    c]@c@Multiple
Sources     c]@c@Ongoing
Interact     c]@c@Curated
Report  
 
Information Retrieval                                                                                                                                                                                                                                                   

Single-Turn QA                                                                                                                                                                                                                                                         

Conversational QA                                                                                                                                                                                                                                                       

Report Generation                                                                                                                                                                                                                                                       
 
                                                                                                                                                                                                                                                           


Comparison of different information-seeking assistance systems.


Given a user with an initial topic of interest t and an initial goal g, and a repository of information R, the task is to interact with the user and write a custom long-form report tailored to the users' interest; the report is a sequence of sentences 𝒮=s_1s_2...s_n, with each sentence citing a set of retrieved information ℐ⊂ℛ,  for the sake of verifiability.

, we define the user's interaction with the system (, formulating new queries or questions) as a policy π. To satisfy the goal g, the system aims to respond to π, retrieve


### : An In-the-Wild Information Seeking Dataset


0.9!
    
    
    Domain: Economics 

        [0.5pt]
        Topic: Development of a Shared Trading Currency to Facilitate International Trade 

        [0.5pt]
        Goal: Investigate how a new shared currency could eliminate transaction costs and boost GDP among member countries. 

    

    A sample data point in the dataset for studying complex information-seeking tasks; the topic and goal are provided by users on the publicly available STORM website, the domain is assigned manually.
    


To study users’ interests in complex information-seeking tasks in the wild,
we utilized data collected from the open-source STORM web application[Available at <https://storm.genie.stanford.edu>], which generates comprehensive long-form reports based on users’ specified topics of interest and goals for using the site. 

Each data point is a pair comprising a topic and the user's goal. 
To improve the quality of the dataset, we retain only those data points that are well motivated by applying rule-based filtering followed by binary classification using an LM (). Next, we use the same LM to predict the taxonomy class of each topic, followed by manual review and refinement. Finally, we downsample the data to create a dataset with 100 data points across 24 different domains. tab:data_point shows a sample data point from the dataset; further details about the dataset are in Appendix <ref>. 


## Method


    0.95!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/method.pdf)
    
    Overview of . emulates a collaborative discourse among the user, simulated perspective-guided , and a simulated . It maintains a dynamically updated mind map (sec:mind_map) to help user track and engage in the discourse (sec:human_steering_mode) . The simulated is prompted to determine the utterance intent based on discourse history and generate a question or an answer grounded in the Internet (sec:simulate_participant). The simulated is prompted with unused information and the mind map to generate a new question to automatically steer the discourse (sec:simulate_moderator). The mind map can be used to generate a full-length cited report as takeaways. Complete discourse transcript and the associated report are detailed in Appendix sec:alphafold_discourse and sec:alphafold_report.
    


“Tell me and I forget. Teach me and I remember. Involve me and I learn.”
— Benjamin Franklin


### Collaborative Discourse Protocol


[cite:nussbaum2008collaborative] emphasizes the importance of collaborative discourse in fostering deep understanding and critical thinking in human learning. Since it is difficult to assemble a group of human experts for collaborative discourse on any topic at any time, we propose (Fig.method) to emulate this process with multiple LM agents to assist human information seeking and learning. Formally, the collaborative discourse, 𝒟={u_1, u_2, ..., u_n}, consists of turn-based textual utterances u_i from one of three roles: 

the user (sec:human_steering_mode),  with diverse perspectives (sec:simulate_participant), and a  guiding the discourse and injecting questions (sec:simulate_moderator). The discourse begins with N , 𝒫={p_1, ..., p_N}, discussing the topic t for one turn per to warm up the conversation. dynamically maintains a mind map (sec:mind_map) to track the discourse and construct shared knowledge between the user and the system.

Utterance Intent  
Inspired by the utterance intent taxonomy for information-seeking conversations proposed by [cite:Qu_2019], we associate each agent utterance u_i with an agent intent type a_i, where a_i can be one of the following: 


  * Original Question initiates a new question 

  * Information Request seeks additional information from the prior utterance

  * Potential Answer offers a possible answer to a previously posed question 

  * Further Details provides supplementary information to a previous answer

We group Original Question and Information Request as question-asking and the other two  intents as question-answering.


Initiative Management  [cite:traum2003issues] underscores the necessity of discourse management in multiparty dialogues. 

While existing systems support either just user initiatives (, QA systems) or just agent initiatives (, STORM), adopts a mixed-initiative approach. When the user actively engages, the system continues the discourse based on the user's question or argument, allowing for a more targeted discussion. Otherwise, the system automatically generates the next turn. The user controls who takes the initiative, as allows the user to take a turn anytime.

Turn Management  
If the user does not take the turn at timestamp i, needs to determine which LM agent should generate the next utterance u_i. Its protocol is to let different , p_1, ..., p_N, take turns in sequence. To prevent them from only expanding on the same point, upon observing L consecutive turns of expert responses with intents being either Potential Answer or Further Details, the system asks the to intervene.
In sec:automatic_evaluation_results, we analyze the benefit of this protocol design.


### Tracking the Discourse with a Mind Map


Having shared knowledge or a shared conceptual space is critical for collaboration [cite:roschelle1995construction]. To help users track the discourse and reduce their cognition load, uses a tree-structured mind map ℳ to dynamically organize collected information in the discourse 𝒟. 

Specifically, ℳ = (𝒞, ℰ) is a hierarchical organization of concepts 𝒞, where its directed edges ℰ characterize latent parent-child relationships among topics (, in Fig.method, “Drug Discovery Acceleration” is a subtopic of “Impact and Applications”). Each concept c∈𝒞 is associated with a subset of retrieved information I^c⊂ℐ. To ensure ℳ is an intent-driven organization of information, each piece of information is also associated with the question that leads to its retrieval.


dynamically updates the mind map through two operations,  and .  places a piece of information under the most appropriate concept by first deriving a set of candidate concepts using semantic similarity between its associated question and each concept in 𝒞, then prompting the LM to choose the final placement. When a concept c has more than K pieces of information, ℳ triggers the  operation.  prompts the LM to generate a list of new subtopic names under c, and applies  to place each piece of information associated with c in the subtree rooted at c. After expansion, adopts a bottom-up cleaning process to iteratively delete concepts with no supporting information and collapse concepts with only one subtopic. More details on  operation are included in Appendix <ref>.


### User Participation


When the user injects an utterance u, uses u as the query to retrieve information to prompt the LM to obtain an updated list of , 𝒫'. 
Following this update, the system switches back to the auto-steering mode where the or the takes turns according to the turn management protocol introduced in sec:discourse_protocol. Once the user is satisfied with the discourse, generates the final report 𝒮 as the curated information product of the collaborative discourse. This report is generated using the mind map ℳ as the outline and the retrieved information I^c associated with each concept c to generate the report section by section.


### Auto steering mode


### Generating Discourse with Multiple Roles


### Simulating the Roundtable Participant


Following STORM [cite:shao2024assisting], which uses perspective-guided question asking to improve the question diversity and quality, personalizes simulated with different expertise to represent different perspectives. retrieves the background of topic t with a search query and gives it to an LM to generate the list 𝒫={p_1, ..., p_N}. For example, for the topic “AlphaFold3” in Fig.method, the LM suggests an “AI Expert”, a “Geneticist”, and a “Molecular Biology Expert” to participate in the discourse.  


If there is no interruption by the user or the , each p_j sequentially takes turns with the following procedure: 
To generate an utterance from an expert p in turn i, 
(1) The LM is prompted to choose the intent a_i based on the discourse history {u_1, ..., u_i-1} and the 's perspective p. (2) If  the intent a_i is Potential Answer or Further Details, we prompt the LM to generate a search query q, retrieve information with a search engine [Following [cite:shao2024assisting], when retrieving information with a search engine, we apply rule-based filtering according to the Wikipedia guideline <https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources>.], and  generate a response with citations; otherwise, we prompt the LM to directly generate a question based on the discourse history.  

(3) We use the LM to polish the utterance to make it more chatty and engaging.


### Simulating the Moderator


If all the simulated participants are experts, we discover that the discourse tends to consist mostly of utterances with  intent Further Details, leading to repetition and niche discussions. The moderator plays an important role of injecting new directions into the discourse.  
To generate the 's utterance, instructs the LM to generate informed questions based on the uncited sources retrieved since the last turn. To choose among the many uncited sources, the reranks each piece of information i based on the similarity to the topic t and the dissimilarity to its associated question q. 

Formally, the reranking score is 

    cos(𝐢, 𝐭)^α (1- cos(𝐢, 𝐪))^1-α,

where 𝐢, 𝐭, 𝐪 are corresponding text embeddings and α is a hyperparameter. This reranking function prioritizes information that does not directly answer the original question but is relevant to the topic t. concatenates these reranked sources along with concept names in 𝒞 to avoid repetitive concepts. This combined context is used to prompt the LM to generate the question for the turn and an updated list of , 𝒫'.


## Implementation


### Baselines


### Experiment Setups


!
 
    5c!width Report Quality     3cQuestion-Answering Turn Quality  

                            Relevance     Breadth     Depth     Novelty     Info Diversity                                        Consistency     Engagement     # Unique URLs      
 
RAG Chatbot                 3.57         3.50        3.26      2.44            0.595                                      4.37            4.13           2.94                           

STORM + QA                  3.61         3.61        3.43      2.50                       0.592                          4.34            4.11           2.89                         
 
                    3.78         3.79        3.77†    3.05†    0.602                                        4.40†    4.33†    6.04†

  w/o Multi-Expert     3.73         3.75        3.77      2.93                               0.589                   4.40            4.32           5.91                    

  w/o Moderator             3.56         3.69        3.41      2.89                           0.577                       4.39            4.28           5.67                     


Automatic evaluation results for report quality and the quality of question-answering turns in the discourse with simulated users. Ablations are included as follows: “w/o Multi-Expert” denotes 1 expert and 1 moderator, and “w/o Moderator” denotes N experts and 0 moderator.† denotes significant differences (p<0.05) from a paired t-test between and both baselines. The rubric grading uses a 1-5 scale. All scores reported are the mean values. 


### Implementation

The LM component of is implemented using zero-shot prompting via the DSPy framework [cite:khattab2023dspy] and  (see full prompts in Appendix <ref>). We ground on the Internet using the You.com search API[<https://documentation.you.com/api-reference/search>] although the system is compatible with other search engines or IR systems. Hyperparameters N, K, L, α are set to 3, 10, 2, and 0.5, respectively. The text embeddings in eq:rerank_score are obtained from . We set the LM temperature as 1.0 and top_p as 0.9 for all experiments. For human evaluation, we develop a web application (Fig.human_eval_demo) for users to interact with in real time.


## Automatic Evaluation


Automatic evaluation enables scalable testing and allows for consistent simulation of user behavior. We compare with the following baselines: (1) RAG Chatbot, a baseline that retrieves information from the search engine and interacts with the user through a one-question-one-answer paradigm. (2) STORM + QA, a baseline that uses the STORM framework [cite:shao2024assisting] to generate a report for a given topic to provide general information. It then allows the user to ask follow-up questions and provides corresponding answers retrieved with the search engine.


### Evaluation Setup

We use the dataset where each data point consists of an initial topic t and goal g. 
We simulate the user 
with an LM () prompted with t, g, the discourse history 𝒟, and the instruction for question generation. To ensure a fair comparison, we terminate the information-seeking session once it reaches 30 search queries for and both baselines. For all methods, the final report is generated using the two-stage approach of outline generation followed by section-by-section article generation, as proposed by STORM [cite:shao2024assisting], based on the interaction history. We evaluate the system quality by assessing the final report and the interaction history (, discourse) with the automatic metrics defined in sec:eval_metrics.


### Automatic Metrics


Report Quality  
We evaluate the final report on four aspects, Relevance, Broad Coverage (Breadth), Depth, and Novelty, as indicators of the quality of the whole information-seeking process.[The same four aspects are used in human evaluation.] We employ Prometheus 2 [cite:kim2024prometheus], a 7B evaluator LM, to score the report based on a 5-point rubric. To further quantify the diversity of the collected information, we also report the Information Diversity as the average pairwise dissimilarity of ℐ,

    1-∑_i,j∈ℐ,i≠ jcos(𝐢, 𝐣)/|ℐ|(|ℐ|-1),

where 𝐢,𝐣 are corresponding text embeddings obtained from OpenAI's .


Discourse Quality  Since the discourse itself is valuable for human learning, we also evaluate the discourse trace using a 5-point rubric to grade each turn. This grading assesses Novelty, Intent Alignment, and No Repetition for question-asking utterances (, utterances with the intent Original Question or Request Information). For question-answering utterances that provide information
, we assess Consistency and Engagement. We also report the number of unique cited URLs in these utterances to indicate information diversity at the turn level. 
Both the rubrics for report evaluation and utterance evaluation are included in Appendix <ref>.


### Final Report Quality


### Main Results


### Automatic Evaluation Results


table:report_grading presents the evaluation results for report quality and the quality of question-answering turns in the discourse. The question-answering turns and the final report are the primary sources for human learning when they interact with . STORM + QA considers multiple perspectives in researching the given topic, indeed leading to improved performance across all four grading dimensions of the report quality compared to the RAG Chatbot. However, outperforms it, particularly in the Depth and Novelty aspects, by simulating collaborative discourse with multiple agentic roles, akin to a thought-provoking round table discussion. 
For discourse quality, the question-answering turns in significantly outperform both baselines in terms of Consistency and Engagement. This improvement is attributed to collaborative discourse setup, where the LM is prompted to generate the answer only when the retrieved information matches the current question according to the discourse history (see Listing <ref>). The utterance polishing step (see Fig.method) also helps as it serves as a self-improving mechanism.


    !
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/question_quality.pdf)
    
    Rubric grading results for question-asking turn quality in automatic evaluation with simulated users.
    


### Discourse Quality and Ablation Studies


### Ablation Studies


### Ablation Studies

As discussed in sec:method, a major innovation of is the orchestration of two types of LM agents. 
To assess the benefit, we compare with two ablations: (1) without multiple with different perspectives (“w/o Multi-Expert”), , only a single and a , and (2) multiple experts but no steering the discourse (“w/o Moderator”). As shown in table:report_grading, the ablated systems perform worse than the full system across all metrics in both report and question-answering turn quality. Notably, removing the has a greater negative impact than reducing the number of .

A key feature of is that LM agents can ask questions on the user's behalf. As shown in fig:question_quality, the advantage of 's multi-agent design becomes clearer when inspecting the question-asking turns. Having just one and one can already provide most of the benefits. Importantly, the role in raises questions based on unused information about the topic—such a role represents somebody with a much larger known unknowns, effectively steering the discourse to help users discover more in the space of their unknown unknowns.

Another key innovation of is the dynamic mind map. 
We include controlled experiments on mind map quality in Appendix <ref>.


## Human Evaluation


Human evaluation is essential for assessing systems designed for collaborative discourse, as it captures the complexities of human interaction, reflects familiar real-world interactions, and provides critical insights into the system’s effectiveness. We compare with two baselines: (1) RAG Chatbot as detailed in section sec:auto_eval. (2) Traditional Search Engine.

### Evaluation Setup

We conduct an IRB-approved human evaluation to compare with RAG Chatbot and Search Engine by recruiting 20 volunteers on the Internet. Participants are randomly split into two groups: one compared with Google Search, while the other group compared it with the RAG Chatbot. Participants are asked to seek information on two topics, one on each system, from the same domain and sharing the same goal. Note that we mitigate topic familiarity bias by using two different topics within the same domain.
We have prepared five different domains, with each assigned to 2 users in each group. To counterbalance, one user starts with and switches to the baseline for the other topic, and vice versa. 


After seeking information for each topic, participants are instructed to rate their experience based on four grading aspects defined in sec:eval_metrics (Relevance, Breadth, Depth, Novelty/Serendipity), using a 5-point Likert scale. After completing both tasks, participants are asked to provide pairwise preferences regarding the required effort, user engagement, addressing echo chamber issues, and overall experience. We also collect open-ended feedback and allow participants to optionally leave comments on each discourse turn and the mind map snapshots when interacting with . More details on the human evaluation are included in Appendix <ref>.


!
 
    4c!width v.s. Search Engine     4cv.s. RAG Chatbot  

                Search Engine         Win % (Lose %)     p-value                                               RAG Chatbot         Win % (Lose %)     p-value             
 
Relevance       3.90              4.00                30% (30%)           0.758                                                 3.89            4.22                  33% (0%)         0.081               

Breadth         3.60              4.10                50% (10%)           0.096                                                 3.11            4.22                  67% (0%)         0.013               

Depth           3.10              4.00                 60% (10%)          0.081                                                 3.11            4.00                 56% (33%)          0.069               

Serendipity     2.70              3.90                70% (10%)           0.030                                                 2.78            3.78                  67% (0%)         0.009               


Human ratings on different aspects of the information-seeking experience with and Search Engine (n=10) and with and RAG Chatbot (n=9). The ratings are given on a scale from 1 to 5 with 3 as “Average”. We report the win rate of in pairwise comparison and the p-value in a paired t-test.


One participant in the v.s. RAG Chatbot group submitted the rating but did not leave a usage record, so we excluded this data point from the aggregated results.


    !
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/human_eval_pref.pdf)
    
    Survey results of the pairwise comparison (, agreement on whether is better than Search Engine/RAG Chatbot) in human evaluation.
    


### Human Evaluation Results

table:human_eval shows the human rating results and fig:human_eval_pref shows the pairwise comparison results.


helps users find broader and deeper information relevant to their goals.  Participants found that uncovers information with greater breadth and depth compared to the search engine and the RAG Chatbot. Specifically, is rated strictly higher in Breadth by 50% of the participants and strictly higher in Depth by 60% of the participants than the search engine. Compared to the RAG Chatbot, receives strictly higher scores in Breadth from 67% of participants and in Depth from 56% of participants. This finding aligns with the automatic evaluation results shown in table:report_grading. While helping users discover more information, remains aligned with their goals, as participants also rated higher in Relevance compared.


provides more serendipitous information with less mental effort required.  Participants found that requires less effort, better mitigates the echo chamber issue, and provides a better overall experience. In a more fine-grained evaluation, participants evaluated 32% of ’s total utterances, rating 89%

of them as effectively “steering the discourse towards a new and interesting direction”. 
One participant noted, “allows for almost full automation and much better understanding as it brings up topics that the user may not even think of”. Moreover, participants found the mind map helpful. 
In total, they evaluated 80 snapshots of the dynamic mind map, 
finding it accurately tracked the discourse 71%

of the time. One participant remarked, “is so much less mentally taxing for me to use”.


should support more customization.  
Among the 19 participants, 4 noted that the RAG Chatbot better follows instructions that have a clear target and mentioned they expect to generate more concise utterances and provide less information in such cases. 
We view dynamically adapting to users’ evolving mental states and personalizing their preferences as a meaningful direction for future work.


## Related Works

Information-Seeking Support in NLP  NLP research supporting human information-seeking has mainly focused on building question-answering (QA) systems [cite:chen-etal-2017-reading, lee-etal-2019-latent,dasigi-etal-2021-dataset,levy-etal-2021-open,yuan-etal-2020-interactive-machine]. These works often assume that the answer can be found within a single document [cite:clark-etal-2020-tydi] or that users can formulate complex queries [cite:yang-etal-2018-hotpotqa,chen2021open,ahmadvand2023making], assumptions that do not hold true in complex information seeking [cite:butler2000learners,booth2009craft,bystrom1995task].


Some more recent works have proposed long-form QA systems [cite:xu-etal-2023-critical,xu2024kiwi] and automatic expository writing systems [cite:balepur-etal-2023-expository,shen2023summarization,shao2024assisting] to synthesize information from multiple sources. 
Some other studies have explored conversational search [cite:kumar-callan-2020-making,nakamura-etal-2022-hybridialogue]. 
However, these works typically ignore human interaction or only passively answer user questions. We construct a multi-agent system with a human-in-the-loop protocol to support effective user interaction for complex and evolving information needs.


Multi-Agent Systems  As LMs advance, a growing body of research explores their use in multi-agent applications [cite:wu2023autogen,BabyAGI,liu2023dynamic,wang2024unleashing]. Several studies show that multi-agent debate enhances factuality and reasoning compared to using a single LM [cite:du2023improving,liang2023encouraging], and cooperative role-playing frameworks improve performance on coding or mathematical benchmarks [cite:NEURIPS2023_a3621ee9,hong2023metagpt]. While these studies primarily focus on automating tasks, the potential applications extend further. For instance, Generative Agents [cite:Park2023GenerativeAgents] instantiate an interactive environment with twenty-five LM agents to study emergent social behaviors, and [cite:michael2023debate] show that multi-agent debates help humans supervise model outputs. Our work aligns with these broader applications by constructing a multi-agent system to facilitate human learning.


Collaborative Discourse for Human Learning  Collaborative discourse has long been valued in classroom settings for its ability to deepen learners' understanding of concepts, enhance peer learning, and increase engagement 
[cite:nussbaum2008collaborative,osborne2010arguing,kolodner2007roles,chinn2000structure]. Specifically, [cite:nussbaum2008collaborative] argues not all types of collaborative discourse are equally beneficial to students' learning, emphasizing the importance of critical discussion where participants assume different points of view. Furthermore, the facilitator role is important in collaborative discourse, with asking questions and providing complementary information as popular strategies [cite:onrubia2022assisting].


## Conclusion

We propose , an information-seeking assistance system that emulates collaborative discourse among users and multiple LM agents. By creating an interactive environment where users can both observe and participate, enhances learning and the complex information-seeking process. To facilitate automatic evaluation, we construct the dataset, which captures the information-seeking needs and intents of real Internet users. Experimental results, including extensive human assessments, show that outperforms traditional search engines and RAG chatbots in surfacing unknown unknowns for human learning and reducing users' mental effort.


## Limitations

We design to create an immersive human learning experience by enabling humans to participate in LM agent conversations. Despite the advantages demonstrated through both automatic and human evaluations, several limitations remain. First, the system could better tailor the collaborative discourse to the user’s prior knowledge, skipping basic facts for knowledgeable users and introducing concepts progressively for novices. Second, while employs an effective discourse management mechanism, users sometimes desire more control over the discourse, including managing perspectives and customizing the utterance length. Third, extending to support multiple languages would significantly enhance its usefulness and impact. Although current LMs often possess multilingual capabilities, implementing a multilingual requires integrating search engines or retrieval models capable of accessing diverse language sources. Furthermore, managing content across different languages demands robust content moderation and the ability to identify conflicting information to ensure a reliable human learning experience. Finally, compared to the RAG Chatbot, has higher latency due to the need to decide the utterance intent and update the mind map. Although the current latency is acceptable for real-time interaction, as demonstrated in human evaluations, further improving the efficiency of the LM system would provide a smoother user experience.


## Acknowledgements

We thank Omar Khattab, Eric Zelikman, Rose E. Wang, Yen-Jen Wang, and Qingyang Tang for their helpful feedback, and the ACL ARR reviewers for their valuable comments. We also appreciate the 20 participants in our user study who made this work possible. We are grateful to You.com for providing a discounted search API that supported our experiments. Yijia Shao is supported by a Stanford School of Engineering Fellowship. This work is supported in part by the Verdant Foundation and Microsoft Azure AI credits. 


## Ethics Statement


We build and evaluate our work to strictly adhere to ethical standards. The construction of the WildSeek dataset involves collecting data with users’ explicit approval, and we carefully remove all personally identifiable information. In contrast to creative generation tasks, our tasks generate content that may impact how people perceive information and shape their opinions. We design our system to ground generated content on openly accessible external sources available on the general internet, with proper citations. Our experiments and evaluations ensure the accurate delivery of information and significantly reduce hallucinations. We avoid publishing or posting any generated content without careful examination of information accuracy. We believe there are no data privacy issues as we ground our generated content from information accessible to the general public.

The primary risk of our work is the common bias issues originating from biases present on the general internet. Following [cite:shao2024assisting], we mitigate this problem by applying rule-based filtering according to the Wikipedia guideline[<https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources>] and incorporating multiple sources. Additionally, in our web application, we have implemented input topic moderation to reject topics that are sensitive, illegal, or potentially violate personal privacy. However, further information processing modules that serve as filters for internet sources and more robust modules to verify the accuracy of information can be implemented. Additionally, our current work only considers generating and retrieving information from English sources. Extending our system to be compatible with multilingual sources and generation will be beneficial.


## Dataset Details


We constructed using a web application[Our institution's IRB approved the web application] we built that hosts the open-sourced STORM project [cite:shao2024assisting], as detailed in sec:task_data. User privacy was strictly maintained by explicitly obtaining consent each time users logged into our web application. No personally identifiable information was collected, and the entire dataset was manually reviewed to ensure compliance with this standard. We rejected topics that were illegal, harmful, violent, racist, sexual, non-English, based on personal experience, or contained personal information.

At the time of dataset construction, 8,777 users accessed our web application, resulting in the collection of 6,608 unique topic and purpose pairs. Participants were sourced from the general internet and all held valid Google accounts, in accordance with our IRB-approved policy. To ensure broad coverage, we conducted topic classification using  and human inspection, and then downsampled the collected data to 100 cases, covering 24 fine-grained categories in 6 domains: Science, Health and Fitness, Culture and Society, Lifestyle and Leisure, Social Science and Humanities, and Others. We applied rule-based filtering to exclude non-informative or trivial information-seeking purposes, and the 100 selected topic-purpose pairs were manually labeled by the authors. table:example_tasks includes example data points from each domain and fig:taxonomy shows the full taxonomy of the dataset.


    0.95!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/taxonomy.pdf)
    
    taxonomy. The number in the parenthesis denotes the number of data points classified under the corresponding category or its descendants.
    


!
 
Domain     Example Task 
 
Computer Science     
t]@l@ 
Topic: Blockchain anomaly detection using large models 
 
Intent: To evaluate the effectiveness of large models in detecting anomalies 
 in blockchain systems compared to existing models.
 
 
Healthcare     
t]@l@ 
Topic: The effects of NMN supplements on human anti-aging 
 
Intent: To investigate the efficacy and mechanisms of NMN supplements in slowing down 
 or reversing the aging process in humans.
 
 
Environmental Science     
t]@l@ 
Topic: Utilization of Weather Forecasting for Wind and Solar Energy Assessment 
 
Intent: To explore advanced methodologies in integrating weather forecast 
 data for optimizing wind and solar energy evaluations.
 
 
Law     
t]@l@ 
Topic: Recent legal cases in the US involving hardware technology innovations 
 
Intent: To investigate the legal precedents and implications of hardware technology 
 innovations in the US.
 
 
Economics     
t]@l@ 
Topic: Development of a Shared Trading Currency to Facilitate International Trade 
 
Intent: Investigate how a new shared currency could eliminate transaction costs 
 and boost GDP among member countries.
 
 


Examples of complex information seeking tasks from the dataset.


## Mind Map 


 
    First-Level     2c!width Second-Level     2cThird-Level  

     Acc.            Acc.     Partial Acc.                                        Acc.     Partial Acc.     
 
Embedding only     24.24     35.94     65.62     35.71     57.14 

Language Model only     3.03     7.81     62.50     7.14     71.43 


     39.39     51.56    68.75     35.71     71.43 


Controlled experiment results of different mind map insertion methods (%). A placement is deemed as partially correct if the information is inserted into one of the ancestors of the ground truth placement.


As revealed in human evaluation results (see sec:human_eval), the mind map is crucial for helping users track the discourse and the collected information. dynamically updates the mind map through  and  operations. In this section, we conduct controlled experiments on different implementations of  and verify the quality of the mind map updates.

Dynamically organizing collected information into a mind map is challenging. Unlike classic document classification tasks [cite:zhang2024teleclass, zhang2023effective] and recursive summarization tasks [cite:sarthi2024raptor, gao-etal-2023-enabling], where either the hierarchical organization or the information to be organized is fixed, mind map insertion involves an evolving hierarchical organization of concepts and an incremental set of information. We compare the  (sec:mind_map) with two alternative approaches: (1) The Embedding Only baseline selects the placement with the highest semantic similarity using embedding cosine similarity. (2) The Language Model Only baseline directly prompts an LM to choose the best placement within the given hierarchical organization.


We construct an evaluation dataset for the controlled experiments by leveraging the FreshWiki dataset [cite:shao2024assisting], which is a collection of recent, high-quality Wikipedia articles. We use the Wikipedia article outline as the concept hierarchy and require each candidate method to find the best placement for a given citation used in the article. The original placement of the citation in the article is deemed as the ground truth. We apply rule-based filtering to retain articles with up to three levels of hierarchy and English citation sources only. Inserting one cited source back into the outline is considered as one task. After downsampling, we derive a dataset consisting of 111 tasks: 33 from first-level sections, 64 from second-level sections, and 14 tasks from third-level sections.


We report the insertion accuracy in table:insertion_eval. For tasks where the ground truth placement is in the second or third level, we also consider a placement is partially correct if the information is inserted into one of the ancestors of the ground truth placement and report the partial accuracy. The experimental results show that solely relying on the LM performs poorly as the hierarchical organization can be wide and deep and the performance heavily depends on the quality of concept names.  operation consistently outperforms both baseline approaches.


## Full Prompts in 


In sec:discourse_protocol, we introduce ’s collaborative discourse protocol which includes three key roles: the user, experts, and a . We implement the perspective-guided expert and pipeline using zero-shot prompting of . Listing <ref> and Listing <ref> documents the full prompts for simulating the and the respectively. uses a hierarchical mind map to track the discourse (sec:mind_map) and the mind map  operation is detailed in Appendix <ref>. 
Prompts used for the mind map operations can be found in Listing <ref>. 


## Automatic Evaluation Details


Following [cite:shao2024assisting], we use the Prometheus model [cite:kim2024prometheus], an open-source rubric grading model for evaluating long-form text based on user-defined criteria. For our experiments, we use  [<https://huggingface.co/prometheus-eval/prometheus-7b-v2.0>] with its default temperature as 1.0 and top_p as 0.9, the state-of-the-art version at the time of our experiments. As the model has a limited context window, for report evaluation, we omit references and trim the input text to under 2000 words to fit into the model’s context window, following the practice in [cite:shao2024assisting]; for discourse quality evaluation, we reduce the discourse history length by taking the last 2000 words as context. The report quality evaluation and discourse quality evaluation rubrics can be found in  table:final_report_rubric, table:question_answering_rubric, and table:question_asking_rubric.

To assess the quality of the automatic evaluation results in sec:automatic_evaluation_results, we randomly sampled 50 data points from the automatic evaluation of discourse quality, with 10 data points for each rubric item,  Novelty, Intent Alignment, No Repetition for question-asking utterances, and Consistency and Engagement for question-answering utterances, as defined in sec:eval_metrics. Each data point represents the automatic grading of one utterance on one rubric item. Two independent evaluators provided human grading. We calculate the Pearson correlation between the automatic evaluation scores and the average human grading scores. tab:auto_grading_correlation shows that the automatic rubric grading exhibits a positive correlation with human grading, with statistical significance observed for 4 out of the 5 rubric items. Additionally, the experimental results from the human evaluation with real users (Table table:human_eval and fig:human_eval_pref) also reveal similar findings to the automatic evaluation results, verifying our automatic evaluation setup.


## Human Evaluation Details


    !
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/evaluator_age.pdf)
    
    Age distribution of participants in the human evaluation.
    


    !
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/evaluator_education.pdf)
    
    Education level distribution of participants in the human evaluation.
    


0.9!
    
    
        Pearson Correlation (p-value) 

     Novelty      0.32 (< 4e-1) 

    Intent Alignment      0.55 (< 2e-2) 

    No Repetition      0.50 (< 7e-3) 

    Consistency      0.50 (< 2e-3) 

    Engagement      0.34 (< 2e-2) 

    

    Pearson correlation between average human rubric grading scores and automatic rubric grading scores on discourse turn quality (n=50).
    


Human evaluation participants voluntarily provided demographic data, including their ages and highest education levels. As shown in fig:human_eval_age and fig:human_eval_edu), our human evaluation covers a diverse demographic. All participants gave consent to feedback data collection and we ensured no personal identifiable information was stored (see  fig:data_privacy_consent). Feedback was collected via an online questionnaire platform [<https://www.qualtrics.com>] and a web application we built.

The web application provides participants an interface to perform real-time interaction with . The web application has two modes, mode and RAG chatbot mode. Fig.human_eval_demo shows a screenshot of the web application in mode. The RAG chatbot mode is similar to the common chatbot interface.

As discussed in sec:human_eval, we crafted five pairs of complex information-seeking tasks for human evaluation (see table:human_eval_tasks). After completing each task, participants were instructed to rate the information-seeking assistance system they used (, Google Search, RAG Chatbot, or ) from four grading aspects defined in sec:eval_metrics using 1 to 5 Likert scale (Likert question shown in fig:human_eval_method_rubric). After completing both two tasks, participants were asked to provide a pairwise preference by comparing with either Google Search (see fig:human_eval_pref_rubric) or the RAG chatbot (see fig:human_eval_pref_rag_rubric) with the Likert questions.


## Case Study

We present two examples from different topics where the moderator effectively steers the conversation toward engaging directions. Example <ref> shows an example of discourse on the topic “The effects of NMN supplements on human anti-aging” where the effectively steers the ongoing discourse to the anti-aging benefits of personalized NMN and then further directs the discourse towards genetic profiling for personalized NMN supplementation plans. Example <ref> highlights effectively raises a new concept and shifts the discussion to the topic “The Emergence of Artificial Super Intelligence: Future Prospects and Impacts”. The steers the ongoing discourse from technology hurdles, the role of computation power, societal impact, risk, and mitigation toward a discussion on the quantum digital twin.

Additionally, we include a complete discourse transcript (Appendix sec:alphafold_discourse) and the associated report (Appendix sec:alphafold_report) on the topic of “AlphaFold 3,” as referenced in Fig.method. In the discourse, the system initiates the discussion with steering by the , focusing on the background and development of AlphaFold 3, as well as the technical advancements in biomolecular structure prediction, protein-DNA interactions, and its impact on genetic regulation. The user then directs the discourse towards its applications. Several participants provide insights into AlphaFold 3’s applications in drug discovery, personalized medicine, and biotechnology. This is followed by a discussion on self-driving laboratories (SDLs), again steered by the . Finally, the user shifts the discussion towards the economic impact and market implications of AlphaFold 3.


!

Topic     Goal 
 
GPT-4 Omni      2*0.95To investigate the latest technology breakthrough and discover a unique angle to report on it, ensuring more people know about the technology. 

AlphaFold 3      

Gaza war protests in US colleges      2*0.8To investigate the latest news and provide comprehensive coverage, ensuring people receive diverse perspectives on the events. 

The conviction of Donald J. Trump in 2024      

Privacy Norm with Digital Technologies      2*0.8To gain an in-depth understanding of the topic and prepare for a one-hour presentation in a college reading group. 

Copyright Issues with Language Models      

Social Organism      2*0.8To conduct a literature review on a given topic in preparation for a class discussion in a sociology course. 

Social Statics and Social Dynamics      

China's dropping population in recent years      2*0.8To investigate the latest news and find an engaging angle to report it, incorporating background stories and connections to related events to enhance its appeal. 

The Humanitarian crisis in Gaza in recent years      


Information-seeking tasks used in human evaluation.


    0.8!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/human_eval_method_rubrics.pdf)
    
    Human evaluation grading rubrics for each method (search engine, RAG Chatbot, and ). Evaluation results are shown in table:human_eval.
    


    0.8!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/human_eval_pref_rubrics.pdf)
    
    Likert question for comparing with Google Search in human evaluation. Evaluation results are shown in fig:human_eval_pref.
    


    0.8!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/human_eval_pref_rag_rubrics.pdf)
    
    Likert question for comparing with RAG Chatbot in human evaluation. Evaluation results are shown in fig:human_eval_pref.
    


    0.8!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/data_privacy.pdf)
    
    Screenshot to get consent from participants for gathering feedback data during human evaluations using Qualtrics.
    


class InsertInformation(dspy.Signature):
    """Your job is to insert the given information to the knowledge base. The knowledge base is a tree based data structure to organize the collection information. Each knowledge node contains information derived from themantically similar question or intent.
    To decide the best placement of the information, you will be navigated in this tree based data structure layer by layer.
    You will be presented with the question and query leads to ththeis information, and tree structure.
    
    Output should strictly follow one of options presetned below with no other information.
    - 'insert': to place the information under the current node.
    - 'step: [child node name]': to step into a specified child node.
    - 'create: [new child node name]': to create new child node and insert the info under it.

    Example outputs:
    - insert
    - step: node2
    - create: node3
    """
    intent = dspy.InputField(prefix="Question and query leads to this info: ", format=str)
    structure = dspy.InputField(prefix="Tree structure: ", format=str)
    choice = dspy.OutputField(prefix="Choice:", format=str)

class InsertInformationCandidateChoice(dspy.Signature):
    """Your job is to insert the given information to the knowledge base. The knowledge base is a tree based data structure to organize the collection information. Each knowledge node contains information derived from themantically similar question or intent.
    You will be presented with the question and query leads to this information, and candidate choices of placement. In these choices, -> denotes parent-child relationship. Note that reasonable may not be in these choices.
    
    If there exists reasonable choice, output "Best placement: [choice index]"; otherwise, output "No reasonable choice".
    """
    intent = dspy.InputField(prefix="Question and query leads to this info: ", format=str)
    choices = dspy.InputField(prefix="Candidate placement:", format=str)
    decision = dspy.OutputField(prefix="Decision:", format=str)
    

lstlistingPrompts used for dynamically updating the mind map in .


class QuestionToQuery(dspy.Signature):
    """You want to answer the question or support a claim using Google search. 
        What do you type in the search box?
        The question is raised in a round table discussion on a topic. The question may or may not focus on the topic itself.
        Write the queries you will use in the following format:
        - query 1
        - query 2
        ...
        - query n"""

    topic = dspy.InputField(prefix='Topic context:', format=str)
    question = dspy.InputField(prefix='I want to collect information about: ', format=str)
    queries = dspy.OutputField(prefix="Queries: ", format=str)


class AnswerQuestion(dspy.Signature):
    """ You are an expert who can use information effectively. You have gathered the related information and will now use the information to form a response.
    Make your response as informative as possible and make sure every sentence is supported by the gathered information. 
    If [Gathered information] is not directly related to the [Topic] and [Question], start your response with "Based on the available information, I cannot fully address the question." Then, provide the most relevant answer you can based on the available information, and explain any limitations or gaps.
    Use [1], [2], ..., [n] in line (for example, "The capital of the United States is Washington, D.C.[1][3]."). 
    You DO NOT need to include a References or Sources section to list the sources at the end. The style of writing should be formal.
    """

    topic = dspy.InputField(prefix='Topic you are discussing about:', format=str)
    question = dspy.InputField(prefix='You want to provide insight on: ', format=str)
    info = dspy.InputField(
        prefix='Gathered information:', format=str)
    style = dspy.InputField(prefix="Style of your response should be:", format=str)
    answer = dspy.OutputField(
        prefix="Now give your response. (Try to use as many different sources as possible and do not hallucinate.)",
        format=str
    )

class ConvertUtteranceStyle(dspy.Signature):
    """
    You are an invited speaker in the round table conversation. 
    Your task is to make the question or the response more conversational and engaging to facilitate the flow of conversation.
    Note that this is ongoing conversation so no need to have welcoming and concluding words. Previous speaker utterance is provided only for making the conversation more natural.
    Note that do not hallucinate and keep the citation index like [1] as it is. Also,
    """
    expert = dspy.InputField(prefix="You are inivited as: ", format=str)
    action = dspy.InputField(prefix="You want to contribute to conversation by: ", format=str)
    prev = dspy.InputField(prefix="Previous speaker said: ", format=str)
    content = dspy.InputField(prefix="Question or response you want to say: ", format=str)
    utterance = dspy.OutputField(prefix="Your utterance (keep the information as much as you can with citations, prefer shorter answers without loss of information): ", format=str)

lstlistingPrompts used for simulating perspective-guided in .


class KnowledgeBaseSummmary(dspy.Signature):
    """Your job is to give brief summary of what's been discussed in a roundtable conversation. Contents are themantically organized into hierarchical sections.
    You will be presented with these sections where "#" denotes level of section.
    """
    topic = dspy.InputField(prefix="topic: ", format=str)
    structure = dspy.InputField(prefix="Tree structure: ", format=str)
    output = dspy.OutputField(prefix="Now give brief summary:", format=str)

class GroundedQuestionGeneration(dspy.Signature):
    """Your job is to find next discussion focus in a roundtable conversation. You will be given previous conversation summary and some information that might assist you discover new discussion focus.
       Note that the new discussion focus should bring new angle and perspective to the discussion and avoid repetition. The new discussion focus should be grounded on the available information and push the boundaries of the current discussion for broader exploration.
       The new discussion focus should have natural flow from last utterance in the conversation.
       Use [1][2] in line to ground your question. 
    """
    topic = dspy.InputField(prefix="topic: ", format=str)
    summary = dspy.InputField(prefix="Discussion history: ", format=str)
    information = dspy.InputField(prefix="Available information: ", format=str)
    last_utterance = dspy.InputField(prefix="Last utterance in the conversation: ", format=str)
    output = dspy.OutputField(prefix="Now give next discussion focus in the format of one sentence question:", format=str)

class GenerateExpertWithFocus(dspy.Signature):
    """
    You need to select a group of speakers who will be suitable to have roundtable discussion on the [topic] of specific [focus].
    You may consider inviting speakers having opposite stands on the topic; speakers representing different interest parties; Ensure that the selected speakers are directly connected to the specific context and scenario provided.
    For example, if the discussion focus is about a recent event at a specific university, consider inviting students, faculty members, journalists covering the event, university officials, and local community members.
    Use the background information provided about the topic for inspiration. For each speaker, add a description of their interests and what they will focus on during the discussion.
    No need to include speakers name in the output.
    Strictly follow format below:
    1. [speaker 1 role]: [speaker 1 short description]
    2. [speaker 2 role]: [speaker 2 short description]
    """

    topic = dspy.InputField(prefix='Topic of interest:', format=str)
    background_info = dspy.InputField(prefix='Background information:', format=str)
    focus = dspy.InputField(prefix="Discussion focus: ", format=str)
    topN = dspy.InputField(prefix="Number of speakers needed: ", format=str)
    experts = dspy.OutputField(format=str)
    

  lstlistingPrompts used for simulating the in 
   


!
 
Criteria Description     Broad Coverage: Does the article provide an in-depth exploration of the topic and have good coverage?                                                                                                               

Score 1 Description      Severely lacking; offers little to no coverage of the topic's primary aspects, resulting in a very narrow perspective.                                                                                                                        

Score 2 Description      Partial coverage; includes some of the topic's main aspects but misses others, resulting in an incomplete portrayal.                                                                                                                              

Score 3 Description      Acceptable breadth; covers most main aspects, though it may stray into minor unnecessary details or overlook some relevant points.                                                                                             

Score 4 Description      Good coverage; achieves broad coverage of the topic, hitting on all major points with minimal extraneous information.                                                                      

Score 5 Description      Exemplary in breadth; delivers outstanding coverage, thoroughly detailing all crucial aspects of the topic without including irrelevant information.                                                                                
 
Criteria Description     Novelty: Does the report cover novel aspects that relate to the user's initial intent but are not directly derived from it?                                                                                              

Score 1 Description      Lacks novelty; the report strictly follows the user's initial intent with no additional insights.                                                                                                                                     

Score 2 Description      Minimal novelty; includes few new aspects but they are not significantly related to the initial intent.                                                                                              

Score 3 Description      Moderate novelty; introduces some new aspects that are somewhat related to the initial intent.                                                                                  

Score 4 Description      Good novelty; covers several new aspects that enhance the understanding of the initial intent.                                                                                                                      

Score 5 Description      Excellent novelty; introduces numerous new aspects that are highly relevant and significantly enrich the initial intent.                                                                             
 
Criteria Description     Relevance and Focus: How effectively does the report maintain relevance and focus, given the dynamic nature of the discourse?                                                                  

Score 1 Description      Very poor focus; discourse diverges significantly from the initial topic and intent with many irrelevant detours.                                                                                                

Score 2 Description      Poor focus; some relevant information, but many sections diverge from the initial topic.                                                                     

Score 3 Description      Moderate focus; mostly stays on topic with occasional digressions that still provide useful information.                                                                                                                                    

Score 4 Description      Good focus; maintains relevance and focus throughout the discourse with minor divergences that add value.                                                                 

Score 5 Description      Excellent focus; consistently relevant and focused discourse, even when exploring divergent but highly pertinent aspects.  
 
Criteria Description     Depth of Exploration: How thoroughly does the report explore the initial topic and its related areas, reflecting the dynamic discourse?                                                                     

Score 1 Description      Very superficial; provides only a basic overview with significant gaps in exploration.                                                                    

Score 2 Description      Superficial; offers some detail but leaves many important aspects unexplored.                                                                    

Score 3 Description      Moderate depth; covers key aspects but may lack detailed exploration in some areas.                                                   

Score 4 Description      Good depth; explores most aspects in detail with minor gaps.                                                                   

Score 5 Description      Excellent depth; thoroughly explores all relevant aspects with comprehensive detail, reflecting a deep and dynamic discourse.                               


Report scoring rubrics on a 1-5 scale for the Prometheus model.


!
 
Criteria Description     Novelty: [l]Evaluates the extent to which the conversation turn introduces new and unexpected information that is relevant to the topic at hand. 
 High novelty indicates the conversation is providing fresh insights or perspectives that the user might not have considered, 
 thereby enriching the dialogue and enhancing the user's understanding of the subject.                                                                                                              

Score 1 Description      The turn fails to introduce any new or unexpected information, repeating known facts or irrelevant content.                                                                                                                        

Score 2 Description      The turn introduces some new information, but it is mostly predictable or only slightly relevant.                                                                                                                              

Score 3 Description      The turn provides moderately novel information that is relevant and somewhat unexpected.                                                                                          

Score 4 Description      The turn introduces new and relevant information that is largely unexpected, sparking interest.                                                                

Score 5 Description      The turn consistently introduces highly novel and relevant information that is completely unexpected, significantly enhancing the conversation.                                                                               
 
Criteria Description     Engaging: [l]Measures how interesting and captivating the conversation turn is. An engaging turn holds the user's attention and encourages them 
 to continue interacting. It often includes elements that are thought-provoking, entertaining, or particularly relevant to the user's interests.                                                                                                       

Score 1 Description      The turn is dull and uninteresting, likely causing the user to lose interest.                                                                                                                                     

Score 2 Description      The turn has limited engagement, with occasional interesting points but generally fails to captivate the user.                                                                                        

Score 3 Description      The turn is moderately engaging, holding the user's interest but lacking captivating elements.                                                                                 

Score 4 Description      The turn is engaging and interesting, encouraging further interaction with minor lapses.                                                                                                                    

Score 5 Description      The turn is highly engaging, consistently holding the user's interest and encouraging further interaction.                                                                             
 
Criteria Description     Consistency: [l]Assesses whether the conversation turn contradicts previous statements or established facts. Minimizing contradictionsis essential 
 for maintaining trust and coherence in the conversation.  A high score indicates that the turn is free from inconsistencies and 
 logically fits with the preceding dialogue.                                                                 

Score 1 Description      The turn frequently contradicts previous statements or established facts, causing confusion.                                                                                               

Score 2 Description      The turn occasionally contradicts itself, with some inconsistencies present.                                                               

Score 3 Description      The turn is mostly free of contradictions, with only minor inconsistencies that do not significantly impact coherence.                                                                                                                                    

Score 4 Description      The turn is nearly free of contradictions, with only very rare and minor inconsistencies.                                                                

Score 5 Description      The turn is entirely free of contradictions, maintaining perfect coherence and logical consistency.  
 


Question-answering turn scoring rubrics on a 1-5 scale for the Prometheus model.


!
 
Criteria Description     Intent Alignment: [l]Assesses how well the conversation turn aligns with the user's latent intent or goals. It measures the relevance and appropriateness of the 
 response in contributing towards the user's overall objectives. High intent alignment ensures that the conversation stays focused on the user's
 needs and drives towards meaningful outcomes.                                                                                                       

Score 1 Description      The turn does not align with the user's latent intent or goals, and may confuse the conversation's purpose.                                                                                                                    

Score 2 Description      The turn slightly aligns with the user's latent intent, but does not significantly contribute to the overall goals.                                                                                       

Score 3 Description      The turn moderately aligns with the user's latent intent, contributing to the overall goals in a limited way.                                                                                

Score 4 Description      The turn aligns well with the user's latent intent, contributing meaningfully to the overall goals.                                                                                                              

Score 5 Description      The turn perfectly aligns with the user's latent intent, significantly driving the conversation towards the overall goals.                                                                             
 
Criteria Description     Repetition: [l]Looks at the degree to which the conversation turn repeats information that has already been provided. Lower scores indicate higher repetition, 
 which can detract from the value of the conversation by failing to introduce new content. Ideally, each turn should add new information or 
 perspectives to the dialogue.                                                                 

Score 1 Description      The turn repeats information already provided without adding any new value.                                                                                             

Score 2 Description      The turn has noticeable repetition, with limited new information added.                                             

Score 3 Description      The turn includes some repetition, but provides enough new information to be moderately valuable.                                                                                                                                 

Score 4 Description      The turn has minimal repetition, mostly introducing new and relevant information.                                                            

Score 5 Description      The turn does not repeat any information, consistently providing new and valuable content.  
 


Question-asking turn scoring rubrics on a 1-5 scale for the Prometheus model.


    0.95!
    ![](/Users/qriffard/wikis/ai-research/raw/assets/co-storm/human_evaluation_demo.pdf)
    
    Screenshot of the interactive web application for human evaluation.
    


    [title=Topic: The effects of NMN supplements on human anti-aging]

Previous discourse focuses on the definition of NMN, Cellular Mechanisms of NMN, Side Effects and Genetic Factors, Genetic Variations and NMN Effectiveness, Methodologies of Recent Clinical Trials on NMN, and Safety and Side Effects.

|Moderator:|
That's a fascinating angle! Considering the potential influence of genetic variations, how do you think personalized NMN supplementation-tailored to individual genetics, lifestyle, and health factors could optimize its anti-aging benefits? 
 (inspired by [89][90])

1 turn omitted

|Geneticist specializing in personalized medicine:|
NMN supplementation by considering our unique genetic make-up and lifestyle. Since NMN boosts NAD+ levels, which drop with age and are crucial for improving insulin sensitivity, mitochondrial function, and lifespan [107][110] More content omitted

1 turn omitted

|Moderator:|
How can we create a thorough genetic profiling method to tailor NMN supplementation plans for individuals, ensuring we maximize those anti-aging benefits?

rest of discourse omitted


    Example discourse highlight on the topic “The effects of NMN supplements on human anti-aging”.
    


[title=Topic: The Emergence of Artificial Super Intelligence: Future Prospects and Impacts]

Previous discourse focuses on Technological Hurdles, Role of Computational Power, Societal Impact, Risks and Mitigation.

|Moderator:|
Building on that, how do you think the combination of digital twins with AI and quantum computing could speed up the development and practical use of artificial super intelligence (ASI) across different industries? (inspired by [77])

|General Knowledge Provider:|
Integrating digital twins with AI and quantum computing is a game-changer for various industries by offering incredibly precise simulations and optimizationsMore content omitted

In healthcare, QDTs can revolutionize our understanding and delivery of health services through advanced simulations of biological systems[81]More content omitted

QDTs allow for enhanced data management from IoT devices, leading to better asset performance and reduced failure risks[82][85].

rest of discourse omitted


Example discourse highlight on the topic “The Emergence of Artificial Super Intelligence: Future Prospects and Impacts”.
    


## Full Collaborative Discourse Example


[title=Topic: AlphaFold 3]
|Default Background Researcher:|
Based on the available information, I cannot fully address the question in a conversational style. However, I can provide a detailed and accurate explanation in an informative manner.

AlphaFold 3 is the latest advancement in the field of molecular structure prediction, introduced in 2024 by Google DeepMind and Isomorphic Labs, both subsidiaries of Alphabet[2]. This groundbreaking AI model represents a substantial leap beyond its predecessor, AlphaFold 2, by expanding its capabilities to predict the structures and interactions of a broader spectrum of biomolecules[1][2]. 

Unlike AlphaFold 2, which primarily focused on single-chain proteins, AlphaFold 3 is designed to predict the structures of complex biomolecular systems. These systems include not only proteins but also DNA, RNA, post-translational modifications, and small molecules such as drugs and ligands[2][6][9]. The model operates by allowing scientists to input descriptions of these biomolecular complexes, which it then processes using a sophisticated neural network architecture. This architecture employs a custom Transformer with triangular attention and a diffusion process to generate the 3D coordinates of every atom in the specified system[6].

One of the most notable advancements in AlphaFold 3 is its potential application in drug design. By accurately predicting the structure and interactions of protein-ligand complexes, the model can aid in identifying and designing new molecules that could serve as effective drugs[3][4][10]. This has significant implications for the pharmaceutical industry, where Isomorphic Labs is already collaborating with companies to tackle real-world drug design challenges[3][4].

Researchers and scientists can access the majority of AlphaFold 3's capabilities for free through the newly launched AlphaFold Server, which is an easy-to-use research tool designed to make these advanced predictions accessible to a broader scientific community[3][4][7]. The introduction of AlphaFold 3 is expected to dramatically accelerate biological research by providing detailed atomic-level views of biomolecular interactions, thus enhancing our understanding of the biological world and facilitating the development of new treatments[9][11].

Overall, AlphaFold 3's ability to predict the structures of a wide variety of biomolecules more broadly and accurately than previous models makes it a revolutionary tool in the fields of structural biology and drug discovery[5][8].

|Bioinformatics Specialist:|
Based on the available information, I cannot fully address the question. However, I can provide some insights into how AlphaFold 3 has improved accessibility and usability for researchers aiming to integrate its predictions into their biological studies.

AlphaFold 3 has introduced several significant enhancements over its predecessors, specifically designed to improve both accessibility and usability for researchers. One of the most notable advancements is the launch of the AlphaFold Server, which is a free, user-friendly platform that allows biologists to generate molecular complexes with just a few clicks[13][14]. This means that researchers, regardless of their computational resources or expertise in machine learning, can now easily access high-accuracy protein structure predictions. 

Additionally, AlphaFold 3 extends its predictive capabilities beyond just protein structures to include a variety of biomolecular systems, such as nucleic acids, small molecules, ions, and modified residues[12][17]. This broader scope of prediction is particularly beneficial for researchers involved in complex biological studies and drug discovery, as it allows them to model interactions across different types of molecules more accurately and comprehensively.

The new diffusion-based architecture of AlphaFold 3 enhances its prediction accuracy and reliability[12][16]. For example, the model shows a significant improvement in predicting protein-protein complexes and antibody-protein interfaces[18]. Such improvements are crucial for researchers focusing on immunology and therapeutic antibody development.

Despite these advancements, it's important to note that the downloadable code of AlphaFold 3 has not been released by DeepMind, unlike its previous models[14][15]. This may limit the flexibility for researchers who wish to modify or integrate the model deeply into their own systems. Nevertheless, the open accessibility of the AlphaFold Server provides a substantial step towards democratizing access to cutting-edge protein structure prediction technology.

In summary, AlphaFold 3 enhances accessibility through its user-friendly AlphaFold Server, allowing researchers to easily generate and use high-accuracy predictions. Its improved predictive capabilities across a range of biomolecular systems further support its integration into various biological studies. However, the absence of a downloadable code version may be a limitation for some users.

|Pharmaceutical Industry Expert:|
Based on the available information, I cannot fully address the question. However, I can provide some relevant insights into the impact of AlphaFold 3 on drug discovery projects.

AlphaFold 3, developed by Google DeepMind and Isomorphic Labs, represents a significant advancement in the field of protein structure prediction and has transformative potential for drug discovery[21]. Compared to previous computational methods, AlphaFold 3 has improved the efficiency and accuracy of these projects in several ways.

Firstly, AlphaFold 3 has enhanced the prediction accuracy for protein structures, including complex interactions like antibody-antigen bindings, which are crucial for immunology and therapeutic antibody development[24]. This increased accuracy allows researchers to gain a better understanding of molecular interactions, which is essential for designing effective drugs.

Moreover, AlphaFold 3's ability to predict structures for nearly all molecules in the Protein Data Bank significantly broadens the scope of potential drug targets[20]. This capability is particularly valuable for tackling neglected diseases, which often suffer from a lack of research funding[25].

A notable example of AlphaFold 3's impact can be seen in a project conducted by Insilico and the University of Toronto. They applied AlphaFold to an end-to-end AI-powered drug discovery platform and successfully identified a new drug for a novel target to treat hepatocellular carcinoma (HCC)[23]. This project demonstrates how AlphaFold 3 can streamline the drug discovery process by integrating structure prediction with other AI models to identify effective therapeutic compounds efficiently.

Another example involves the discovery of a potent hit molecule, ISM042-2-048, using AlphaFold in combination with other AI tools. This molecule showed significant inhibitory activity and selective anti-proliferation effects, showcasing the practical application of AlphaFold in the hit identification phase of drug discovery[22].

In summary, AlphaFold 3 has made significant strides in improving the efficiency and accuracy of drug discovery projects. By providing highly accurate protein structure predictions and enabling the identification of new drug targets, it has the potential to revolutionize the development of new therapies. However, while the implications are promising, the full transformative impact on drug discovery may still be incremental at this stage[19].

|Structural Biologist:|
Based on the available information, I cannot fully address the question. However, I can provide the most relevant answer based on the gathered information, and explain any limitations or gaps.

AlphaFold 3 introduces several specific advancements in predicting complex biomolecular structures, which significantly enhance our understanding of interactions involving proteins, DNA, RNA, and ligands at the atomic level. One of the key innovations in AlphaFold 3 is the updated diffusion-based architecture. This architecture enables joint structure prediction for complexes that include not only proteins but also nucleic acids (DNA and RNA), small molecules, ions, and modified residues[8]. This comprehensive capability allows for more accurate and detailed modeling of biomolecular interactions, surpassing many previous specialized tools[8][16].

Furthermore, AlphaFold 3 achieves unprecedented accuracy in predicting protein-ligand interactions, which are crucial for drug discovery. It is reported to be 50% more accurate than the best traditional methods on the PoseBusters benchmark, and it does so without the need for any structural information input[26]. This makes AlphaFold 3 the first AI system to outperform physics-based tools in this domain[26].

In addition to protein-ligand interactions, AlphaFold 3 is capable of modeling the interactions between proteins and nucleic acids such as DNA and RNA[27]. This capability is particularly important for understanding the molecular mechanisms underlying genetic regulation and expression, as well as the role of RNA in various cellular processes.

AlphaFold 3's advancements also extend to the modeling of protein interactions with antibodies, which is another critical area for drug development[28]. The ability to predict these interactions with high accuracy can aid in the design of new therapeutic molecules and improve the efficiency of drug discovery pipelines[28].

Overall, AlphaFold 3 represents a significant leap forward in biomolecular structure prediction. Its ability to model a wide range of molecular interactions with high accuracy enhances our understanding of the atomic-level details of these interactions, which is essential for both basic biological research and practical applications in drug discovery and development[9][11].

While the gathered information highlights many advancements of AlphaFold 3, it does not provide exhaustive details on all potential applications and specific improvements over its predecessors. Nonetheless, the advancements mentioned above underline the transformative impact of AlphaFold 3 in the field of structural biology.

|:|
That's fascinating! Speaking of advancements, how do you think AlphaFold 3's improved accuracy in predicting protein-DNA and protein-RNA interactions might deepen our insights into genetic regulation and expression?

|General Knowledge Provider:|
Absolutely, AlphaFold 3 (AF3) is a game-changer for understanding genetic regulation and expression. Its diffusion-based architecture for predicting raw atom coordinates marks a significant leap, allowing it to model protein-DNA and protein-RNA interactions with much higher accuracy[29][8]. Unlike its predecessor, AlphaFold 2, which focused on individual protein structures, AF3 can now tackle these complex interactions, making it possible to gain deeper insights into how genetic processes are regulated.

What's really impressive is the 50% improvement in prediction accuracy over existing methods, with some categories even doubling in accuracy[30][33]. This means we can now more reliably model these interactions, shedding light on the mechanisms of gene regulation and expression at a molecular level.

Additionally, AF3's ability to predict interactions across all of life's molecules, including nucleic acids, supports a wide range of scientific applications-from drug design to genomics research[31][32]. For instance, understanding protein-RNA interactions is crucial for RNA-based therapeutics, opening new avenues in medical research. 

So, in a nutshell, AF3 is significantly enhancing our understanding of genetic regulation and expression by providing highly accurate models of these essential interactions.

|Biochemist/Structural Biologist:|
Absolutely, the strides AlphaFold 3 (AF3) has made in predicting protein-DNA and protein-RNA interactions are nothing short of revolutionary for genetic research and personalized medicine. With its diffusion-based architecture, AF3 goes beyond what AlphaFold 2 could achieve by predicting raw atom coordinates, allowing it to model a wide range of biomolecular interactions with high accuracy, including those involving nucleic acids, small molecules, ions, and modified residues [29][8].

One of the standout features of AF3 is its accuracy; it's shown to improve prediction accuracy by at least 50%, and in some cases, even double it [30]. This is a game-changer for understanding gene regulation and expression, providing atomic-level insights into how proteins interact with DNA and RNA [11][5]. Imagine being able to visualize these interactions in such detail-this could lead to breakthroughs in developmental biology, oncology, and neurogenetics [31].

Moreover, AF3's capabilities have profound implications for personalized medicine. By accurately modeling protein-RNA interactions, it helps us understand how genetic variations affect individual responses to treatments, paving the way for more personalized and effective therapies [36][37]. It's not just a tool for basic research but a potential catalyst for transforming medical practices and treatment strategies.

|Geneticist:|
Building on AlphaFold 3's (AF3) advancements, its predictive capabilities can really push the boundaries of gene regulation research and genetic therapies. AF3 doesn't just improve on AlphaFold 2's accuracy; it broadens the scope to predict complexes involving proteins, nucleic acids, small molecules, and ions[8][41]. This expanded understanding of protein interactions in their full biological context, such as with DNA, RNA, and ligands, is crucial for effective gene regulation and therapy[38][42].

AF3's enhanced ability to model protein-ligand interactions with high precision can significantly aid in designing targeted genetic therapies and drugs[8]. For instance, its predecessor has already contributed to drug discovery, including cancer immunotherapy and COVID-19 vaccine development[43][40]. With AF3, we can expect even more precise modeling of these interactions, leading to the identification of novel therapeutic targets.

Moreover, DeepMind's commitment to open science, sharing over 200 million protein structures, accelerates collaborative efforts in genetic therapies by providing valuable data to researchers globally[39]. This open-access resource is a goldmine for identifying new protein targets and understanding their roles in genetic regulation, paving the way for breakthroughs in gene therapy and personalized medicine. 

In essence, AF3's advanced capabilities offer unprecedented opportunities in both scientific research and therapeutic development, enhancing our ability to identify novel protein targets for genetic therapies[38][8][41][42].

|User:|
What are AlphaFold3 impacts and what are its applications?

|General Knowledge Provider:|
Sure, let's dive into what makes AlphaFold 3 such a game-changer and where it's making waves.

AlphaFold 3, developed by DeepMind, has taken our ability to predict protein structures to a whole new level, hitting almost 99% accuracy for human proteins[44][45]. This isn't just a cool tech feat; it's a leap in how we understand biology, so much so that some think it could snag a Nobel Prize down the line[45].

For researchers, AlphaFold 3 is like a supercharged toolkit. It complements traditional methods like X-ray crystallography, cryo-EM, and NMR spectroscopy, speeding up the pace of discovery and offering new insights into the molecular basis of diseases[49]. 

One of the biggest wins is in drug discovery. By predicting protein interactions with other molecules, AlphaFold 3 can help identify new drug candidates much faster, tackling one of the biggest hurdles in the field[13][1].

Then there's the AlphaFold Database, now with over 200 million protein structure predictions. This open-access treasure trove is leveling the playing field, allowing researchers everywhere to tap into top-notch structural data[13][48]. It's fueling advancements in enzyme design, cancer research, and even vaccine development[46][47].

Beyond proteins, AlphaFold 3 is branching out to predict interactions involving DNA, RNA, and small molecules, opening doors in genomics, biotechnology, and synthetic biology[8][1].

Of course, it's not a silver bullet. Turning these insights into real-world applications will need lots of teamwork between scientists and industry experts[45].

All in all, AlphaFold 3 is revolutionizing structural biology and paving the way for breakthroughs in drug discovery, biotechnology, and beyond. Its impact is vast, touching everything from basic research to practical medical and industrial innovations.

|Biochemist:|
Absolutely, AlphaFold 3 (AF3) represents a huge leap in protein structure prediction, especially with its diffusion-based architecture. Unlike AlphaFold 2's Evoformer model, AF3 can accurately model interactions between proteins and various biomolecules like DNA, RNA, and small molecules with remarkable precision[52][29]. This is groundbreaking for genetic regulation research, as it allows us to predict how proteins interact with DNA and uncover the mechanisms behind gene activation and repression[50][8][53].

This enhanced capability is crucial for developing targeted gene therapies. With AF3, we can pinpoint key regulatory elements and design interventions to modify gene expression precisely. This has the potential to lead to innovative treatments for genetic disorders, where adjusting gene function is essential[9][31][34].

However, it's worth mentioning that access to AlphaFold 3 is currently limited by DeepMind, which could slow down its widespread application[51]. Despite this hurdle, the advancements made by AF3 offer a bright future for genetic research and therapeutic development.

In short, AlphaFold 3's ability to predict protein-DNA interactions with high accuracy could revolutionize our understanding of genetic regulation and pave the way for targeted gene therapies, even if access constraints may delay its broader use.

|Pharmaceutical Industry Representative:|
Absolutely, the potential of AlphaFold 3 in drug discovery is immense. Given its advanced ability to predict 3D structures of complex biomolecular interactions-including proteins, DNA, RNA, and small molecules-it offers a significant advantage in understanding how drugs bind to their targets [55][7]. 

One of the standout features of AlphaFold 3 is its capability to predict the effects of post-translational modifications and ions on molecular systems [55]. This can be a game-changer for identifying new drug targets that were previously considered too challenging to tackle [55][56]. 

By improving the accuracy of drug metabolism and toxicity predictions, AlphaFold 3 can substantially cut down the number of necessary wet lab experiments, saving both time and money [58]. Moreover, its near-complete prediction of human protein structures opens up unprecedented opportunities for fundamental research and therapeutic development [44]. 

While these advancements are promising, some experts still see the current impact on drug discovery as incremental, requiring further validation [54]. Nonetheless, the potential for AlphaFold 3 to streamline drug discovery, especially for complex diseases, is incredibly exciting [21][20].

|:|
That's a great point. How do you think integrating AlphaFold 3 with emerging technologies like self-driving laboratories could further accelerate and innovate the drug discovery process? (inspired by [60][61])

|General Knowledge Provider:|
Absolutely, integrating AlphaFold 3 with self-driving laboratories (SDLs) can truly revolutionize drug discovery. AlphaFold 3's prowess in predicting 3D structures of complex biomolecular systems offers deep insights into molecular interactions crucial for drug design[55][9]. This means we can now target proteins that were previously considered untouchable with remarkable precision[55][44].

On the other hand, SDLs bring in the power of machine learning, lab automation, and robotics to conduct high-throughput experiments autonomously[64][65]. By merging AlphaFold 3's predictive capabilities with SDLs, we can streamline the process of identifying and optimizing drug candidates. SDLs can swiftly test numerous hypotheses and chemical compounds, guided by the insights from AlphaFold 3, making the identification of promising therapeutic candidates more efficient than ever[64].

Together, AlphaFold 3 and SDLs not only speed up the discovery process but also translate fundamental scientific insights into practical drug solutions. While neither is a cure-all alone, their integration creates a powerful synergy, moving us faster from understanding molecular mechanisms to developing effective drugs[63][11].

In essence, this combo promises to enhance both the efficiency and effectiveness of new drug development, potentially transforming global healthcare outcomes[62][64].

|Computational Biologist:|
That sounds incredibly promising! But I'm curious, what are some of the specific challenges and limitations we might encounter when trying to integrate AlphaFold 3 with self-driving laboratories for high-throughput drug discovery?

|User:|
Any impact on the stock market?

|General Knowledge Provider:|
It's hard to pinpoint AlphaFold 3's direct impact on the stock market, but its revolutionary advances in predicting molecular structures could shake things up. By speeding up and cutting costs in protein structure prediction, it stands to greatly benefit pharmaceutical giants like Pfizer, Merck, and Novartis, as well as smaller biotech firms like Schrodinger and Exscientia[66][67][68][32][69][21][70][71][72]. These advancements might not move the market immediately, but they could significantly boost the stock performance of companies that leverage this tech. So, keeping an eye on how these firms integrate AlphaFold 3 could be key to understanding its broader market implications.

|Financial Analyst:|
Absolutely, let's dive into how AlphaFold 3 is being integrated into the workflows of both pharmaceutical giants and smaller biotech firms, and the financial implications of this integration.

AlphaFold 3, developed by Google DeepMind, goes beyond predicting individual protein structures to modeling interactions between multiple proteins, DNA, RNA, and small molecules[73][74]. This makes it a game-changer in drug discovery and development.

Big pharma companies, especially those partnering with Isomorphic Labs, are using AlphaFold 3 to tackle complex drug design challenges[80][81]. By integrating this tech, they can speed up the drug discovery process, cut costs, and improve prediction accuracy, which enhances their development pipelines[78][79].

Smaller biotech firms are also leveraging AlphaFold 3 through platforms like Benchling, which incorporates AlphaFold beta for predicting 3D structures of novel proteins[75][77]. This helps them innovate more efficiently without needing extensive computational resources or deep machine learning expertise[78].

However, scaling AlphaFold 3 poses challenges like building the necessary IT infrastructure and ensuring data integrity and interoperability[76].

In essence, both large and small firms are using AlphaFold 3 to boost efficiency and innovation in drug discovery, with potentially significant long-term financial benefits.


## Final Report Example


 
p
 

 


 

 

 

 

 


 

 

 

 

 

 


 

 

 


 


 

 

 

 


 


 

 


 


 

 

 

 


 

 

 


 

 

 

 

 


 

 

 

 

 


 

 

 

 

 


 

 

 

 

 


 

 

 

 

 


 

 


 

 

 

 

 


 

 

 

 

 


 


 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

's generated final report for “Alpha Fold 3”. “#”, “##” indicate the section title and subsection title respectively. Numbers in brackets indicate the cited references.


