# Failures

### GPT-3.5

- Claiming vector norm isn’t always representing distance
    
    Do vector norms always represent a dsitance
    
    <
    
    Vector norms do not always represent a distance.
    
    A vector norm is a mathematical function that assigns a non-negative scalar value to a vector, typically representing the "size" or "magnitude" of the vector.
    
    While in some cases, vector norms may represent a distance, such as the Euclidean norm, which is commonly used to measure the distance between two points in a 2D or 3D space, other vector norms may not have a direct interpretation as a distance.
    
    For example, the L1 norm (also known as the Manhattan norm or taxicab norm) is often used in image processing and computer vision, but it does not correspond to a Euclidean distance. Additionally, the Frobenius norm, commonly used to measure the "size" of a matrix, also does not have a direct interpretation as a distance.
    
    ---
    
    Contradicts:
    
    [https://en.wikipedia.org/wiki/Norm_(mathematics)](https://en.wikipedia.org/wiki/Norm_(mathematics))
    
    [https://math.stackexchange.com/questions/172028/difference-between-norm-and-distance](https://math.stackexchange.com/questions/172028/difference-between-norm-and-distance)
    
    > All norms can be used to create a distance function
    > 
- Wrong attention mask example
    
    Here's an example of what the **`inputs`** dictionary and attention mask tensor might look like for a batch of two input sequences, where the first sequence has length 4 and the second sequence has length 3:
    
    ```
    inputs = {
        'input_ids': tensor([[101, 2054, 2131, 2003, 102],
                             [101, 1996, 7922, 102,   0]]),
        'attention_mask': tensor([[1, 1, 1, 1, 1],
                                  [1, 1, 1, 0, 0]])
    }
    ```
    
    Here, the **`inputs`** dictionary contains two keys: **`'input_ids'`**, which is a tensor of shape **`(2, 5)`** containing the token IDs of the input sequences (where **`101`** corresponds to the **`[CLS]`** token and **`102`** corresponds to the **`[SEP]`** token), and **`'attention_mask'`**, which is a tensor of shape **`(2, 5)`** containing the attention mask for each input sequence (with a value of **`1`** for non-padding tokens and a value of **`0`** for padding tokens).
    
    In the first input sequence (**`inputs['input_ids'][0]`**), there are no padding tokens, so the attention mask is all ones (**`inputs['attention_mask'][0]`** is equal to **`[1, 1, 1, 1, 1]`**). In the second input sequence (**`inputs['input_ids'][1]`**), there are two padding tokens at the end, so the last two values of the attention mask are zero (**`inputs['attention_mask'][1]`** is equal to **`[1, 1, 1, 0, 0]`**).
    

### GPT-4

- Claiming MLP and key-values have no relation
    
    [https://www.notion.so/Transformer-Feed-Forward-Layers-Are-Key-Value-Memories-0a97101d5550430d8ef5e0a4c8016253?pvs=4#838db617c2c3420e94640e6651cfc861](../Papers%203fa55c25c0194ccd89e95feefb9e16bc/Transformer%20Interpretability%201592ca5b054c4b76a9f4ace09d1bf8ba/Transformer%20Feed-Forward%20Layers%20Are%20Key-Value%20Memo%200a97101d5550430d8ef5e0a4c8016253.md)
    
    ![Untitled](Failures%20a0e9fb20cd944c758b975221e7976553/Untitled.png)
    
- It contradicts itself if you claim it’s wrong, so you don’t know what the answer actually is
    
    Why does taking the transpose work to reduce computational cost or reduce instability?
    
    Taking the transpose of a matrix can sometimes help reduce the computational cost or improve the numerical stability of a matrix equation, depending on the specific problem at hand.
    
    One reason why taking the transpose can help reduce computational cost is that it can allow us to use a more efficient algorithm or data structure for solving the equation. For example, if the original matrix equation is Ax = b and we have a more efficient algorithm or data structure for solving the equation A^T y = c, we can use this alternative equation instead. This is because the transpose of a matrix has the same eigenvalues as the original matrix, so solving the transpose equation can give us the same solution as solving the original equation.
    
    Another reason why taking the transpose can help improve numerical stability is that it can sometimes reduce the condition number of the matrix. For example, if we have an ill-conditioned matrix A, solving the normal equation A^T A x = A^T b can sometimes give us a more stable solution than directly solving the original equation Ax = b. This is because the condition number of A^T A is the square of the condition number of A, so if the condition number of A is large, the condition number of A^T A may be smaller and lead to better numerical stability.
    
    However, it is important to note that taking the transpose does not always help reduce computational cost or improve numerical stability. It depends on the specific problem at hand and the properties of the matrix involved. Therefore, it is important to carefully analyze the problem and choose the most appropriate approach for solving it.
    
    If condition number of A^T A is the square of the condition number of A, wouldn't it be bigger? Like 2^2 = 4
    
    You are correct. If A is an ill-conditioned matrix, then its condition number is typically a large number, say k. In this case, the condition number of A^T A would be k^2, which is an even larger number. This means that solving the normal equation A^T A x = A^T b may actually lead to worse numerical stability than directly solving the original equation Ax = b.
    
    Therefore, while solving the normal equation can sometimes help reduce the computational cost or improve the numerical stability of a matrix equation, it is not always the best approach. It is important to carefully analyze the properties of the matrix involved and choose the most appropriate approach for solving the problem. In some cases, it may be better to use other techniques such as regularization or iterative methods to solve the equation.
    

[data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2730%27%20height=%2730%27/%3e)