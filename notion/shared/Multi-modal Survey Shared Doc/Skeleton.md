# Skeleton

*What topics/ideas/concepts should this survey include?*

1. Brainstorm Taxonomies
    1. Different RECENT approaches
    2. Criticize previous groupings (extend, flesh out)
2. 

---

Possible ideas

- Mech interp vs other types of interp (MI focuses on labeling internals and latent space repr like feature vectors)
- ViT and CLIP
    - Is it worth including a quick primer on these architectures? Or is that too much?
- Possibly extend to multimodal other than vision (audio, 3D physics, graphs, geometric mesh, etc.) to compare sims/diffs in models, and based on this, conjecture how mech interp can be applied in those areas (similar to how ViT has “token analogues” like patch embeddings; what does audio have?)
    - consult/co-author with researchers who have worked with those data types
- What patterns in approaches to interpretability are emerging, anything specific to multi-modality?
    - People love claiming that dictionary learning/sparsity -> interpretable
    - Specific to multimodal e.g. SpLiCE operates on the idea that representations in one modality are equivalent to another (?):
        - “Property 3.3. For the same latent concept vector ω, the CLIP image and text representations are equal to each other”

---

Steps to Taxonomy Brainstorm

1. Look at related work of a few (~5) state of art papers:
    1. Splice, RW approaches:
        1. Train different model (proxy models) - may merge with “post-hoc”
            1. Downstream CBMs or probes
            2. Dictionary Learning
        2. Take pre-trained then do post-hoc analysis
        3. Modify architecture then training
            1. STAIR: replace just a head with token prediction head

Mech Interp is too broad (not well defined either) and lop-sided on amount of papers

Merge groups into 1 if each is too specific

---

*Previous survey paper attributes*

- Identify trends and branching directions (different viewpoints) for unsolved problems
- Make a table with attribute columns of year, problem type, methods, objectives/topics, limitations
- Branching tree figure of topics to sub-topics to node of papers
- Background on topics (architecture, etc)
- Compare validity and effectiveness of methods used to tackle same problem
- Organize into **useful and new** categories (ie. identify new patterns across papers that were not recognized before, such as connective vs functional techniques)

*Survey papers to learn how to do good survey + comparisons:*

- [Toward Transparent AI](https://arxiv.org/pdf/2207.13243.pdf)
    - This is a broader topic so the paper is longer, while ours is more narrow and newer
    - What Nishant likes about this paper:
        - I enjoyed the very clear and bolded statements, super easy to tell what the paper is making a bold claim about.
        - It also makes very nice connections that people hypothesize about but are not necessarily fleshing out in their technical papers (because its hard)
    - What Nishant dislikes about this paper:
        - Felt a bit repetitive in some places, could be more succinct.
- [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549)
    - Multimodal model survey (not on interp) on the more recent LLMs like GPT-4 used with vision, so doesn’t mention older models like CLIP
- [Transformers in Vision: A Survey](https://arxiv.org/pdf/2101.01169.pdf)
- LLM interp survey

*Useful survey paper writing resources:*

- [What_is_a_Survey_Paper.ppt](https://docs.google.com/presentation/d/1gXHNhw0xshlyoDXXEAo11IpS1uk9bHj3/edit?usp=drive_link&ouid=116508571574321806982&rtpof=true&sd=true)
- [https://academia.stackexchange.com/questions/43371/how-to-write-a-survey-paper](https://academia.stackexchange.com/questions/43371/how-to-write-a-survey-paper)
- [https://academia.stackexchange.com/questions/167708/what-are-benefits-of-writing-a-survey-paper](https://academia.stackexchange.com/questions/167708/what-are-benefits-of-writing-a-survey-paper)
- [https://academia.stackexchange.com/questions/150773/is-it-worth-writing-and-publishing-a-survey-paper-while-a-phd-student](https://academia.stackexchange.com/questions/150773/is-it-worth-writing-and-publishing-a-survey-paper-while-a-phd-student)

Research survey papers typically range from 10 to 50 pages in length in academic journals, though this can vary. For conference proceedings, they might be shorter, generally around 6 to 12 pages. It is possible to write a survey paper even if only a small number of papers (like 10) have been published in the area. In emerging fields or highly specialized niches, early surveys can be particularly valuable. They help in setting the stage for future research, identifying gaps in the current literature, and proposing directions for new studies. Some survey papers are written by a single author, while others might have multiple authors, especially if the survey covers a broad or interdisciplinary area that requires expertise in multiple subfields.

---