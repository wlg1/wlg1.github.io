# PLAN- Size Comparison Circuits and Neurons

Previously: [tall_short_neuron_investigation.ipynb](../../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/tall_short_neuron_investigation%20ipynb%20b6fb8fd5adfc47f4b7b737249042ae53.md)

Expm blocks: [EB- Analysis on Inputs for Tall vs Short](../../Experimental%20Results%208545f5a36448499c934d8659ba08d2c1/EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8.md) 

[tall_short_circuit_draft.ipynb](../../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/tall_short_circuit_draft%20ipynb%2060d5d6b60d014ebd950e958ed1264c6a.md) 

### Working on

[Size Comparison Congruence](PLAN-%20Size%20Comparison%20Circuits%20and%20Neurons%201111d95ef57b4131b259ef88363f3010/Size%20Comparison%20Congruence%20e94368b6a22a4e9e9d0d444b3c5972e5.md)

### Done

- State Goals and brainstorm starting points
    
    We want to use path patching, so we look for code that used it. This is the only notebook using path patching found so far: IOI Notebook.ipynb
    
    [https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing#scrollTo=qYdX5EoB4uuL](https://colab.research.google.com/drive/1n4Wgulv5ev5rgRUL7ypOw0odga9LEWHA?usp=sharing#scrollTo=qYdX5EoB4uuL)
    
    The other one for the pronoun circuit uses ACDC (autoamted path patching)
    
    Thus, just take code from the IOI notebook and use it for new tasks
    
- Dot prod of large and huge and decline

### Future Work

- NOTE: IOI paper only used single tokens, and attempts at “averaging” multiple did not go well, so just use single tokens
- Find neurons. How do they interact in a circuit with each other?
    - How are its weights related to features? They ARE in the same direction.
    - “External knowledge” like big vs small- isn’t that stored in MLPs? How do MLPs interact with attn heads to combine knowledge with patterns (of moving info by circuits)? Do certain circuits attend to certain MLPs of “processing info”? (ROME showed the exact MLPs didn’t matter as long as in middle; but is that due to “analogous” shfits in attn also mean analogous shifts in MLP? is it due to backups?
- Find circuit. How does this combine information from MLP weights?
    - See ‘pronoun circuits’ to see circuits not targeting just info, but external semantic knowledge (eg. knowing Mary is ‘she’)
        - How do you input the tokens to ACDC?
    - Query and key weights connect tokens and features
- Check if similar heads for “synonyms”, “same type of opposites comparisons (large/small, black/white, man/woman, king/queen, etc)
- Check how embeddings get more similar over time
- Trace thru a token by dot product sequences. What is obscured (not findable) by this approach? Why must locate components it uses by actv patch over other methods?
- Dot prod of Chihuahua with dog+small, like king queen
- Give the embedding or dot of embs to gpt to see if it recognizes it, in some universal way
- Generalize causal trace to patch any component
- Test hypothesis: The outgoing weights of a neuron matches a feature if it’s in a similar direction as the feature vector. (test for similar words)
- Neuron feature arithmetic. Attention weights artih?
- Try multiple prompts about bigger vs smaller to see if there are composites for it

Draft Final Products

- Circuits by patching
- Neurons + Embeddings Congruence (similarities)