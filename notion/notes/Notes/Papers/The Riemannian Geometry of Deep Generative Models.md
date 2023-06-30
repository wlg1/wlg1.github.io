# The Riemannian Geometry of Deep Generative Models

- What does it mean to minimize an energy functional to compute a geodesic curve?
    1. Geodesic Curve: In differential geometry, a geodesic curve is the shortest path between two points on a curved surface or a manifold. It generalizes the concept of a straight line in Euclidean geometry to curved spaces. Geodesics can be thought of as the paths that minimize distance or energy between two points.
        
        Use the least energy to traverse between the two points
        
    2. Energy Functional: An energy functional is a mathematical function that assigns an energy value to each possible curve or path. In the context of geodesic computation, the energy functional quantifies the total energy associated with a given curve. The energy functional typically depends on various properties of the curve, such as its length, curvature, and other geometric characteristics.
    - What's energy in an energy functional of a curve? Why is it called energy?
        
        Comes from an analogy with physical systems, where it represents a measure of the system's ability to perform work or undergo changes.
        
        1. Length or Arc Length: In some cases, the energy functional might be defined as the length or arc length of the curve. The length of a curve represents the distance traveled along the curve, and it can be viewed as a measure of the "energy" required to traverse the curve.
        2. Curvature: The energy functional may also consider the curvature of the curve. Curvature measures how sharply the curve deviates from a straight line at each point. Higher curvature typically implies more bending or "energy" required to follow the curve.
        3. Deformation: In other scenarios, the energy functional might capture the deformation or distortion of the curve. It could measure the amount of stretching, compression, or bending that occurs along the curve, which can be interpreted as an "energy" associated with the deformation.
    
    To compute a geodesic curve, one would typically formulate an energy functional that captures the desired properties of the curve, such as minimizing length or curvature. Then, mathematical techniques like variational calculus or optimization methods are used to find the curve that minimizes the energy functional. 
    

- we can bring a vector into tangent space by SVD of the Jacobian