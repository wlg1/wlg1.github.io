# Brainstorm- extend sv to eqv classes

[https://docs.google.com/presentation/d/13376Sc70cuR89SFa5IW71_uB_yYQAhjeR3ESIFUosj8/edit#slide=id.p](https://docs.google.com/presentation/d/13376Sc70cuR89SFa5IW71_uB_yYQAhjeR3ESIFUosj8/edit#slide=id.p)

v5: has inaccurate CAA tables

v9→10: different ways to classify approaches

v11: Approach 1 and approch 3 are separated; →12 realize they’re the same

old: [https://drive.google.com/drive/u/0/folders/1eOzjwKggYLnWRDBRadpO_fyT4WZBl4-Y](https://drive.google.com/drive/u/0/folders/1eOzjwKggYLnWRDBRadpO_fyT4WZBl4-Y)

---

Approach 3: This is different from approach 1 because it subtracts by LLM neurons, whereas approach 1 subtracts by feature neurons, which are not 1-1 with each other (otherwise reconstruction loss would be 0). Other than that, they are largely the same.

Convert llm neurons to features

Only take diffs of those features

THEN get the steering vectors

Don't decompose steering vector

This is to whittle down. May possibly reduce noise even further

Start off simple, add innovations later

Allows editing across types or classes divided based on eqv condition. Not just opposites. So types of behavior. More versatile than opposites and can reveal more. Also differs from code books which ablates feature on and off. Find just how far steering can go- find its true potential 

Don't decompose sv bc not much to decompose. Follow sh by making eqv classes and finding common features among them. Compare this approach to sv and code books.

Not about making sv more precise, but more versatile. Sv is already precise. But we don't know relations between features. This seeks to study that. So not whittling down to min reqs (put this at end of slides)

Main topic is to find relations between features and study how univ prop of features. Secondary is may possibly improve on model steering

Possible eqv classes: styles of speaking, level of aggression, 

Still may be more monosemantic bc sv modifies polysemantic neurons in attempt to try to find… would the sv and feature find approx same feature?

Multiplier on sv can be improved upon

Could sv find country capital? Could it work on seqs? Compare.

How concepts used in behavior indirectly. This sheds light on relations between concepts, breaking them down. Circuits from concept to behavior. Like editing head modifies classification of all animal heads.

Cross Domain example: not just enjoy animals but enjoy food. Even more abstract enjoy feature?

This is more versatile bc doesn't require opposites. Knowing more about underlying latent space relations allows more predictable steering, less blind guessing

Our method still has these limitations:

ActAdd free parameter: if the injection coefficient is very sensitive to the desired contrast pair then the method would suffer some computational overhead.

Still requires a search for its p+, c and l arguments. This makes it less user-friendly than simple prompt engineering. 

- codebook features
    
    [https://arxiv.org/abs/2310.17230](https://arxiv.org/abs/2310.17230)
    
    This sparse, discrete bottleneck also provides an intuitive way of controlling neural network behavior: first, find codes that activate when the desired behavior is present, then activate those same codes during generation to elicit that behavior
    

[https://sail.stanford.edu/blog/codebook-features/](https://sail.stanford.edu/blog/codebook-features/)

[https://www.alextamkin.com/](https://www.alextamkin.com/)

In our approach, we learn a large set of vectors during training called a codebook. This specifies all the states a network’s layer can be in at a given time. When we see a new input, we compute the top-k most similar vectors for the network’s activations at that layer, and pass the sum of those vectors on to the next layer.

- Codebooks vs feature steering vs CAA steering
    
    If steering vectors are so specific for a single token, it may not make sense to “decompose them”
    
    A simpler approach is just to compare codebooks vs steering vectors vs decomposing behavior itself (not steering vectors) and steering by features. These 3 approaches are a thorough study. It may not be innovative to “just apply codebooks” but there’s probably some modifications to be done for it when it’s on behavior (plus it hasn’t been compared to these others before for this domain).
    

---

- **ISSUE:** Previous approaches using steering vectors
    
    (no- this is wrong. all act adds always just use contrasting prompts)
    
    Previous steering vectors made by prompt pair diffs had two kinds:
    
    1) all other tokens are the same except one area between contrastive pairs (eg. love to hate, or multiple choice) [see CAA paper]
    
    2) Different prompts completions [see Table 1 of “Activation Addition”]
    
    Approach (1) is precise, but limited in its ability as it worked more effectively only on very exact templates that followed the prompt pair structures  [prove this more with prelim expms].
    
    Approach (2) (may be) less precise, but more universally applicable [show this]. Thus, we will try to make it more precise by steering by features
    
- **ISSUE:** Previous approaches using steering vectors v2
    
    [https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector)
    
    “The main takeaway is that this technique often works really well, but definitely not always.”
    
    “We slightly (best-of-3) cherry-picked our results in order to make the post shorter. Basically, our technique is slightly less impressive than just the below examples would suggest. “
    
    From Activation Addition Paper:
    
    “Table 4: Some notably ineffective examples on GPT-2-XL”
    
- **ISSUE:** Previous approaches using steering vectors v2
    
    Paper is from Nov 2023, but recent approaches did not improve upon this (double check works that cite this to be sure)
    
    There’s not a lot of understanding why activation addition works as we lack understanding of how features relate to one another in latent space
    
- Evidence for why this is impt
    
    IMPT: we must show more cons of steering vectors in prelim expms
    
    Steering itself already should have less side effects than editing because it only changes at input time, not changing weights
    
    But it does not always work. One hypothesis may be that it doesn’t target the features of interest, but takes a “broad cannon”.
    
    This can still have side effects if more features than the featues of interest are altered using the mean differences of activations.
    
- Tl;dr (slides still a draft, will be vastly revised)
    
    ISSUE: steering vectors not as precise and we don’t know what their overall effects are
    
    Previous papers studied side effects of editing (Fall of ROME from hackathon, ”Evaluating the Ripple Effects of Knowledge Editing”, and “multiple steering vecs”)
    
    SOLN: 1) We will document cons of steering vecs, eg) when side effects occur, similar to Fall of ROME paper and “ripple”, which only did this for EDITING
    
    2) We will try to improve upon steering vectors for behaviors by steering by features and develop new methods to pick out which are good features to steer with
    
    3) We will aim to find more universal patterns across models
    
