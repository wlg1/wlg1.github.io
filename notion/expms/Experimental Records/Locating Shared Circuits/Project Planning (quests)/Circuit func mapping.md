# Circuit func mapping

- even if components are different, check if they can be mapped to one another in structure preserving way; see if they have similar features (cosine) or functionality (attn heads, relational patterns, etc). There has to be SOME similarity.
- If not, check if backups similar to 1234 circuits occur if ablate main heads of 2468 circ. Run 2468 prompts on 1234 circuits (rest are ablated).
    - Iteratively ablate by a path, breadth then depth
- instead of plotting circuits based on high 80% performance level, plot only most essential components based on lower threshold (eg. 50% drop if not all used together)
- Find classes of circuit types. Dispersed, concentrated.