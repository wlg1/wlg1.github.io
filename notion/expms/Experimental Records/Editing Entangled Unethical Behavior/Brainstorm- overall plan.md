# Brainstorm- overall plan

Ideas to try: (talk to collaborators about them)

- Find abstract features entangled with behavior and edit them
    - Chains of editing from feature to feature
    - Abstract to specific editing: animal to lion
    - Feature to feature (concept): lion to danger (ripple effects)
    - Feature to behavior: danger to acting safe
    - If we remove concepts that indicate danger, what impact does that have on behavior?
- Measure disentanglement of fine-tuning vs editing features to alter behavior
- Define features not as analogous, but as linear combinations
- Find what subsets of features are tied to (causal, correlate with) a behavior.
    - Can we use these features to predict behavior?
    - How were these tied by training?
    - We define hierarchical, abstract groups of features tied to behaviors (don't do this as vectors, rely on expm correlation scores). Feature groups across models
- OPTIONAL: find circuits entangled with features (b/c circuits are harder to prove than features or components)

- Analogous systems that are very different but share “not obvious” patterns
    
    Eg) A man failing vs glass breaking: both trigger “danger” analogously by a mapping
    
    the glass is the man
    
    falling is breaking
    
    - What is the shared representation of these analogies? Locate this in the model.
        
        LLMs do this by relational, vision only finds similar by visual. So LLM better?
        
    - This allows LLM to recognize ethical situations based on analogies.
        
        Editing the abstraction activations changes ethical reasoning and decisions
        
    - Does the model “label” the man and the glass as the same? do they have similar measures when projected onto the labeling vector?

---

Out of scope: (use this for second paper)

- Analogous mappings of vectors in latent space using structure-preserving maps
- Abstract to specific based on analogous mapping definition
- Mappings features between Text-to-Vision models
- Predictive Coding of analogous abstract forms to recognize specific inputs