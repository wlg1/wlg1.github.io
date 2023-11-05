# Brainstorm- proj start

Questions to answer

- How to efficiently test which combinations of neurons (and attention heads) work together in a circuit to identify a feature or to perform a task?
    
    Ideas to tackle:
    
    - Ablate multiple at the same time, choosing another based on a bottom-up greedy algorithm

[SUB-ISSUE: How to define “analogous tasks”?](Brainstorm-%20proj%20start%207f2162094b5d412187f4af9137210dc7/SUB-ISSUE%20How%20to%20define%20%E2%80%9Canalogous%20tasks%E2%80%9D%20333b7aa1455848748dab3f768b8dfb55.md)

- How to find shared circuits for “analogous tasks”?
    
    Reasoning:
    
    - We can find shared components by conducting Direct Logit Attribution (Causal Tracing) and Attention Pattern Analysis on each task type, then seeing if the tasks share the same top important components (which restore most of the correct token’s logit)
    - We can measure shared similarity via Cosine similarity (projection) or “Congruence with component’s weights” (see: An Neuron)
    
    Issues:
    
    - How do we find shared INTERACTIONS between components? That is, the output of component h influences the output of component R
    
    Ideas to tackle and their issues:
    
    - Use Path Patching to reduce chances that other intermediate mediators affect the interaction of components h → R

Other Questions

- Dot product between similar concepts should be high. At what point in training or layers during inference does this happen?

---

Techniques

Superposition of analogous concepts

- use SVD to find impt correlation directions
    - ref Callumn blog
- Get a couple of places that use Eigenvector analysis (math framework)

Circuits

- copy scores

MLPs

- neuron2graph

Model editing

training dynamics starting from toy models

- Ablate combo of attn heads and mlp neurons
    
    Ablate combo of attn heads and mlp neurons
    
    Combines ioi and an neuron
    
    The number seq algo
    
    A scale of relatedness based on cosine sim
    
    Is it +1 or a scale?
    
    Greedy search combos of neurons. Find most impt, then find next impt that fire with it, etc. Ablaze these combos
    
    Choose from cands
    
    Top down vs bot up- ablaze all, then narrow
    Ablate each
    
    Find project ideas by looking at limitations in paper conclusion
    
    Another idea I have is do nn use reusable analgoies? If a pattern up and down circuit is same as for another, is it reused? Perhaps more efficient during training.
    

Next steps:

- Causal scrubbing

---

[https://chat.openai.com/c/f1c98c41-a9c7-45c1-afa1-312d932a562a](https://chat.openai.com/c/f1c98c41-a9c7-45c1-afa1-312d932a562a)

---

Hypotheses: 

---

- Do workshops have a different deadline than the main conference?
    
    Yes, workshops typically have different deadlines than the main conference. Workshops are usually smaller events that are co-located with a larger main conference. They may focus on a specific topic or subfield and provide a forum for specialized discussions and presentations.
    
    Here are some key differences in deadlines between workshops and the main conference:
    
    1. **Submission Deadline:** Workshops often have their own call for papers (CFP) with submission deadlines that may be either before, after, or even parallel to the deadlines for the main conference.
    2. **Notification Date:** Similarly, the date by which authors are notified of acceptance or rejection for workshops is usually different from the notification date for the main conference.
    3. **Camera-Ready Deadline:** Workshops have their own camera-ready deadlines for accepted papers, which again may differ from those for the main conference.
    4. **Registration:** Workshops may also have separate registration deadlines or processes, though registration for the main conference often includes the option to register for co-located workshops.
    5. **Event Date:** Workshops are often held just before or just after the main conference, though sometimes they occur in parallel.
    
    Always consult the specific conference and workshop websites for the most accurate and up-to-date information, as the above points can vary.