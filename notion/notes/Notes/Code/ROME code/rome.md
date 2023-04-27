# /rome/

rome_main.py —> apply_rome_to_model()

—> execute_rome() —> compute_u(), compute_v()

---

- apply_rome_to_model():
    
    This takes in several (r, s, o) and applies execute_rome() to each of them 
    
    ```python
    request = [
        {
            "prompt": "{} in located in",
            "subject": "Disneyworld",
            "target_new": {"str": "France"},
        }
    ]
    ```
    
    ```python
    for i, request in enumerate(requests):
            deltas = execute_rome(model, tok, request, hparams)
    ```
    
- execute_rome():
    
    weights are changed, then stored
    
    Delta dictionary STORE the changes to each weight
    
    ```python
    weights[weight_name][...] += upd_matrix
    deltas[weight_name] = (
                    left_vector.detach(),
                    right_vector.detach(),
                )
    ```
    
    upd_matrix: the update matrix is a rank-1 matrix, which means that it has the lowest possible rank for a non-zero matrix. A rank-1 matrix can be expressed as the outer product of two vectors, which are commonly referred to as the left and right singular vectors of the matrix. These vectors represent the directions in which the matrix has the most influence.
    
    - Why outer product?
        
        [Outer Product](../../Math%2089624985ddb64f0c91c334b1ab5df1d0/Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Outer%20Product%2065f8a1a8e8fd45c4ac6e59d22afad162.md) 
        
        The outer product is used to construct the rank-1 update matrix because it generates a matrix that has the same dimensions as the weight tensor, and can be added to the weight tensor to modify it. The inner product is not suitable for this purpose because it generates a scalar value that cannot be used to directly modify the weight tensor.
        
    
    Each u and v vector used to construct the rank-1 update matrix is a vector of rank 1.
    
    [REF](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/732789d4b5c1247ccab5faf13b6f29d2_MIT18_06SCF11_Ses1.11sum.pdf)
    
    ![Untitled](rome%204d51c63203334d548af5595c8a8cff1d/Untitled.png)
    
    ![Untitled](rome%204d51c63203334d548af5595c8a8cff1d/Untitled%201.png)
    
    - More on rank-1
        
        [https://byjus.com/question-answer/what-is-a-rank-1-matrix/](https://byjus.com/question-answer/what-is-a-rank-1-matrix/)
        
        The matrix has rank 1 if each of its columns is a multiple of the first column.
        
    
    The **`u`** vector is computed by minimizing:
    
    (model's output for the original prompt) - (its output for the modified prompt)
    
    the **`v`** vector is computed by minimizing
    
    (**`u`**-modified model output for the modified prompt) - (its output for the original prompt)
    
    ```python
    weight_name = f"{hparams.rewrite_module_tmp.format(layer)}.weight"
    ```
    
    - Above code explained:
        
        [A string.](../../CS%20&%20SWE%20f7436b5aff924c04aa569007bb061038/Python%20f5fe14898d744a74819532b914123159.md) 
        
        ```python
        message = "Hello, my name is {} and I am {} years old".format(name, age)
        ```
        
        **`hparams.rewrite_module_tmp` is a string. It is a (format) string that contains {}**
        
        The **`hparams`** parameter contains hyperparameters for the ROME algorithm, including a format string **`rewrite_module_tmp`** that is used to construct the weight tensor name.
        
        The **`rewrite_module_tmp`** format string contains a placeholder **`{}`** that is used to insert the layer number. By calling **`hparams.rewrite_module_tmp.format(layer)`**, the format string is formatted with the layer number, resulting in a string that specifies the name of the weight tensor for the specified layer.
        
        Then .weight gets the name of the weight from this weight tensor (??)
        
        The weight tensor can be retrieved from the model using this string by calling **`nethook.get_parameter(model, weight_name)`**.
        
    
    ```python
    upd_matrix = left_vector.unsqueeze(1) @ right_vector.unsqueeze(0)
    ```
    
    When **`@`** is applied to two tensors, it performs matrix multiplication between the tensors.
    
    The **`unsqueeze()`** method is used to add a new dimension to each of the vectors
    
    **`left_vector.unsqueeze(1)`** adds a new dimension to **`left_vector`** at position 1, which results in a tensor of shape **`(batch_size, 1, vector_size)`**.
    
    **`right_vector.unsqueeze(0)`** adds a new dimension to **`right_vector`** at position 0, which results in a tensor of shape **`(1, vector_size, batch_size)`**.
    
    **`upd_matrix`** is of shape **`(batch_size, vector_size, vector_size)`**
    
- from .compute_u import compute_u
    
    compute_u.py:
    
    ```python
    inv_mom2_cache[key] = torch.inverse(
                stat.mom2.moment().to("cuda")
            ).float()  # Cast back to float32
    ```
    
    The **`inv_mom2_cache`** dictionary stores the inverse of the second moment of the gradients of the model with respect to the input. 
    
    The second moment of the gradients is a measure of the variance of the gradients with respect to the input. It is used in the ROME algorithm as a way to estimate the curvature of the loss surface around the current input.
    
    - Why second moment of the gradients is a measure of the variance of the gradients with respect to the input?
        
        The second moment of the gradients is a measure of the variance of the gradients with respect to the input because it calculates the average of the squared gradients with respect to the input.
        
        [Second Moment](../../Math%2089624985ddb64f0c91c334b1ab5df1d0/Probability%2055dc8908e9204acfbb1013eb383fb72b/Second%20Moment%205b9af19ee012427eb1dc5def31647ce8.md) 
        
        When the second moment of the gradients is high, it indicates that the gradients vary a lot with respect to the input, which suggests that the optimization problem may be difficult to solve. On the other hand, when the second moment of the gradients is low, it indicates that the gradients are more stable and that the optimization problem may be easier to solve.
        
        By using the inverse of the second moment of the gradients to scale the gradient in the direction of the modified prompt, the ROME algorithm ensures that the gradient is normalized by the variance of the gradients with respect to the input. This normalization helps to make the optimization problem more stable and easier to solve, because it ensures that the gradient is not too large or too small relative to the variance of the gradients.
        
    
    The inverse of the second moment is used to scale the gradient in the direction of the modified prompt. This scaling ensures that the **`u`** vector is orthogonal to the direction of the original prompt, and lies in the subspace spanned by the modified prompt.
    
    - Why the inverse of the second moment?
        
        The inverse of the second moment is used instead of the second moment itself because it provides a way to scale the gradient without changing its direction. When the second moment is used to scale the gradient, it can change the direction of the gradient, which can lead to incorrect updates and slower convergence.
        
        - Why doesn’t it change the direction?
            
            because it is a scalar value that is applied uniformly to all components of the gradient vector.
            
            - Why is the inverse a scalar value? Give a simple example
                
                it is calculated by taking the inverse of the average of the squared gradients with respect to the input. The squared gradients with respect to the input are summed across all dimensions to obtain a scalar value, and then this scalar value is divided by the total number of dimensions to obtain the average. Finally, the inverse of this average is taken to obtain the inverse of the second moment.
                
                To illustrate this with a simple example, consider a gradient vector **`g`** with 3 components. To calculate the second moment of this gradient vector, we first square each component of the gradient vector:
                
                - SIDE NOTE: How do we calculate its first moment?
                    
                    It’s just the average of all values, which is a scalar.
                    
                
                ```
                g = [1, 2, 3]
                g_squared = [1, 4, 9]
                ```
                
                Next, we sum these squared values to obtain a scalar value:
                
                ```
                sum_squared = 1 + 4 + 9 = 14
                ```
                
                This scalar value represents the total variance of the gradients with respect to the input. To obtain the average variance, we divide this scalar value by the total number of dimensions, which in this case is 3:
                
                ```
                avg_variance = sum_squared / 3 = 4.666...
                ```
                
                Finally, we take the inverse of this average variance to obtain the inverse of the second moment:
                
                ```
                inverse_second_moment = 1 / avg_variance = 0.214...
                
                ```
                
                This scalar value represents the factor by which the gradient vector should be scaled in the direction of the modified prompt to make the optimization problem more stable and easier to solve.
                
                - What is the formal definition of second moment and its inverse? use latex
                    
                    ![Untitled](rome%204d51c63203334d548af5595c8a8cff1d/Untitled%202.png)
                    
                - What is the formal definition of second moment of a gradient and its inverse?
                    
                    ![Untitled](rome%204d51c63203334d548af5595c8a8cff1d/Untitled%203.png)
                    
                
                IT CONTRADICTS ITSELF:
                
                - If the second moment is also a scalar, why doesn't it change direction?
                    
                    The second moment of the gradient with respect to the input is a scalar value, and it does not change the direction of the gradient when it is used to scale the gradient in the direction of the modified prompt.
                    
                    To understand why the direction of the gradient is not changed by the second moment, consider that the second moment is a scalar value that is used to scale the gradient vector uniformly across all its components. The direction of the gradient vector is determined by the relative magnitudes of its components, not by their absolute values.
                    
                    When the gradient is scaled using the second moment, the relative magnitudes of its components are preserved, and the direction of the gradient is not changed. This means that the gradient vector still points in the same direction as before, but its magnitude is adjusted to reflect the variance of the gradients with respect to the input.
                    
                    Therefore, the second moment of the gradient is a scalar value that does not change the direction of the gradient vector when it is used to scale the gradient in the direction of the modified prompt.
                    
                - But the second moment is a scalar, so it can't change the direction
                    
                    The reason why the inverse of the second moment is used instead of the second moment itself is that it provides a way to normalize the gradient vector without changing its magnitude. When the second moment is used to scale the gradient, it can change the magnitude of the gradient, which can affect the rate of convergence of the optimization algorithm.
                    
    - Why orthogonal to the original prompt?
        
        This modified subspace is orthogonal to the subspace spanned by the original prompt because the two prompts are different and do not lie in the same subspace.
        
    
    In the line of code you mentioned, **`torch.inverse()`** is called to compute the inverse of the second moment. This function calculates the matrix inverse of the second moment tensor using the LU decomposition method. The resulting inverse matrix is then cast back to the **`float32`** data type, which is the same data type used for the weights of the model.
    
    By storing the inverse of the second moment in the **`inv_mom2_cache`** dictionary, the ROME algorithm avoids recomputing this value for each update request, which can be computationally expensive. Instead, the inverse of the second moment is computed once and then cached for future use.