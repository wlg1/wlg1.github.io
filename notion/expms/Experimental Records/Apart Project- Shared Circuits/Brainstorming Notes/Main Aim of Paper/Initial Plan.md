# Initial Plan

Brief summary
Very briefly, what is this project, what will happen, and why is it important? (You’ll elaborate on these points further below.)

The main aim is to discover how analogous prompts are calculated via circuits, and to check if there are circuits shared among analogous prompts. In addition to exploring this using established techniques, we aim to develop novel, more rigorous methods suited for this task both within and across models.

This is important to AI safety because we want to ensure that editing a circuit used for task A does not damage the model's performance on task B. Additionally, there may be non-human understandable shared components that lead to "illogical" decisions, and thus, would be very dangerous if not correctly identified. [ Elaborated on in 'Path to Impact'].

<<<
References
Links to other material relevant to the project that your future self or the mentor should have access to

Documents made with Notion and other tools will be created upon further project development. This will keep track of to-do lists, issues, team project tasks, schedules, and more.

Neel Nanda tutorials:
[https://www.neelnanda.io/mechanistic-interpretability](https://www.neelnanda.io/mechanistic-interpretability)

Callum Mcdouggall tutorials:
[https://github.com/callummcdougall/ARENA_2.0](https://github.com/callummcdougall/ARENA_2.0)

<<<
People I should consider talking to or getting feedback from

I have not connected with many researchers yet, so I will think about this more once I network with more people.

<<<
Research I have been reading or should consider reading

[https://arxiv.org/pdf/2211.00593.pdf](https://arxiv.org/pdf/2211.00593.pdf), [https://arxiv.org/abs/2305.19911](https://arxiv.org/abs/2305.19911), [https://arxiv.org/abs/2209.10652](https://arxiv.org/abs/2209.10652), [https://arxiv.org/abs/2305.01610](https://arxiv.org/abs/2305.01610)

References include:

Wang, K., Variengien, A., Conmy, A., Shlegeris, B., & Steinhardt, J. (2022).
Interpretability in the Wild: A Circuit for Indirect Object Identification in GPT-2
Small. [https://arxiv.org/pdf/2211.00593.pdf](https://arxiv.org/pdf/2211.00593.pdf)

Foote, A., Nanda, N., Kran, E., Konstas, I., Cohen, S., & Barez, F. (2023). Neuron to
Graph: Interpreting Language Model Neurons at Scale. arXiv preprint
arXiv:2305.19911

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., ... & Olah, C. (2022). Toy models of superposition. arXiv preprint arXiv:2209.10652.

Gurnee, W., Nanda, N., Pauly, M., Harvey, K., Troitskii, D., & Bertsimas, D. (2023). Finding Neurons in a Haystack: Case Studies with Sparse Probing. arXiv preprint arXiv:2305.01610.

<<<
How will your team members organize?
Please write the MOCHA roles for this project. Often, one of you will be the Owner with others acting as Helpers, our research mentor will be the Manager, and other co-authors will be the Consulted.

I am the only non-manager team member so far, but I am open to collaborating with others for this or any other project. I am interested in aiding another team project even if it is different from this project's topic.
Thus far: Owner (and potential Helper and Approver)- Michael Lan

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Objectives to impact

Primary Objectives

1. The main aim is to discover how analogous prompts are calculated via circuits, and to check if there are circuits shared among analogous prompts:
This problem is related to feature entanglement, in which performing model editing on one feature may change another correlated feature due to, for instance, editing polysemantic neurons. It is also related to superposition, which compresses multiple features into fewer dimensions. In this case, we are interested not only in which components are shared among features, but in how interacting components are shared among them.
2. Derive novel methods to find and measure shared circuitry:
While the hackathon project was an exploratory phase that straightforwardly applied existing techniques to investigate if analogous prompts shared circuits in one model, new methods may be developed to better tackle this problem. For instance, the project determined shared circuits only by looking for shared components. This may not be rigorous enough, as these components may also be shared by other non-related prompts and thus are not prompt-type specific; additionally, this approach does not show evidence that these components interact in similar ways.

<<<
Secondary Objectives

1. We aim to investigate this topic not just within a model, but to find similarities mapping across several LLMs with varying architectures.
2. We will attempt to develop methods to connect MLP functionalities with Attention Head functionalities in circuits. So far, much analysis has been done by separately looking at MLP neurons (eg. Finding Neurons in a Haystack) or Attention Heads (eg. IOI).
3. The hackathon project studied numerical sequences, but instead of specifically focusing on numbers, which may have their own complicated idiosyncarcities involving models performing mathematical operations, we may choose to focus on other types of prompts, such as superclasses to subclasses (eg. animals to species to dog breeds). This will help provide evidence to derive more general principles for multiple concept types.

<<<
Path to Impact

This is important to AI safety because:

1. In cases where only a targeted tweak to an AI's beliefs is necessary, model editing greatly reduces the expensive costs of re-training entire models, allowing for faster, more efficient alignment. We want to ensure that editing a circuit used for task A (eg. months) does not damage the model's performance on task B (eg. digits). If we do not know the greater impact that editing a model has on other tasks, that could lead to the AI developing hidden beliefs that deceive us. Thus, our goal is to minimize both adverse side effects and the costs of unforeseen risks.
2. We want to understand how AI determines concept similarity. In humans, superficial similarity often leads to "illogical" decisions, such as how one may dislike green vegetables because they "feel" similar to green bugs; there may be a shared neurological component that allows one to make this analogy. In AI, there may be non-human understandable shared components that lead to similar "illogical" decisions, and thus, would be very dangerous if not correctly identified.

<<<
Influence Plan
‍What concrete steps will we take to ensure the “Path to Impact” happens? E.g., who will we disseminate findings to, and how?

1. First, we will contact individual researchers to obtain information/connections to parties that may be interested in this work, as it may help build upon their own work or products. Contact may be done through email, Discord, in-person meetings, and more. This will help align our research to broader interests.
2. Next, we aim to present our work at conferences and workshops. This will also spread this work to researchers we otherwise would not know to contact.
3. Through these researchers, we will find larger organizations interested in this work. These include companies and university groups.
4. Lastly, we will present our results to a more general audience through mediums such as YouTube, including videos made in a 3Blue1Brown-style.

<<<
Methods/Accuracy Plan
‍How will we ensure the project is adequately reviewed and makes accurate claims? How will we make sure we don’t omit relevant information?

1. When conducting exploratory analysis using existing techniques that are considered well-established by the research community, we will contact paper authors to see if they have time to ensure that we are applying their methods correctly.
2. We will post to LessWrong and other forums to obtain feedback.
3. We will obtain feedback from peer review.

<<<
Scope
‍What questions/topics will be in-scope? What questions/topics will be out of scope? For what questions/topics are you not sure whether they should be in scope, and roughly when and how will you decide that?

In-scope:

1. We perform experiments on specific prompt types to obtain evidence for or against our hypotheses.
2. We will analyze toy, small, and medium size models (eg. GPT-Neo, with 2.7B parameters).

Out of scope:

1. Given that we still require more evidence to deduce general principles, this work will mainly be exploring what are good ways to conduct experiments for this problem, and to analyze their results. It will avoid making bold claims about general principles, as that requires more evidence on more prompt-types and models.

More questions/topics will be rated as in-scope or out-of-scope as more preliminary work is done to scout for feasible tasks to tackle.

<<<
[https://asq.org/quality-resources/fmea](https://asq.org/quality-resources/fmea)[https://pmstudycircle.com/failure-mode-and-effect-analysis-fmea/](https://pmstudycircle.com/failure-mode-and-effect-analysis-fmea/)
Failure Modes
Write possible failure modes for this project in the following format:
[Failure mode]: [Description] ([Likelihood]) [How can/will this failure mode be mitigated]

Failure to find shared circuits: Even if we find shared attention heads and MLPs for analogous prompts, these may not be shared circuits.
(Likelihood): Likely
Mitigation: Double check if the techniques are properly utilized. If they are, revise the approach and experiment on refined hypotheses using what we learn from our mistakes.

Lack of adequete computing resources: The project may require running/training models that require more computing resources (eg. GPUs/TPUs).
(Likelihood): Likely
Mitigation: Estimate the costs for running/training models based on experimental outline beforehand. Adjust these costs as more experimental tasks are added. When a lack of resources is reached, look for cost-effective providers to obtain more resources from, or scale down the experiments if possible.

Inactive team member(s): Members of the team may not be able to continue the project, due to a life issue or another unexpected event.
(Likelihood): Unlikely
Mitigation: The inactive member's tasks will have to be divided among the team, and new members or temporary substitute will have to be sought. As of now, I am the only non-manager team member, and I do not have any foreseeable risks for being inactive.

<<<
Early stopping points
‍We should end a project early if it isn’t getting the desired results. What would you look for to decide to stop early? Where would be some good early stopping points? When might these occur?

1. If we cannot find shared components for analogous prompts after trying a certain number (say, 4) of well-established techniques, we will move onto other types of prompts. Similarly, if we cannot do this for a model, we will try another type of model, such as a simpler toy model. We may take 1 week to explore each technique, and thus, this phase may last around a month.
2. If after a month, the approach does not yield positive results, we will re-adjust the task, re-adjusting more general topics and brainstorming new hypothesis as more specific candidates fail.

For instance, we will look for circuits in each prompt, then check if analogous prompts share components. We will use multiple techniques to try to find circuits, and double check if we are using them in the correct context. If we are using them correctly, yet still do not find shared circuits, we declare that it is not worth further investigation for this prompt type (eg. animal classes). Then, we will move onto a new topic that shows better promise.

<<<
Time Sensitivity
‍Are there any relevant external deadlines? Why?

I will be working on a few other projects