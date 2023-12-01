# Matrix row vectors

if dot product measures how much v is on r (row vector), then it uses r as "1 unit", not the scaled version of r down to its basis?
[2 1] = r
[2 1] * [1 4] = 6

[0.4 0.2] = b
[0.4 0.2] * [1 4] = 0.4 + 0.8 = 1.2 = 6/5

Is [1 4] 6 units or 1.2 units in the target space?
it's 6 units

[0.4 0.2] * [2 1] = 1
[0.4 0.2] is 1 unit

[2 1] * [2 1] = 5
[2 1] is 5 units

Thus, there is NO issue. The row vector is NOT 1 unit; so it's wrong to say r is "1 unit". r merely states the feature direction that is mapped to. r ITSELF can be 5 units