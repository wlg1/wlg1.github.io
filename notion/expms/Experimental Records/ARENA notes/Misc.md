# Misc

Use chatgpt in VScode instead of web browser; browser takes up a lot of memory and heats up computer

dan hendrycks: unsolved problems in LLM AI Safety

hydra effect: ablate neurons, later neurons will activate strongly to repair these

[https://arxiv.org/pdf/2307.15771.pdf](https://arxiv.org/pdf/2307.15771.pdf)

name movers in diff models (real time): [https://www.youtube.com/@neelnanda2469/videos](https://www.youtube.com/@neelnanda2469/videos)

Neel also gave a talk on this at EA Global SF '22 if you want a video format: [https://youtu.be/edoQ3CiNa_s?si=5ElQg-Gv2jQEcEHe](https://youtu.be/edoQ3CiNa_s?si=5ElQg-Gv2jQEcEHe)

copy suppression in self repair: attend back to where word appeared in context to suppress it. If ablate component taht did orig pred, since model can reduce extreme predictions, these mechanisms just kick in less (?)

[https://www.lesswrong.com/posts/43C3igfmMrE9Qoyfe/scaffolded-llms-as-natural-language-computers](https://www.lesswrong.com/posts/43C3igfmMrE9Qoyfe/scaffolded-llms-as-natural-language-computers)

chain together using wrappers

attribution patching over ACDC since it has computational efficiecny; ACDC is more thorough. attribution patching approx gradients (change in model outputs) by asssuming it’s a first order function (get its gradient)- get all tehse grads in a single backwards pass.

softmax grad won’t say much?

ACDC finds which components are impt; alternate is start with all ablated (corrupted) and sel add back in. Second is hard to do bc many components are work together with each other. If that one component is impt then good, but hard bc many combos 

combine ACDC with approach with second approach