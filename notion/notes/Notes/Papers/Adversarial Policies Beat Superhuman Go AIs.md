# Adversarial Policies Beat Superhuman Go AIs

AI can be beaten if you find its weaknesses. An AI trained on Go was beaten.
[https://twitter.com/farairesearch/status/1682078072064077824](https://twitter.com/farairesearch/status/1682078072064077824)
If you get the AI to make a circle shape, it thinks the shape is invulnerable and won’t defend it even though it can be killed.

[https://far.ai/publication/wang2022adversarial/](https://far.ai/publication/wang2022adversarial/)

helper systems:

it also poses significant problems when an AI system is tasked with [overseeing another AI system](https://far.ai/post/2023-03-safety-vulnerable-world/), such as a learned reward model being used to train a reinforcement learning policy, as the lack of robustness may cause the policy to capably pursue the wrong objective (so-called *[reward hacking](https://arxiv.org/abs/2209.13085)*).

The policy network is trained to match as closely as possible the distribution of moves output by MCTS, and the value network is trained to predict the [FINAL] outcome of games played by the agent.

policy network: intuition (feels like this move will lead to good future moves)

MCTS: simulation (actually see future plans up to an certain time step)

Since it is not practical for MCTS to exhaustively evaluate every possible sequence of play, the policy network is used to steer MCTS in the direction of better moves. Additionally, a *value network* is used to heuristically evaluate board states so that MCTS does not need to simulate all the way to the end of the game.

instead of playing against a copy of itself (so-called *self-play*), we pit the adversary against a static version of KataGo (which we dub *victim-play*).

In regular MCTS, moves are sampled from a single *policy network*. This works well in self-play, where both players are the same agent. But with victim-play, the adversary is playing against a potentially very different victim agent. We solve this by sampling from KataGo’s move distribution when it’s KataGo’s turn, and our policy network when it’s our turn.

Why can’t kataGo playing by itself find these adversarial policies? Perhaps it’s already ingrained them as assumptions, so you need a fresh new perspective to find them

patch pass attack and then this network finds cyclic attack

Even superhuman AI systems can be tripped up by a human if the human knows its weaknesses. Another way to put this is that *worst-case robustness* (the ability to avoid negative outcomes in worst-case scenarios) is lagging behind *average-case capabilities* (the ability to do very well in the typical situation a system is trained in).

Many proposed solutions to the alignment problem involve one “helper AI” providing a feedback signal steering the main AI system towards desirable behavior. Unfortunately, if the helper AI system is vulnerable to adversarial attack

---

[https://goattack.far.ai/](https://goattack.far.ai/)