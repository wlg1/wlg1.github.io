# EB- Analysis on Inputs for Tall vs Short

- EXPM: See what GPT-2-large outputs given prompts that intend to output opposite adjectives such as:
    
    > "John is tall. Mary is”
    > 
    
    DESC:
    
    RESULT: 
    
    Yes, GPT-2-large is able to say “short”
    
    ANALYSIS:
    
    REFS: 
    
    [https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx](https://colab.research.google.com/drive/1GQo_RSEY40ncByvwy81kxwSKGPHlbxSx)
    
    [https://www.notion.so/Brainstorm-about-relations-between-analogy-order-task-and-IOI-task-d6428f8228444e4584e2a30fc993b59a?pvs=4#43532eb8a7584f9895795ae380ec754f](https://www.notion.so/Brainstorm-about-relations-between-analogy-order-task-and-IOI-task-d6428f8228444e4584e2a30fc993b59a)
    
- EXPM: Continuing analyzing the prompt above, observe the logit lens diff for “short” vs “tall”
    
    
    RESULT:
    
    ![Untitled](EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled.png)
    
    The values near 0 mean it weights tall and short around the same. The negative means it weighs tall more. Then near the last layers, it shoots back up to positive and thinks short. Why? Look at the attention heads involved in the last few layers.
    
- EXPM: Check the attention heads of the prompt above
    
    ![Untitled](EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled%201.png)
    
    Head 14, Layer 30 stands out
    
    We want to look for the heads near the last layers that are responsible for
    
- EXPM: Add a source system in input and check logit diffs
    
    DESC: Test the following:
    
    > **"John is big. Mary is small. John is tall. Mary is"**
    > 
    
    A “source system” means there is a “template example” in the input from which the model can use in-context learning on. The model makes analogies from the source system example. Eg) The source system in the test input is: “**John is big. Mary is small”**
    
- EXPM: Will adding a source system prevent the model from even considering tall over short within its layers?
    
    
    DESC: 
    
    Hypothesis: The source system is expected to make the model “more sure” of what to output b/c it has an example to draw in-context learning from on what it’s expected to do. It wants to follow a pattern.
    
    No source system:
    
    ![Untitled](EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled.png)
    
    With source system:
    
    ![Untitled](EB-%20Analysis%20on%20Inputs%20for%20Tall%20vs%20Short%20370cf22d285243ec9dd1f4ad9e25efe8/Untitled%202.png)
    
    There's still a dip. But compare it to before. Before there were two dips, and they were deeper. Also, the end logit diff is bigger now. Could the source sentence be making it "more sure" of "short", through in-context learning and induction heads? Try more examples of "no source" vs "source".
    
    First check the last layer logit diffs in 'test prompts'. Then compare how their layers logit diff changes; is "with source sys" more sure throughout the layers? The (inductive based) hypothesis is that it will be, given this one example.