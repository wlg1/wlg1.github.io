# Linear Algebra

[Matrix Multiplication](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Matrix%20Multiplication%20114407d494a34203b4e6e68b5496efe3.md)

[Low Rank](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Low%20Rank%20818dedfe95ac406c8a655a1bcb715813.md) 

[Determinant](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Determinant%20a06d6e4f4bca4a8fa95e6ca6d5364b61.md)

[Eigenvalues](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Eigenvalues%2089e61573e33743da932dbb63575d7600.md) 

[Singular Values](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Singular%20Values%20837973abb02f400faa322e0a56f9415b.md) 

[SVD](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/SVD%20b6e01b133b7d495b81236acafc3cea9b.md)

[Positive semidefinite](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Positive%20semidefinite%20920c5133c7164318beee2503e482dda6.md)

[Jacobian](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Jacobian%20165dd8f2c88b48758e8f2b8878c49db2.md) 

[Triangular Forms](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Triangular%20Forms%209953416118784fccab5c39e7e4046aad.md) 

[Outer Product](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Outer%20Product%2065f8a1a8e8fd45c4ac6e59d22afad162.md)

[Dot Product](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Dot%20Product%20db791e171b114aa1b4dd4edf67362ab3.md)

[Unstable Matrices](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Unstable%20Matrices%20058376257eae4b09b7adf3cad29ff23d.md) 

[Rank-1 Updates](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Rank-1%20Updates%205c333cecc74b4b17a0e585b31bbc6849.md)

[Affine](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Affine%20afe0e7fdf70a41bd94641bff03fbd4c4.md)

[Moore penrose inverse](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Moore%20penrose%20inverse%2096b4529e2abb4a0cab9ad796f01eff1f.md)

[Matrix row vectors](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Matrix%20row%20vectors%2048855e328f26473d8351c564fe666de6.md)

[Kronecker Product](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Kronecker%20Product%20522d797501164854b3b6a5597cd35157.md)

---

[MIT 18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/MIT%2018%20065%20Matrix%20Methods%20in%20Data%20Analysis,%20Signal%2006b8a1fe738744d0890b812702c5cd60.md)

---

Non-linear functions, such as exponential, logarithmic, or trigonometric functions, generally cannot be represented by matrices. One common approach is to use an algorithm that approximates the function using a series of simpler, linear functions. This is often done using techniques such as interpolation or regression. Another approach is to use iterative numerical methods to approximate the value of the function at a given point. For example, one can use Newton's method or gradient descent to find the root of a nonlinear equation or the minimum of a nonlinear function.

---

[https://dynalist.io/d/AzaG5a1q-GLme4SmFrDlLD-O](https://dynalist.io/d/AzaG5a1q-GLme4SmFrDlLD-O)

![Untitled](Linear%20Algebra%20e6bc642112314024b2392685dfd6e47a/Untitled.png)

- each row and col in a matrix forms a dimension in a coordinate space. but a 2D matrix is one with rows and cols. why is dimension used differently in these cases?
    
    The term "dimension" in mathematics and physics can have slightly different meanings depending on the context in which it's used.
    
    1. **Dimension in Coordinate Space:**
    When talking about coordinate spaces, each dimension corresponds to one degree of freedom that a point can have. For example, in a 3-dimensional coordinate space, each point is defined by three coordinates (x, y, z), with each coordinate representing a dimension. Here, dimensions are axes in space along which you can measure positions.
    2. **Dimension in Matrices:**
    When referring to matrices, the "dimension" often refers to the number of rows and columns in a matrix. A 2D matrix has two dimensions: one for rows and the other for columns. This can be confusing because a 2D matrix does not represent a two-dimensional space in the same way that a coordinate system does. Instead, it's a tabular representation of data that can store information that maps to higher-dimensional spaces.
        - For instance, a matrix with 3 rows and 3 columns is a 2D matrix, yet it can represent points in a 3-dimensional space where each row or column corresponds to a different point or vector in that space.
    
    In the context of matrices, when people refer to a "2D matrix," they are usually distinguishing it from higher-dimensional arrays such as 3D matrices (often called tensors in this context), which would have rows, columns, and depth - representing yet another axis of data.
    
    So, while the term "dimension" does have a consistent underlying idea of representing an axis or a degree of freedom, its specific interpretation can change depending on whether we're discussing the geometry of a space or the structure of data within an array-like entity such as a matrix.