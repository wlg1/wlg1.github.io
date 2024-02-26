# Other groups capstones

Ising model: +- 1, output energy

Entropy tries to get logits as close as poss. But this makes energy bad. So balance

thm: botlzman sampling is equivalent to an otpimla RL play with fixed entropy

Instea of 1s, gen logits. 

PPO / TRPO

free energy is total entropy plus enegry of board state. over games, and avg. in limit, get 

mod this game to get stronger results (renormalization gives output of value fn, not just policy)

since this is slow, if this pseudocode works, it’d be exp better to give output of value fn

entropy of a policy and of board state. 

in more general, renorm is “almost” semi group. here it’s more combinatorial

---

mamba acts more like RNN. do its hidden states behave like res streams in transf?

get priv basis after adding relu

---

e attr patching: edge attr pass runs 2 fwd passes (clean and corr) instead of every E, and a backw pass on clean grads. linear approx between them approx the changes. acdc not good at detecting redundant circuits. issues: grads are 0s and 1s when passing in boolean inputs, so no signal gets all way thru. but can take both grads for each fwd pass, and look for passes where can pick which actv to use. this gets in linear time

pytorch cant calc full grads

partial corrupt E by some lambda between 0 and 1 (clean and corr). EAP lienarize around task performance (logit diff) on y-axis vs lambda x-axis graph. EAP fails in 2 quadratic failure cases.

---

Self rec mnjst

Keenan, mateusz cellular automata