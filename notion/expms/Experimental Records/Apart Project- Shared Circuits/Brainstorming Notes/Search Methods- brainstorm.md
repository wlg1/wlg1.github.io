# Search Methods- brainstorm

Can also train a model (DRL?) to choose the best next edge in the circuit based on previous cases, to beat greedy? How can the greedy method be used in this case? 

---

[https://chat.openai.com/c/32d62fc6-7b14-4d53-966e-8602ccb5520d](https://chat.openai.com/c/32d62fc6-7b14-4d53-966e-8602ccb5520d)

transformer and self attn are dags

Work backwards:

1. Start with full circuit. From the last layer, remove one head at a time and see how much performance falls. If performance falls <1% (or some threshold T), allow the removal. 
    1. We work backwards because components at the end don’t depend on components upstream, as the model is a DAG. If we worked from first to last layer, then removing a first layer node means destroying many paths that depend on it. Whereas working backwards means the nodes at the end have less dependence.
2. Continue backwards to the previous layer. Stop once reach first layer.

- latex draft
    
    \hl{Describe mean ablation above this. Then, we start with a simple search approach, and refine its issues/weaknesses later.}
    
    We use a simple search method that remove one component at a time and checks how much performance falls. If performance falls <T\%, where T is a user-defined threshold, we allow the removal and continue.
    
    When transformer models, including GPT-style models, are modeled as graphs with each node being a component (attention head, MLP, or residual stream layer), they are directed and contain no cycles, and are Directed Acyclic Graphs (DAGs). This means components at later layers will not affect nodes are previous layers. Thus, our search approach works backwards from the last layer to the first layer. It removes one component at a time in a layer, and once it finishes with a layer, it moves on to the previous layer, and stops once it finishes with the first layer.
    
    One potential weakness with this approach is that a model also processes tokens in parallel, in which the self-attention mechanism allows for each token to attend to all other previous tokens in the sequence. The self-attention mechanism still allows the transformer to be modeled as a DAG; however, ~~given there are edges between attention heads for each token position,~~
    
    The self-attention mechanism still allows the transformer to be modeled as a DAG as each head is operated on independently and in parallel; however, there may be a certain order in which removing
    

[https://colab.research.google.com/drive/1H6Rx_g6yaZOkrP30MT55AB2fA-6PY1tq](https://colab.research.google.com/drive/1H6Rx_g6yaZOkrP30MT55AB2fA-6PY1tq)