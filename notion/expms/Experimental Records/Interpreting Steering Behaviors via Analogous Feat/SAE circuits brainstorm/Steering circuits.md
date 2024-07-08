# Steering circuits

find circuit for function vector

is it solving higher lvl task

ablate and scale pre-existing gpt-2 small circuits from marks

to choose threshold, relative effect: how steering changes circuit relative to non-steering

error terms of saes to circuits. if run model without this, not accurate. 

---

[https://www.alignmentforum.org/posts/zj3GKWAnhPgTARByB/saes-discover-meaningful-features-in-the-ioi-task](https://www.alignmentforum.org/posts/zj3GKWAnhPgTARByB/saes-discover-meaningful-features-in-the-ioi-task)

[https://arxiv.org/pdf/2405.08366](https://arxiv.org/pdf/2405.08366)

[https://openreview.net/pdf?id=JdrVuEQih5](https://openreview.net/pdf?id=JdrVuEQih5)

A Systematic Comparison of Sparse Autoencoder Variants for Model Steering on the IOI Task

Task-specific SAEs vs s. Full-distribution SAEs

“SAEs trained on either the IOI dataset (task-specific SAEs) or the LLM’s pre-training dataset (fulldistribution SAEs)”

“task-specific SAEs allow us to edit attributes by changing fewer features compared to full-distribution SAEs.”

why find circuit instead of just using steering vectors?

because steering circuit is “better”?

“(2) the features can be used to edit capability-relevant information in internal model representations”

so you first need supervised dictionaries? so circuits act as supervision?

[https://arxiv.org/pdf/2405.08366](https://arxiv.org/pdf/2405.08366)

aim of original paper: 

“we cannot directly evaluate the usefulness of features learned by an SAE, as we do
not know the hypothetical ‘true’ features to begin with”

- simple supervised methods can be used as a principled way to compute high-quality
feature dictionaries in a task-specific context;

• these dictionaries can be used as ‘skylines’ to evaluate and contextualize the performance of unsupervised methods, such as SAEs.

Makelov do steer at specific circuits cross section 

I see the authors do steer at the cross sections and mention in appendix expecting specific subject inhitibition steering when steering at subj inhi heads, was talking to someone in my lab who reproduced these results (to generalize them later). So looks like a promising approach so far!