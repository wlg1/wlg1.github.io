# Tensor

**What are tensors?**

[https://www.youtube.com/watch?v=L35fFDpwIM4&ab_channel=StatQuestwithJoshStarmer](https://www.youtube.com/watch?v=L35fFDpwIM4&ab_channel=StatQuestwithJoshStarmer)

(Not from math view, but ML view): unlike normal scalars arrays matrices and n-dimensional matrices, tensors were designed to take advantage of hardware acceleration. In other words, tensors don't just hold data in various shapes like these, but they also allow for all the math that we have to do with the data to be done relatively quickly. Usually, tensors and the math they do are sped up with special chips called graphics processing units (GPUs). But there are also tensor processing units (TPUs) that are specifically designed to work with tensors and make neural networks run relatively quickly.

Automatic differentiation: tensors will also take care of derivates for you

- If each linearly independent column of a matrix is a dimension, does that mean a tensor is not just a multidimensional matrix?
    
    Yes, that is correct. While tensors and matrices can both be thought of as multi-dimensional arrays, tensors are a more general mathematical concept than matrices and can have an arbitrary number of dimensions.
    
    In linear algebra, a matrix can be thought of as a collection of vectors, where each column represents a vector in the space. The linearly independent columns of a matrix correspond to a set of basis vectors that span the column space of the matrix. 
    
    Tensors, on the other hand, can have an arbitrary number of dimensions and can represent more complex mathematical objects. For example, a tensor of rank two can be thought of as a multi-dimensional array of numbers, where each entry corresponds to a combination of two basis vectors. Tensors of higher rank can be thought of as arrays of numbers that correspond to combinations of more than two basis vectors.
    
    So while matrices can be thought of as tensors of rank two, not all tensors can be represented as matrices.
    
    - Give an example of a tensor of rank 2 that's not a matrix. Represent this as a figure
        
        One example of a tensor of rank 2 that is not a matrix is a color image. In digital image processing, an RGB color image can be represented as a three-dimensional array of numbers, where each entry corresponds to the intensity of the red, green, or blue color channel at a specific pixel location.
        
        The dimensions of the tensor correspond to the width, height, and color channels of the image. For example, a color image with dimensions 256x256x3 would have a tensor of rank 2 with shape (256, 256, 3).
        
        Here is an example of a small color image represented as a tensor:
        
        ```
        
        [[[255, 0, 0], [0, 255, 0]],
         [[0, 0, 255], [255, 255, 0]]]
        ```
        
        This tensor has dimensions 2x2x3 and represents a small image with red, green, and blue pixels arranged in a checkerboard pattern.
        
        - So elements of tensor can be matrices?
            
            Yes, that's correct. The entries of a tensor can themselves be matrices or other higher-dimensional tensors. In general, the entries of a tensor can be any mathematical object that is compatible with the algebraic operations defined on the tensor.
            
            For example, a tensor of rank 3 could be a collection of matrices, where each matrix corresponds to a particular slice of the tensor. Or a tensor of rank 4 could be a collection of tensors of rank 2, where each tensor of rank 2 corresponds to a particular sub-tensor of the rank 4 tensor.
            
            In machine learning, tensors with entries that are matrices or higher-dimensional tensors are commonly used to represent more complex objects such as images, videos, and sequences of data. These types of tensors are often referred to as multi-modal tensors, as they can represent multiple modes or types of information simultaneously.
            
        - Can matrices have vectors as elements? Does it depend on if it's a matrix of reals, etc.?
            
            Yes, a matrix can have vectors as its elements. In fact, this is a common way to represent collections of vectors in linear algebra.
            
            The entries of a matrix can be any mathematical object that is compatible with the algebraic operations defined on the matrix. In particular, if we have a collection of n vectors, each of dimension m, then we can represent this collection as an m x n matrix, where each column of the matrix corresponds to one of the vectors.
            
            It doesn't depend on whether the matrix is of real numbers or other types of numbers. The concept of a matrix is a general one that applies to any field, including the real numbers, complex numbers, or any other field. The only requirement is that the entries of the matrix come from the same field.
            
            For example, here is a matrix with vectors as its elements:
            
            ```
            [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
            ```
            
            In this case, the matrix has three columns, and each column represents a vector in three-dimensional space.
            
        

---

[**Sum over an index**](Tensor%205555c4af00994d9fb9a8b7e90d5b18de/Sum%20over%20an%20index%208e5f325c799447948ab6fc98514a56ea.md)