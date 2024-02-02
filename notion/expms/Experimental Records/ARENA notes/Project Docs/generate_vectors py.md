# generate_vectors.py

Expl tests:

[https://colab.research.google.com/drive/1Qy_QsOh5RKcjguU1Ar6Zq6cMEoOq56j4](https://colab.research.google.com/drive/1Qy_QsOh5RKcjguU1Ar6Zq6cMEoOq56j4)

GOAL: Average the activations of both positive and negative examples

Compare the shapes of activation tensors you get from original code with the shapes you get from nnsight saving code. Make sure they’re the same.

- why p_activations[0, -2, :]
    - The first index `0` refers to the first element in the batch dimension
    - The second index `2` is selecting the second-to-last element in the sequence dimension. In the context of language models, this could be the activations corresponding to the second-to-last token in the input sequence. The reason for choosing the second-to-last token could be specific to the model's architecture or the particular task it's being used for. For instance, if the last token is always a special token (like an end-of-sequence token), then the second-to-last token might represent the actual last piece of meaningful input data.
    - The colon `:` is used to select all elements along the feature dimension (`d_model`). This means it's taking all the features (or neurons) of that particular token in
    
- stack vs vstack
    
    The difference between `stack` and `vstack` functions in Python, particularly in the context of NumPy or similar libraries, lies in how they combine arrays:
    
    1. **`stack`**:
        - The `stack` function combines a sequence of arrays along a new axis. This new axis is created for the stacking process.
        - The arrays that you stack must have the same shape.
        - You can specify the axis along which stacking is to be done using the `axis` parameter. For example, if you have two 2D arrays and you use `stack` with `axis=0`, you will get a 3D array where these two arrays are stacked along a new first axis.
    2. **`vstack`** (Vertical Stack):
        - The `vstack` function stacks arrays vertically, i.e., along the first axis (rows).
        - This method is essentially a concatenation along the first axis for 2D arrays. However, for 1D arrays, it behaves like adding a new row, effectively transforming them into a 2D array.
        - Unlike `stack`, `vstack` does not increase the dimensionality of the output array. For example, vertically stacking two 2D arrays will result in a larger 2D array, not a 3D array.
    
    In summary, while `stack` introduces a new axis for stacking and can increase the dimensionality of the array, `vstack` stacks arrays along the existing vertical axis (rows) and does not increase the dimensionality. The choice between them depends on how you want your arrays to be combined.
    
- is stack(dim=1) the same as vstack?
    
    In Python, particularly when working with NumPy or similar libraries, `stack` and `vstack` are functions used to combine arrays, but they work in slightly different ways.
    
    1. **`stack(dim=1)`**: The `stack` function stacks arrays along a new axis. The `dim` parameter (or `axis` in NumPy) specifies the index of the new axis in the array dimensions. When you use `stack(dim=1)`, it means you are stacking the arrays along the second axis (since indexing starts from 0). This will increase the dimensionality of the array. For instance, if you stack two 2D arrays (matrices) using `stack(dim=1)`, the result will be a 3D array.
    2. **`vstack`**: On the other hand, `vstack` (vertical stack) is used to stack arrays vertically, i.e., along the first axis (rows). It is equivalent to concatenation along the first axis after 1-D arrays of shape `(N,)` have been reshaped to `(1,N)`. `vstack` does not increase the dimensionality of the array; it just stacks the arrays on top of each other. For example, vertically stacking two 2D arrays will result in a larger 2D array.
    
    In summary, `stack(dim=1)` and `vstack` are not the same. `stack(dim=1)` stacks arrays along a new second axis, increasing the dimensionality, while `vstack` stacks arrays vertically along the existing first axis (rows), without increasing the dimensionality.