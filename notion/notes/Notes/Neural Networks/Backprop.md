# Backprop

[https://cs231n.github.io/optimization-2/](https://cs231n.github.io/optimization-2/)

Every gate in a circuit diagram gets some inputs and can right away compute two things: 1. its output value and 2. the *local* gradient of its output

Backpropagation can thus be thought of as gates communicating to each other (through the gradient signal) whether they want their outputs to increase or decrease (and how strongly), so as to make the final output value higher.

### Chain Rule

the eqn for chain rule is simple, but the proof is not as simple as just introducing num/denom terms and rearranging, b/c the dash in the deriv is NOT division, and it must account for when g(x) approaches g(a) in the limit.

the idea is similar, but b/c the dash in deriv is not division, then traditional division rules can't be applied to it. instead, go around and look at what deriv represents, which uses division as a term (but with limit). then can apply division rules there.