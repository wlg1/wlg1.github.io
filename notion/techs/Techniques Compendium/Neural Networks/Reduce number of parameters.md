# Reduce number of parameters

SOLN:

Enforce [Low Rank](https://www.notion.so/Low-Rank-80625e8314d84dadb475196257ea6009?pvs=21) constraints so it can be represented as low-rank

<<<

SOLN DET:

Given matrix with (m * n) elements (parameters), represent it as a product of two lower-dimensional matrices:

(m * n) —> (m * k) and (k * n)

Then calculate (m * k) + (k * n)

= (mk + kn)

= (m + n) * k

Many less parameters if k is much smaller than min(m, n)