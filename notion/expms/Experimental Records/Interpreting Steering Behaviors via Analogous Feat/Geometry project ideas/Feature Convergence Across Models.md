# Feature Convergence Across Models

As increase sae size do they converge? Do features split and still map together? Compare all to supervised features as a hub?

Composition is related to features splitting. Does that converge to simplicial structure?

Do features disappear? Merged?

---

comparing saes across models. I think your project is about finding better sae features for a model using a method you call alignment regularization; it's not directly related to what I'm thinking of, but I think you have some useful insights into how saes can better learn true features. Given that you have experience comparing saes I think I may have several questions to ask later if you have time in a few weeks. I'm running prelim geom experiments now so it'd be easier to explain once I finish them

And by comparing sae features across models I mean a continuation of this: [https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality](https://transformer-circuits.pub/2023/monosemantic-features#phenomenology-universality)

To phrase it better, I was thinking about how your method would approximate the true features better in one LLM. For two LLMs that are initialized differently, the saes trained on each of them for a layer would likely not find many analogous features. But if you train better saes, say with your method using the aggregates of multiple saes, I was wondering how much they would "converge' to find universally similar features, esp when features splitting occurs as saes get bigger. Similar to the platonic rep hypothesis. Do you think they would converge?

Hypothesis: They won’t be exactly the same, but there will probably be subsets of them that are very similar, and we can find which ones are similar.