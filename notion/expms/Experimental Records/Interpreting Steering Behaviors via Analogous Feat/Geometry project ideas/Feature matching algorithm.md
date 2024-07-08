# Feature matching algorithm

- how to identify similar features across models: we can’t just use similarity metric. we need to map them to each other! this require a search/matching algorithm.
    - try for 2 different toy models initialized in different ways
        - the issue with two different models is what layers match with what layers? do we try different combos? how did ph paper decide this?
        - also, small models may not have aligned representations. they need to get bigger. so study their mapping as we make them bigger. study big models.
    - we’re not mapping circuits, we’re mapping features based on relational similarity
    - this shows that the feature clusters in one model are similar to feature clusters to another model
    - measure structural match score
        - chatgpt to review information theory and KL div based on distance
            - use kernel similarity metric for matching
            - forbus
        - “chains” of similar features
        - labels are given by neuronpedia? or activation value?
        

Bottom up clusters matching small features, then merge them. possible uncertainties with wrong matches

To filter better starting points, Automate testing labels based on activation input similarity on same dataset. This gives you starting pairs. Refine these pairs using matching algorithm 

We don't need to find all marches, though we can and rank them

Issue: how can we test it IS a match? Steering? To show have same effect? What if not same effect?

Don't need matching algo if don't care about feature relns. But feature relns are useful bc shows models are aligned.  But only aligned if pairs are truly paired. If we only guess they're a pair and get high score what does that tell us?