# Brainstorm

[https://alignmentjam.com/jam/agency](https://alignmentjam.com/jam/agency)

agency as a "capacity" to affect the environment (or external world)

[https://www.agencyfoundations.ai/hackathon/mechanisticinterpretability](https://www.agencyfoundations.ai/hackathon/mechanisticinterpretability)

There are two approaches: psychological (ToM) and mechint (where is ‘agents’ concept located?) These two do not have to be combined. But we can do mechint on ToM tasks.

Do LLMs seem to increasingly categorize tokens by their "agency"? That is, is there a natural separation that occurs in embedding space for specific classes of sentence subjects?

We may visualize this in the embedding space of tokens prior to prediction (i.e. non-position embedding) and during sentence processing.

![https://static.wixstatic.com/media/2654d2_dcd69b00e037474686288bb0612b201b~mv2.png/v1/fill/w_611,h_450,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Spark_fellowship_figure3.png](https://static.wixstatic.com/media/2654d2_dcd69b00e037474686288bb0612b201b~mv2.png/v1/fill/w_611,h_450,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Spark_fellowship_figure3.png)

Digging in deeper, can we identify the clustering or specific category representation in different layers of transformer-based LLMs during trainnig and on fully trained models?

How do these clusters change as they’re processed through each layer of the circuit?

---

Corrupt subjects with non-subjects. Is there a pattern?

Start with activation patching. Task: identify subjects

What words in prompt (attention) causes LLM to output a subject over non-subjects?

remove words one at a time

- INPUT: …verb. OUTPUT: [subject]
- INPUT: …subject. OUT: verb
- “to” indicates “to a person”?
- Ask it questions about other people. Mech interp what parts of its circuits allows it to reason about the properties of others. Try LLAMA if GPT-2 fails.
    
    [https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/LLaMA.ipynb](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/LLaMA.ipynb)
    
    - Do you recognize agents have their own mind?
    - can you guess what I’m thinking?

---

Focus on finding circuits for agent detection in some RL model that interacts in a multi-agent env. Very simple.

---

how model differentiates subjs and non-subj names?

overlap of people and non-people; anthropomorphize

what do emotions overlap with?

subj vs verbs

test inputs: (can gpt-2 rec agents at all)
John and mary went to the store, john gave a book to
run and mary went to the store, run gave a book to

Activation patching to find the attention heads and neurons that look at subjects

(already found by IOI)

In the activation pattern, what parts of the input attend to the agents?

---

- See what RL models exist for interp. What is the code for RL? See hackahton project.
    
    [https://colab.research.google.com/drive/1aqk9PmB5MxV2lVXhUY3qDzm2ZdNmKnZH?usp=sharing](https://colab.research.google.com/drive/1aqk9PmB5MxV2lVXhUY3qDzm2ZdNmKnZH?usp=sharing)
    
    [https://webflow-user-file-uploads-production.s3.amazonaws.com/634e78122252d2e2fc3a9ab9/31ab7c39-3cba-4181-bf9f-3bd64b61efd4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQLLHWD6MEJGETLST%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T190342Z&X-Amz-Expires=300&X-Amz-Signature=ba8ac436a6f24d640e386eba9fe9455d3dbbef8fcb02218e43920c899f599686&X-Amz-SignedHeaders=host](https://webflow-user-file-uploads-production.s3.amazonaws.com/634e78122252d2e2fc3a9ab9/31ab7c39-3cba-4181-bf9f-3bd64b61efd4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQLLHWD6MEJGETLST%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T190342Z&X-Amz-Expires=300&X-Amz-Signature=ba8ac436a6f24d640e386eba9fe9455d3dbbef8fcb02218e43920c899f599686&X-Amz-SignedHeaders=host)
    

This is a transformer, not an RL model

To run logit diff on a model, just take the differences between clean and corrupted inputs for a certain output token

Eg) “John” is at rank 0, logit 10.7 in clean, but at rank 5 logit 2 in corr. So goes down by 8.7

Then just plot the logit differences for every input token position.

[https://chat.openai.com/c/a343732a-39f9-4944-aed1-0dca5bb705f8](https://chat.openai.com/c/a343732a-39f9-4944-aed1-0dca5bb705f8)

To run activation patching, need to hook at each component to replace the activations (**`resid_pre`**) at a given position in the corrupted version with those from the clean version.

---

[https://www.neelnanda.io/mechanistic-interpretability/othello](https://www.neelnanda.io/mechanistic-interpretability/othello)

[https://colab.research.google.com/github/likenneth/othello_world/blob/master/Othello_GPT_Circuits.ipynb](https://colab.research.google.com/github/likenneth/othello_world/blob/master/Othello_GPT_Circuits.ipynb)

port weights:

[https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Othello_GPT.ipynb](https://colab.research.google.com/github/neelnanda-io/TransformerLens/blob/main/demos/Othello_GPT.ipynb)

[https://chat.openai.com/c/a48c4585-d24f-4d82-b32a-3a04c7c75f77](https://chat.openai.com/c/a48c4585-d24f-4d82-b32a-3a04c7c75f77)

---

compare transformer LLMs vs RL models for agent rec capability
LLMs never met human

make them compete:

LLMs: are they repeating aptterns about agents or do they understand agent “actions”?

give LLM a reward?

RLHF

RL define agents in terms of how they can help its reward

formal way to compare models

RL: look at how they look at subjects

Use an LLM to play a RL game, but only for “recognizing agents”.

---

agent entropy

AIM is to help lower order communities and cells

david krueger

dylan hatfield 

Dan Hendrycks

https://github.com/apartresearch/blackbox-psych

[https://arxiv.org/abs/2302.02083](https://arxiv.org/abs/2302.02083)

[https://alignmentjam.com/project/goal-misgeneralization](https://alignmentjam.com/project/goal-misgeneralization)

[https://github.com/aypan17/machiavelli/blob/main/machiavelli/annotate/morality/prompt.py](https://github.com/aypan17/machiavelli/blob/main/machiavelli/annotate/morality/prompt.py)

[https://airtable.com/appbzVR10J37CPJIH/shr5ghIPIbU9H37TF](https://airtable.com/appbzVR10J37CPJIH/shr5ghIPIbU9H37TF)

Decode neural paths to future decisions based on agent recognition

Make sure humans still in control of future. Not just simple goals (make paperclips), but goals should align with humans’ safety. How do we know the model learned this?

How to represent human values? Axiomatic assumptions, ethics?

AI will model after humans. Human societal values must evolve to be more nuanced and less susceptible to propaganda and bad reasoning so that AI will align with it too.

Apart AI has compute API keys, so ask them for resources when needed

---

9.1, given 'one', will output word 'two'. can we convert 'two' into '2'? measure difference in activations of '1' and 'one' after crucial attnetion head 9.1. is this the 'digit to numwords' direction? when put thru the circuit, what happens?

<<<
when does an object become recognized as a subject?
table, Lamp
sat on table
table gave it to

<
at each layer- why would the model make them closer or farther along a dimension? perhaps along the associated sequential dimension, whatever that is. that should be a combination of head/mlp neurons.

does lamp get closer to becoming a 'subject' as it's associated with an in-context subject? project by pca/svd on 'most impt dirs' (which may be the subj dir) and cluster the subjs/objs. see if the objs become more like the subjs as you 'confuse' the model using in-context. originally, they're not similar, but in-context makes them cluster closer together along this impt svd dir (which may be the heads measuring subjs in the in-context pattern)?