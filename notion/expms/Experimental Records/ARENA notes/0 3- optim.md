# 0.3- optim

[**Exponentially Weighted Averages**](https://www.youtube.com/watch?v=lAq96T8FkTw&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=17&t=119s&ab_channel=DeepLearningAI)

[https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d](https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d)

![Untitled](0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854/Untitled.png)

Blue data S is noisy, so obtain a moving average (or momentum) equation (in yellow) as follows:

![Untitled](0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854/Untitled%201.png)

Each new point $V_t$ is a weighted sum of the previous point with the current point $S_t$

Higher values of beta mean smoother curves because it averages over more prev data pts (a data pt  $S_i$ is “removed” from contribution to $V_t$ when it becomes too small due to small coefficients). Higher beta gives more weight to $V_{t-1}$. The decay in weight for older data points is slower as the older pts’ values are kept more in each iteration of $V_i$. 

However, the curve is not as close to the original data as it uses more “other” data (the prev data pts) as it gives less weight to the actual data point $S_t$. It adapts slower to the new, actual data pts.

<<<

Takeaways

G- To get a smoother curve, take the moving average with previous data points and the current one

G- To get moving average $V_t$ with prev pts, take the previous iteration of the moving avg, $V_{t-1}$

---

[**Understanding Exponentially Weighted Averages (C2W2L04)**](https://www.youtube.com/watch?v=k8fTYJPd3_I&ab_channel=DeepLearningAI)

Expand recursive EWMA in terms of S

![Untitled](0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854/Untitled%202.png)

Each S term, in the next V term, decays by an exponential amount each new V

Beta is constant, but since it’s raised to a power for each S, each S’s contribution decreases exponentially for each new V.

So exponential refers to how each $V_t$ changes from prev $V_{t-1}$; it does not refer to how different beta values change how smooth the overall V curve is.

Code: We don’t need to keep every previous value, just the last one

---

[https://www.youtube.com/watch?v=k8fTYJPd3_I&ab_channel=DeepLearningAI](https://www.youtube.com/watch?v=k8fTYJPd3_I&ab_channel=DeepLearningAI)

![Untitled](0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854/Untitled%203.png)

If the target optimum along axis W is CLOSE to where the NN weights’ state currently is on axis W, you want **slower** learning so it doesn’t it stray too far

If the target optimum along axis W is FAR to where the NN weights’ state currently is on axis W, you want **FASTER** learning so it gets closer to the target

Similar to the EWMA of data pts, we can use an EWMA for each step in gradient descent to smooth its trajectory (**stabilize)**. The averages will make the trajectory oscillate less when it oscillates a lot in one axis, but if it doesn’t oscillate a lot in another axis, it won’t reduce this oscillation by a lot (**speed up)**. 

![Untitled](0%203-%20optim%207d8f58449c1f42fa93bf1459469ef854/Untitled%204.png)

Velocity is the direction (and speed, the magnitude of the velocity vector) you’re currently on, so it uses previous points. Acceleration is how the direction changes at the current point, so it adds on to the current velocity. The acceleration is the change in velocity $V$ (how $V_t$ changes from $V_{t-1}$)

- is EWMA the same as momentum, or is the term momentum just used when applying EWMA to gradient descent?
    
    "Momentum" refers specifically to the application of EWMA-like averaging of gradients to enhance the gradient descent process. EWMA itself is a broader statistical technique used for smoothing data in various applications. So $V$ is momentum only when using gradients for GD.
    

Usually beta =0.9 works well

<<<
Takeaways:

- G- use momentum to both stabilize and speed up GD convergence

---

SGD is noisy because one sample may not have the right direction, but over time (in avg, or expectation), the trajectory should have the right direction. So locally it may not, but globally it should.