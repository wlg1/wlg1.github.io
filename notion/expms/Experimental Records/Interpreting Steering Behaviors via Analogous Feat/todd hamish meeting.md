# todd hamish meeting

[https://en.wikipedia.org/wiki/Plane-based_geometric_algebra#Projective_geometric_algebra](https://en.wikipedia.org/wiki/Plane-based_geometric_algebra#Projective_geometric_algebra)

[https://direct.mit.edu/netn/article/5/2/549/97548/Simplicial-and-topological-descriptions-of-human](https://direct.mit.edu/netn/article/5/2/549/97548/Simplicial-and-topological-descriptions-of-human)

generalization of a venn diagram

there’s a plane where triangle is in. geometric algebra does planes, not triangles

quaternion: rotation is a 3d simplex added to a 1d simplex (3 vol add to 1 vol). N vol added to (n-2) vol. 2d sphere added to a point, so is around a point. a 3d sphere rotates around a line.

rotation using n x n matrix- but getting an axis from the matrix (an eigenvector problem) is very painful , but geom alg says if you have a transformation then it can break into pieces and ask about those pieces (such as axis of rotation) 

you have something that preserves N things and rotates everything else 

linear features beget a linear plane since the plane / convex hull 

projecting 

for any k vol, can always ask what’s the transformation that this k-vol encodes

shapes and transformations are the “same” in geometric algebra. what happens if you transform a “tree” using the concept “dog”

reflect, rotate, generalizations of those

screw motion is a strange transformation

[https://bivector.net/tools.html?p=3&q=0&r=0](https://bivector.net/tools.html?p=3&q=0&r=0)

code to multiply these things, use cayley table

assume A*B = C. Also define inverting C^(-1)

sandwich product: X*Y*X^-1 = Z → this is alll you need to transform Y with X. if X is rotation, then Z is what you get if you rotate Y. 

N = 2000 (embedding space), X is rotation in N dims, therefore X is a N-volume added to a N-2-volume

N choose 2 plus 1 is dim of X, 2000 choose 2 is approx 2 million, still theoretically feasible to store

XYX^-1 : how long? X^-1 just negates 2 vol part. but multiplying the rest would be a lot of compute, need ot use, would want to use sparse repr

computational adn expm wise: find vector representations of features, and find relations between these vectors. but can we also represent features in other ways and then perform transformations

any k-vector is a vector. here they use 1-vector. actv adding is just 1-vector in 4098 dim space.

generalize distance

distance at angle is different

plane and point is just distance (not angle)

pair of lines and in most dims this is the case, they have both a distance and agle form each other. geom alg can extract the angle and distance, so not forced to use distance. 

simplest transformtion of this one to that one

ask todd for linalg advice; pair prog on lin alg proj code on steering feature vectors and seeing effects on features in next layers

[https://chatgpt.com/c/d5e58a44-0435-4126-9ec7-599afb64c2b0](https://chatgpt.com/c/d5e58a44-0435-4126-9ec7-599afb64c2b0)

- how does it differ from regular linalg, looks like its just geom transf
    
    Projective Geometric Algebra (PGA) differs from regular linear algebra in several key ways, although it builds on linear algebra concepts. Here are the main differences:
    
    1. **Homogeneous Coordinates**:
        - **Linear Algebra**: Typically deals with vectors in Euclidean space using Cartesian coordinates.
        - **PGA**: Uses homogeneous coordinates to represent points, lines, and planes in projective space. This allows for the representation of points at infinity and more flexibility in handling geometric transformations.
    2. **Geometric Interpretations**:
        - **Linear Algebra**: Primarily concerned with vector spaces, linear transformations, and solving systems of linear equations.
        - **PGA**: Extends these concepts to include geometric objects and their relationships. It is particularly well-suited for representing and manipulating geometric transformations such as rotations, translations, and scaling in a unified framework.
    3. **Multivectors and Operations**:
        - **Linear Algebra**: Focuses on operations involving vectors and matrices, such as dot products and matrix multiplication.
        - **PGA**: Introduces multivectors (combinations of scalars, vectors, bivectors, etc.) and operations such as the geometric product, outer product, and inner product. These operations are designed to work naturally with geometric entities and transformations.
    4. **Transformations**:
        - **Linear Algebra**: Uses matrices to represent linear transformations. Transformations are typically applied to vectors.
        - **PGA**: Uses the geometric algebra framework to represent and apply transformations directly to geometric objects (points, lines, planes) in a more intuitive and algebraically consistent manner.
    5. **Unification of Geometric Concepts**:
        - **Linear Algebra**: Requires different tools and methods to handle various geometric transformations and concepts (e.g., separate methods for translation, rotation, scaling).
        - **PGA**: Provides a unified algebraic system that can handle a wide range of geometric transformations and relationships seamlessly. For example, a single framework can represent both rotations and translations, which are treated separately in traditional linear algebra.
    6. **Higher-Dimensional Extensions**:
        - **Linear Algebra**: Extends to higher dimensions but often with increasing complexity in handling geometric interpretations.
        - **PGA**: Naturally extends to higher dimensions while maintaining consistent geometric interpretations and operations. This makes it powerful for applications in computer graphics, robotics, and physics.
    
    In summary, while PGA builds on the foundation of linear algebra, it extends and enhances it to provide a more comprehensive and unified approach to handling geometric transformations and relationships. This makes it particularly useful in fields that require sophisticated geometric reasoning and manipulation.
    
- why study multivectors ? what applications this has to nueral network latent spaces
    
    Studying multivectors and understanding their applications can offer several advantages, particularly in fields like computer graphics, robotics, physics, and even neural networks. Here’s an exploration of why multivectors are studied and their potential applications in neural network latent spaces:
    
    ### Why Study Multivectors?
    
    1. **Unified Framework for Geometric Transformations**:
        - Multivectors provide a unified framework to represent and manipulate geometric transformations such as rotations, translations, and scaling. This is particularly useful in 3D graphics and robotics where complex transformations are common.
    2. **Efficiency and Compactness**:
        - Using multivectors can lead to more efficient algorithms and compact representations of geometric data. This can improve computational efficiency and reduce storage requirements.
    3. **Intuitive Understanding of Geometric Relationships**:
        - Multivectors offer a more intuitive way to understand and work with geometric relationships. They make it easier to reason about the interactions between different geometric entities (points, lines, planes).
    4. **Extensibility to Higher Dimensions**:
        - The framework of multivectors extends naturally to higher dimensions, providing a consistent way to handle complex geometric and algebraic problems in higher-dimensional spaces.
    
    ### Applications in Neural Network Latent Spaces
    
    1. **Enhanced Feature Representation**:
        - In neural networks, particularly in deep learning, latent spaces represent compressed versions of input data. Using geometric algebra and multivectors, it may be possible to encode richer geometric relationships in these latent spaces, potentially leading to better feature representations.
    2. **Improved Geometric Transformations**:
        - Neural networks, especially convolutional neural networks (CNNs) used in image processing, can benefit from the robust and unified transformation capabilities of multivectors. For example, representing transformations in latent spaces more accurately could improve tasks like image recognition and object detection.
    3. **Equivariance and Invariance**:
        - Geometric algebra can help in designing neural network architectures that are equivariant or invariant to certain transformations. This means the network’s output can change predictably (or remain unchanged) when the input undergoes specific transformations, which is valuable in applications like computer vision and reinforcement learning.
    4. **Learning Geometric Relationships**:
        - Multivectors could enable neural networks to learn and encode geometric relationships directly. This is beneficial in tasks where spatial relationships are crucial, such as in 3D object recognition, scene understanding, and robotics.
    5. **Regularization and Constraints**:
        - Incorporating multivector representations can help impose geometric constraints and regularization in neural networks. This can lead to more robust and generalizable models by embedding prior geometric knowledge into the learning process.
    
    ### Example Use Cases
    
    1. **3D Computer Vision**:
        - In 3D computer vision, using multivectors can improve the network’s ability to understand and process 3D shapes, perform object detection, and recognize objects from different viewpoints.
    2. **Robotics**:
        - For robotic manipulation and navigation, multivectors can help neural networks better understand and manipulate spatial relationships, leading to more accurate and efficient robot control.
    3. **Physics Simulations**:
        - In physics-based simulations, representing physical entities and their interactions using multivectors can lead to more accurate models that neural networks can learn from and predict.
    4. **Generative Models**:
        - In generative models like Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs), multivectors can improve the representation of latent spaces, leading to better generation of complex structures such as human faces, natural scenes, and 3D objects.
    
    In summary, studying multivectors and applying them in neural network latent spaces can lead to more powerful, efficient, and geometrically aware models. This can enhance performance in various applications, from computer vision and robotics to generative modeling and beyond.
    
- what relation do multivector have with simplicial complexes and hierarchical concepts in latent space
    
    Multivectors, simplicial complexes, and hierarchical concepts in latent spaces can interrelate in meaningful ways, particularly in the context of geometric and topological data analysis, and machine learning. Here's how they connect:
    
    ### Multivectors and Simplicial Complexes
    
    **Multivectors**:
    
    - Multivectors are elements of geometric algebra that can represent various geometric objects (scalars, vectors, bivectors, trivectors, etc.).
    - They provide a compact and algebraically rich framework to describe geometric transformations and relationships.
    
    **Simplicial Complexes**:
    
    - Simplicial complexes are a combinatorial structure made up of simplices (points, line segments, triangles, and their higher-dimensional counterparts).
    - They are used in computational topology to study the shape of data, particularly in persistent homology, which is a method in topological data analysis.
    
    **Relation**:
    
    - Multivectors can represent the oriented volumes of simplices in a geometric algebra framework. For instance, a bivector can represent an oriented area (a 2-simplex), and a trivector can represent an oriented volume (a 3-simplex).
    - In computational topology, geometric algebra can be employed to perform operations on these simplices more efficiently and intuitively, leveraging the algebraic structure provided by multivectors.
    
    ### Hierarchical Concepts in Latent Space
    
    **Hierarchical Latent Spaces**:
    
    - In machine learning, particularly in neural networks, latent spaces are representations where data is encoded into a lower-dimensional space.
    - Hierarchical latent spaces involve multiple levels of abstraction, where higher levels capture more abstract features and lower levels capture more concrete features.
    
    **Relation to Simplicial Complexes and Multivectors**:
    
    - **Simplicial Complexes**: These can be used to model hierarchical relationships within the data. For example, different layers of simplices can represent different levels of abstraction in the latent space, capturing hierarchical structures within the data.
    - **Multivectors**: By leveraging the rich algebraic properties of multivectors, one can efficiently encode and manipulate these hierarchical structures. For example, a multivector can represent complex hierarchical relationships within the latent space, capturing interactions between different levels of features.
    
    ### Applications
    
    1. **Topological Data Analysis (TDA)**:
        - **Using Simplicial Complexes**: TDA involves using simplicial complexes to study the topological features of data. Persistent homology, a TDA technique, can identify and analyze features at multiple scales, providing insights into the hierarchical structure of data.
        - **Multivectors**: In TDA, multivectors can represent simplices in a way that facilitates geometric computations, making it easier to analyze and manipulate topological features.
    2. **Neural Network Latent Spaces**:
        - **Hierarchical Representations**: In neural networks, especially deep learning models, hierarchical latent spaces can be used to capture complex, multi-scale features of the input data.
        - **Geometric and Topological Insights**: By representing these hierarchical features using simplicial complexes and multivectors, one can gain deeper geometric and topological insights into the latent space, potentially leading to better understanding and improvements in model architecture and performance.
    3. **Geometric Deep Learning**:
        - **Combining Concepts**: Geometric deep learning aims to extend deep learning techniques to non-Euclidean spaces (graphs, manifolds). Using multivectors and simplicial complexes can provide a framework for such extensions, allowing the models to capture more complex geometric and topological structures within the data.
    
    ### Summary
    
    - **Multivectors** provide a powerful algebraic tool to represent and manipulate geometric objects and transformations, which can be applied to simplicial complexes in computational topology.
    - **Simplicial Complexes** are crucial for understanding the topological structure of data, especially in hierarchical and multi-scale contexts.
    - **Hierarchical Latent Spaces** in neural networks benefit from these concepts by allowing for richer, multi-level representations of features, leading to potentially more robust and insightful models.
    
    By integrating these concepts, one can create more sophisticated models that leverage geometric and topological properties of data, leading to advancements in fields such as data analysis, machine learning, and beyond.