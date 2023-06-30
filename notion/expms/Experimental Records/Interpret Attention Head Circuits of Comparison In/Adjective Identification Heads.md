# Adjective Identification Heads

[adj_iden_circuits_DRAFT.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/adj_iden_circuits_DRAFT%20ipynb%207e1a22ebddc44a51b2b1d6570bec0b0f.md) 

Look for Adjective Identification Heads

Copy values for adjs can also be used for adj heads, without needing a circuit.

Adjective moving:

Bob is blue. Mary is Red. Bob is

Note these aren’t as strong as subject finders, but are still consistent. So there’s some signal distinguishing them.

<<<

Adjective mover input tests:

In the previous notebook, simple_analogies_pt2:

[https://www.notion.so/Simple_analogies_circuits-766fb391cad246da9150bcd5d98248a4?pvs=4#e3ec672cd08846699eeea020c4d4f9af](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/simple_analogies_circuits%20ipynb%20766fb391cad246da9150bcd5d98248a4.md)

We did not test these simple adjective mover inputs, but instead tested more complex ones that required the model to understand transitivity, “has”, and analogies. Make a new notebook to test more adjective mover prompts using GPT-2-small:

[adjective_mover_prompts.ipynb](../Code%20Notebooks%20432b45bb746f43eabf4172f69d384f8a/adjective_mover_prompts%20ipynb%20cf8a6d9206fb47588b60c921c090b348.md) 

[https://colab.research.google.com/drive/1e70-iPdPprDXCis-TnyJ64tFhFPS3Xej](https://colab.research.google.com/drive/1e70-iPdPprDXCis-TnyJ64tFhFPS3Xej)

- EXPM: Test if it is checking for the actual correct adjective, or if it's doing something else such as outputting the most recent adjective, the least recent adjective, etc.
    
    DESC: Test if it is checking for the actual correct adjective, or if it's doing something else such as outputting the most recent adjective, the least recent adjective, etc. In any case, it is moving adjectives. Or perhaps not moving the same ones, but "identifying" similar ones.
    
    RESULT: This shows that it doesn't always work. Still, it "identifies color". 
    
- EXPM: Try different colors
    
    RESULT: This also fails. We can say it's not adjective movers.
    
- EXPM: "Bob is tall. Mary is green. Bob is”
    
    RESULT: 1st is ‘a’, 2nd is ‘tall’
    
    When trying "Bob is tall. Mary is big. Bob is”, it has similar rankings.
    
    "Bob is big. Mary is small. Bob is” : similar to before
    
    "Bob is smart. Mary is strong. Bob is” : similar to before
    
    ANALYSIS: Is there a way to make it not output articles?
    
- EXPM: "Bob is not smart. Mary is smart. Bob is”
    
    RESULT: This successfully says “not” by 26%, and “smart” by only 10% in 2nd place. 
    
    TRY: let’s see if sentences have consistent “not” outputs using in-context. See if it does ti CORRECTLY (not on Mary)
    
- EXPM: "Bob is smart. Mary is not smart. Bob is”
    
    RESULT: It successfully outputs “smart” instead of “not”. 
    
    ANALYSIS: So here, it’s not just outputting “not” because “not” exists.
    
- EXPM: "Bob is not big. Mary is big. Bob is”
    
    DESC: Also test:
    
    - "Bob is big. Mary is big. Bob is”
    - "Bob is not big. Mary is not big. Bob is”
    
    RESULT: All yield correct expected output
    

We predict that running more tests will also not give consistent correct answers. We avoid the ones that output articles like “a”. Even if they don’t consistent give what’s right, they still give some sort of adjective. Instead of looking for heads identifying exact adjectives, we look for ones which have “something to do with adjectives”. This means it must still target adjectives in the input, then “move” that to perhaps an adjective-focused attention head or adjective-focused MLP.