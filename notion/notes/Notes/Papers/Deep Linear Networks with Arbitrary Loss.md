# Deep Linear Networks with Arbitrary Loss

![Untitled](Deep%20Linear%20Networks%20with%20Arbitrary%20Loss%2069a690ef79de42439bf37dd7c4cca223/Untitled.png)

- Why is this true?
    
    When the network has only one layer (i.e., $L = 1$), the loss function $\mathcal{L}(W_1)$ is convex with respect to the weights $W_1$. 
    
    - why is the function convex when only 1 layer?
        1. **Linear Operations**: With a single layer, the network performs a linear transformation on the input data. A linear transformation is a mapping $\mathbf{y} = W\mathbf{x}$ that preserves vector addition and scalar multiplication. This means that the transformation of a weighted sum of vectors equals the weighted sum of the transformed vectors, which is a convex operation.
        2. **Convex Loss Functions**: Common loss functions used in machine learning, such as mean squared error or cross-entropy loss, are convex with respect to the network's parameters. This convexity is maintained when the parameters are linearly related to the output.
        3. **Combination of Linear Transformation and Convex Loss**: When you apply a convex loss function to the output of a linear transformation, the result is still a convex function with respect to the weights. This is due to the fact that the composition of a convex function with a linear transformation preserves convexity.
        4. **Convexity of the Objective Function**: The convexity of the objective function (loss function) in a single-layer network means that any line segment drawn between any two points on the function will not pass below the function itself. This is the definition of a convex function, and it implies that there are no local minima that are not also global minima. Hence, the optimization problem is convex, and any solution to the problem will be globally optimal.
        
        For these reasons, in the simple case of a single-layer network with a convex loss function, the optimization landscape is convex, making it much simpler to find the global minimum.
        
    
    In the realm of convex optimization, a convex function over a convex set has the property that any local minimum is also a global minimum. This implies that if you find a point where the gradient (derivative) of the function is zero (a local minimum), this point is the best possible solution (global minimum) you can get; there are no other "valleys" in the function space.
    
    For convex loss functions, this property ensures that gradient descent methods can effectively find the global minimum because there are no other local minima that are not global. This is significant because it simplifies the optimization problem; you don't have to worry about getting stuck in a worse solution that is only locally optimal.
    
    However, when multiple layers are added to the network, this property does not necessarily hold anymore. The loss surface can become non-convex with multiple local minima, some of which may be suboptimal. This makes the optimization problem more challenging because gradient descent methods can potentially get stuck in these suboptimal points.
    

- explain theorem 2 intuitively
    
    For a deep linear network with more than one layer, when the loss function is convex but not differentiable, we lose the guarantee that every local minimum is also a global minimum. This is a contrast to the scenario where the loss function is differentiable, in which case the landscape has the much nicer property that every local minimum is global.
    
    In non-differentiable scenarios, there can exist points where the loss function has a "flat" region (not a sharp minimum), and the gradient does not provide a clear direction for descent. These flat regions can lead to sub-optimal local minima because gradient-based optimization methods rely on the gradient to point towards the minimum, which doesn't happen if the gradient is zero (or undefined) in a flat region.
    
    The theorem illustrates this concept by showing that if the loss function is not smooth (i.e., it has points of non-differentiability), then there can be local minima that are not the absolute best solutions you can get, meaning they are sub-optimal. This is important because in practical terms it means that for certain loss functions, just finding a point where the gradient is zero is not enough to ensure that you've found the best possible model parameters during training. It indicates that extra care must be taken when designing optimization algorithms for these kinds of problems.