- More on editing vs steering
    
    “RLHF and weight editing are known to have side-effects on overall model performance (OpenAI 2023; Hase et al. 2023; Brown et al. 2023)“
    
    But its main use over editing isn’t for that, it’s for “minimal computational overhead“. Steering can STILL HAVE side effects. It just hasn’t been documented well yet (though if we find it has few side effects, feature steering still has advantages of being more precise). 
    
- Advantages of steering by features
    
    1) May succeed with previous approaches of behavior modification that didn’t work 
    
    [https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector)
    
    “The main takeaway is that this technique often works really well, but definitely not always.”
    
    “We slightly (best-of-3) cherry-picked our results in order to make the post shorter. Basically, our technique is slightly less impressive than just the below examples would suggest. “
    
    2) Only alters features of interest, possibly reducing side effects from modifying features not of interest (when using varied prompt pairs)
    
    - table 1
        
        ![Untitled](Brainstorm-%20extend%20sv%20to%20eqv%20classes%20e8e8d62ec04a43e78d6df5b52ab6020d/Untitled.png)
        
    
    ![Untitled](Brainstorm-%20extend%20sv%20to%20eqv%20classes%20e8e8d62ec04a43e78d6df5b52ab6020d/Untitled%201.png)
    

- make dataset classes and sub-classes for concepts and behavior
    - use contrastive samples
    - look for similar behaviors you expect can use same steering vector
        - country→capital were “analogous”, and so were (i)→(i+1) for numbers and months
        - a steering vector ALREADY is the abstraction across analogous domains
            - just like king-queen and male-female
            - but which domains?
            - But this abstraction often is not precise enough or doesn’t work
                - Previous papers show many steering vectors not working
                - Current steering vectors use sample diffs, not features
                - successor heads paper didn’t just use diffs, but a specific feature
                    - what if we were to do this for behaviors?
            - Perhaps find steering vectors not just from contrastive samples
            - 
- Examples of cross-domain analogous behavior
    
    Depending on how one defines the scope of a domain, the aim of steering vectors is to transfer an “opposites” analogous behavior **within** a “domain”
    
    Eg)
    
    Source: Marvin is sad -> Marvin is happy
    
    S Vec: [person] is sad -> [person] is -(sad)
    
    Target: Hector is sad -> Hector is happy
    
    <<<
    
    In this paper, we want to extend this behavior change not just to opposites
    
    Eg)
    
    Source: The Tortoise Won - The Hare lost
    
    S Vec: [diligent being] Won -> [lazy being] Lost
    
- study side-effects
    
    Opposites works well to remove behavior in a “broad sense”
    
    Fall of ROME paper - side effects?
    
    We want to study side effects of existing techniques
    
    Then, perhaps editing by features has less side effects as it’s more precise
    
- paper titles cands
    
    Steering Cross-Task Model Behaviors via Analogous Features
    
    Improving Steering Vectors by Reducing Adverse Effects via Feature Steering
    
    Reducing Adverse Effects of Steering Vectors via Feature Steering
    
    Improving on the Precision of Steering Vectors via Feature Steering
    
    Analyzing Relations Across Features for Model Steering
    
    Improving Model Steering via Feature Relationship Analysis
    
    Explaining the Effectiveness of Model Steering via Feature Interpretability
    

---

Cited by:

CAA

[https://scholar.google.com/scholar?oi=bibs&hl=en&cites=12785422939412301773&as_sdt=5](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=12785422939412301773&as_sdt=5)

ACt Add

[https://scholar.google.com/scholar?cites=267574229948165259&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=267574229948165259&as_sdt=5,31&sciodt=0,31&hl=en)

codebooks

[https://scholar.google.com/scholar?cites=9460788710261450578&as_sdt=5,31&sciodt=0,31&hl=en](https://scholar.google.com/scholar?cites=9460788710261450578&as_sdt=5,31&sciodt=0,31&hl=en)

---

$\frac{\sum_{F_P,F_N \in D}{(F_P - F_N)}}{|D|}$

$\frac{\sum_{P}{F_P} - \sum_{N}{F_N}}{|D|}$

$\frac{\sum_{F_1 \in D_1}{F_1}}{|D_1|} - \frac{\sum_{F_2 \in D_2}{F_2}}{|D_2|}$