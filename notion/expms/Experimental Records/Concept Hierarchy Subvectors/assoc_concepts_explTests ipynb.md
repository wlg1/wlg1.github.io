# assoc_concepts_explTests.ipynb

It DOES pick up meaningful signals, b/c that’s what model steering already does!

color vs red

Questions:

- resid_post_0_diffs has d_model (768) neurons. Given that the neurons are different, how can we say a component as a whole is significant for that concept, or different between the concepts (eg. being the one that distinguishes color from red)?
    - We can measure on a neuron level
    - We can use summary statistics (eg. sum, mean, Jaccard IOU)
    - We can compare this to a null (eg. color vs mean activations from any other token that aren’t specific colors)
- Of course all components would be different. What’s to say a component is “significantly” different?
- Try unembedding the differences