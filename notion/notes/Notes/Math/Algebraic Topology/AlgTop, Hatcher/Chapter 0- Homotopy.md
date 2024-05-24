# Chapter 0- Homotopy

- orig text
    
    ![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled.png)
    

When reading this, the “inner A” looks bold, so readers may confuse that as the “thick” and wonder where the thin is (is it within that as a thinner A?) But the thick is actually the boundary of this amogus:

![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%201.png)

![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%202.png)

After p2, we can do Exercise 0.1. Tell students to pause video and try it themselves if they want before solution explanation.

- Don’t go through entire text; tell students to use the principles of how to understand the text shown here to go through the rest in their own way. For rsch groups, tell them to divide & conquer with some “common overlap” of fundamental concepts so they can communicate, so each individual specialize in a section and can solve exercises with combined knowledge.
    
    Eg) All read ch 1. Then one person (or rsch sub-group) reads ch2, another reads ch3. These are disjoint chapters, not built on top of each other. When solving ch4 problems that rely on both 2 and 3, the two come together to solve it.
    
    This can be organized decen by discord “guilds” that stream audience is on
    
    Their findings can be put on ReLayT
    
    The audience should be more specialized than you; the conductor does not play the violin
    
    Encourage multiple people to do their own interpretations of the same material as you may not cover and understand everything
    

---

Mapping Cylinder (quotient space)

- orig text
    
    ![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%203.png)
    

The disjoint union would take EVERY pair of points from (X x I) and Y. if you plot all these pairs, it’s as if you place all the transitions of a film onto one still image (can’t find this on google)

- Inuitive analogy for this disjoint union
    
    ![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%204.png)
    

A quotient space is under an equivalence relation. What is the equivalence relation of the mapping cylinder of f(x)?

[https://en.wikipedia.org/wiki/Mapping_cylinder](https://en.wikipedia.org/wiki/Mapping_cylinder)

![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%205.png)

The quotient space of this disjoint union is the SAME as the disjoint union EXCEPT one end of (X x I) is made equal to f(x) using the eqv reln. 

(This “making the same using eqv reln” is “gluing”).

Manim will definitely help to show deformations (more efficient when pre-made than live lectures)

---

p3:

[https://chat.openai.com/c/726bfa5b-f103-493c-8718-e268e4412d78](https://chat.openai.com/c/726bfa5b-f103-493c-8718-e268e4412d78)

This section asks questions using the above chat link

- what is this notation
    
    ![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%206.png)
    
    The notation \( f_t | A \) typically denotes the restriction of a function \( f_t \) to a subset \( A \) of its domain. This means that you consider the function \( f_t \) only on the set \( A \). The subscript \( t \) might indicate that \( f \) is part of a family of functions indexed by the parameter \( t \), or it could represent a function that changes over time if \( t \) is a time parameter.
    
- Deformation retraction $X → X$ is a type of homotopy $X → Y$ where $f_0 =$  identity, and $f_1 = A$, where A is a subspace of X
- f_1 = A is actually a “retraction of X onto A”.
- A retraction is also a map r
    - Not all retractions come from deformation retractions
        - “a space that deformation retracts onto a point must be path-connected”. does this mean there must be a homotopy? so a retraction does not need to be part of a homotopy?
            
            ### Path-Connectedness
            
            A space \(X\) is **path-connected** if for any two points \(x, y \in X\), there exists a continuous path $p: [0,1] \to X$ with \(p(0) = x\) and \(p(1) = y\). This is a property indicating that any two points in the space can be connected by a continuous path.
            
            ### Relating the Concepts
            
            When we say that a space deformation retracts onto a point, it means there is a deformation retraction \(F: X \times [0,1] \to X\) onto that point. Because a deformation retraction is a type of homotopy, there indeed must be a homotopy involved.
            
            If a space \(X\) deformation retracts onto a point, this implies \(X\) is path-connected. Here's why: Pick any two points \(x, y \in X\). Since \(X\) deformation retracts to a point, there is a continuous path (formed by the deformation retraction) from \(x\) to the point, and from the point to \(y\). Concatenating these paths gives a continuous path from \(x\) to \(y\), showing \(X\) is path-connected.
            
            A **retraction** is a continuous map \(r: X \to A\) where \(A \subseteq X\) and \(r(a) = a\) for all \(a \in A\). A retraction doesn't necessarily involve a homotopy unless it's a deformation retraction. A deformation retraction is a stronger condition, requiring the entire space to continuously shrink to the subspace \(A\) over time, while still being a type of retraction.
            
            So, to summarize:
            
            - A deformation retraction onto a point indeed requires a homotopy, as it is a homotopy itself that fixes a point (or subspace) while the rest of the space deforms into it.
            - A space that deformation retracts onto a point must be path-connected, as the homotopy provides continuous paths between any points in the space.
            - A general retraction does not necessarily involve a homotopy, but a deformation retraction does, by definition.
        - does homotopy require a path-connected condition? are all path-connected functions homotopies?
            - **Requirement of Path-Connectedness for Homotopy:** The concept of homotopy itself does not require the initial space \(X\) or the target space \(Y\) to be path-connected. Homotopy is a broader concept that applies to functions between topological spaces, regardless of their path-connected properties.
            - Not all continuous functions between path-connected spaces are homotopies, but all paths in a path-connected space form homotopies with each other. For example, any two paths \(p, q: [0, 1] \to X\) with \(p(0) = q(0)\) and \(p(1) = q(1)\) in a path-connected space \(X\) are homotopic, as you can always "slide" one path to the other within \(X\).
            - Saying "path-connected functions" is a bit of a misnomer. Functions themselves aren't described as path-connected; rather, the spaces they map to or from might be. If you're asking whether all functions between path-connected spaces are homotopic, the answer is no. Whether two functions are homotopic depends on the existence of a continuous deformation between them, which is not guaranteed just by path-connectedness.
            
            To summarize:
            
            - Homotopy involves a relationship between two functions and does not inherently require either the domain or codomain to be path-connected, though the concept of creating a "path" or deformation between functions is related to the idea of connectivity.
            - A space being path-connected means that any two points in the space can be connected by a continuous path, but this doesn't automatically make any two continuous functions between two path-connected spaces homotopic. Homotopy depends on the specific functions and spaces involved.
- if a homotopy is a def ret to A, that homotopy is **homotopy relative to A**
- homotopy equivalence: this is a PROPERTY of a pair of homotopies (f:X→Y) and (g:Y→X), if
    
    ![Untitled](Chapter%200-%20Homotopy%20ad416961cdee4c5db3da0836c13823d7/Untitled%207.png)
    
    - this DOES NOT SAY two homotopies (f:X→Y) and (g:Y→X) are “equal” under an eqv reln
- homotopy equiVALENT: refers to the SPACES X and Y, not functions
    - this DOES SAY two spaces are “equal” under an eqv reln (f, g)
    - [see examples](https://www.notion.so/Public-Links-91d2e0a72099442aa995b60c18d94a35?pvs=21)
        - A [homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism) is a special case of a homotopy equivalence
- It is true in general that two spaces X and Y are homotopy equivalent if and only if there exists a third space Z containing both X and Y as deformation retracts.
    - Z can be the mapping cylinder
    - explain how this is abstracted in category theory and why it is abstracted. does it have anything to do with pushouts or pullbacks?
        
        Yes, indeed. The concepts of pushouts and pullbacks in category theory are related to constructions like the mapping cylinder in topology, which can be viewed as instances of these categorical constructions.
        
        ### Pushouts
        
        A pushout in category theory is a way of "gluing" together objects along a common part. If you have two morphisms \( f: Z \to X \) and \( g: Z \to Y \) with a common domain \( Z \), their pushout is an object \( P \) together with two morphisms \( i_X: X \to P \) and \( i_Y: Y \to P \) that "paste" \( X \) and \( Y \) together along \( Z \).
        
        In topology, the pushout corresponds to gluing spaces together along a shared subspace. The mapping cylinder can be viewed as a pushout of the diagram consisting of \( f: X \to Y \) and the identity \( id_X: X \to X \). You are "gluing" \( X \) to \( Y \) along \( X \) via \( f \), and the resulting pushout space is the mapping cylinder of \( f \).
        
        ### Pullbacks
        
        Conversely, a pullback is like a pushout, but for "pulling" objects back along morphisms. Given two morphisms \( f: X \to Z \) and \( g: Y \to Z \) with a common codomain \( Z \), their pullback is an object \( Q \) together with two morphisms \( p_X: Q \to X \) and \( p_Y: Q \to Y \) that "pull" \( X \) and \( Y \) back along \( Z \).
        
        In topology, pullbacks correspond to fiber products or fibered sums. For example, the pullback of two covering maps over a shared base space would give you the fibered product of the coverings.
        
        ### Relevance to Deformation Retracts
        
        The mapping cylinder is one way of combining spaces that shows how homotopy equivalences can be realized by joining spaces together along maps. This is particularly relevant when one considers the process of attaching cells in CW complexes, a fundamental construction in algebraic topology.
        
        In essence, both pushouts and pullbacks are categorical tools for constructing new objects from given ones and for analyzing the relationships between different objects in a category. They help establish conditions under which certain properties (like being a deformation retract) are preserved or reflected in the constructions. These constructions are very natural in the topological setting and are often used to build or analyze complex spaces from simpler ones.
        
    
    - do pullbacks break apart, like "unmixing"?
        
        Pullbacks in category theory don't exactly "unmix," but they do in a sense "factor out" the common information shared by two morphisms with a common target. Here's a bit more about how they work:
        
        ### Pullbacks and Their Purpose
        
        In category theory, a pullback is a limit, which means it is a universal construction that takes a diagram of objects and morphisms and produces a new object that satisfies a particular universal property with respect to that diagram.
        
        Given two morphisms \( f: X \to Z \) and \( g: Y \to Z \) with a common codomain \( Z \), the pullback essentially asks: What is the most general object \( P \) from which there are morphisms to \( X \) and \( Y \) that are compatible with \( f \) and \( g \)? This object \( P \) along with the morphisms \( p_X: P \to X \) and \( p_Y: P \to Y \) form the pullback diagram.
        
        ### How Pullbacks Work
        
        Pullbacks "pull back" the information from \( Z \) into \( X \) and \( Y \) to find a new object \( P \) that simultaneously maps into \( X \) and \( Y \) in a way that's consistent with the original maps to \( Z \). This new object \( P \) is typically a subset or a product of \( X \) and \( Y \) with some additional structure or restrictions.
        
        ### "Unmixing" Interpretation
        
        If you think of \( f \) and \( g \) as mixing or projecting information from \( X \) and \( Y \) into \( Z \), then the pullback \( P \) can be viewed as the space of "unmixed" or "separated" information where each point corresponds to a specific combination of points in \( X \) and \( Y \) that map to the same point in \( Z \).
        
        ### In Topology
        
        In the topological context, consider two spaces \( X \) and \( Y \) that are mapped into a space \( Z \) by functions \( f \) and \( g \). The pullback of \( f \) and \( g \) is the space consisting of pairs \( (x, y) \) where \( x \) is in \( X \), \( y \) is in \( Y \), and \( f(x) = g(y) \) in \( Z \). It forms a subspace of the product space \( X \times Y \). In this way, the pullback in topology captures the idea of "unmixing" to the extent that it reconstructs the pairs of preimages from \( X \) and \( Y \) that were identified or "mixed" in \( Z \).
        
        So while pullbacks don't "unmix" in a literal sense, they do serve to trace back through the morphisms to an original source of information before the "mixing" took place, allowing you to reconstruct what combinations of elements in \( X \) and \( Y \) would map to the same point in \( Z \).
        
    - what does the category theory definition of pullback have to do with how vectors are transported between manifolds using pullback functions in diff geometry?
        
        ### Pullback in Category Theory
        
        In category theory, a pullback (also known as a fibered product) is a construction that deals with two morphisms that have a common codomain. It results in a new object that represents the most general object that maps into both objects in a manner that is compatible with the original morphisms.
        
        ### Pullback in Differential Geometry
        
        In differential geometry, a pullback is an operation that takes a differential form on one manifold and "pulls it back" along a smooth map to a differential form on another manifold. This allows one to compare and transfer geometric information between different spaces.
        
        ### Connection Between the Two Concepts
        
        The connection between these two notions of pullback lies in the idea of inverse images and preimages:
        
        - In **category theory**, the pullback object can be thought of as the "inverse image" or "preimage" of a diagram of spaces and morphisms, where the "image" is considered in the categorical sense.
        - In **differential geometry**, the pullback of a differential form by a smooth map \( f: M \to N \) is literally taking the preimage of geometric structures (like tensors or forms) on \( N \) and transferring them to \( M \).
        
        ### Abstract vs. Concrete
        
        The categorical pullback is more abstract. It is concerned with objects and morphisms in an arbitrary category and doesn't have to involve any geometric or topological structure. The pullback in differential geometry, on the other hand, is very concrete. It involves actual functions (smooth maps) between manifolds and the preimages of geometric or algebraic objects (like differential forms).
        
        ### Underlying Philosophy
        
        Both concepts embody the philosophy of taking something from one context (a codomain or a target manifold) and figuring out where it came from or how it relates to another context (the domain or source manifold). They both represent fundamental ways of transferring and comparing information across different mathematical structures.
        
        While the specifics of how pullbacks work in category theory and differential geometry are quite different, they are united by this underlying principle of inverse mapping or "pulling back" information from one space to a space with which it has a relationship defined by some kind of mapping or morphism.
        
    - Cells can be attached by “gluing” using eqv relns.
        - In mapper, subsets of neighborhoods with the same points are “the same” and become one edge (?)
            
            Yes, you are on the right track with both concepts.
            
            ### Attaching Cells Using Equivalence Relations
            
            In topology, when we talk about attaching cells, we are typically referring to the process used in the construction of CW complexes. To attach an \( n \)-dimensional cell \( e^n \) to a space \( X \), we map the boundary of the cell, which is an \( (n-1) \)-sphere \( S^{n-1} \), to \( X \) via a continuous map \( f \). This map \( f \) is often referred to as the "attaching map."
            
            The new space, \( X \cup_f e^n \), is formed by taking the disjoint union of \( X \) and \( e^n \) and then using an equivalence relation that identifies each point of \( S^{n-1} \) with its image in \( X \) under the attaching map \( f \). So, two points are considered equivalent if one is a point on the boundary of the cell and the other is its image in \( X \).
            
            ### Mapper and Equivalence Relations
            
            The Mapper algorithm is a tool from topological data analysis (TDA), which is used for identifying and analyzing high-dimensional data structure via topological methods. The algorithm works by:
            
            1. Covering the data set with overlapping neighborhoods.
            2. Clustering the data points within each neighborhood.
            3. Abstracting each cluster to a single point or node.
            4. Connecting nodes if their corresponding clusters in the data set intersect.
            
            Here, the Mapper constructs a simplicial complex (often visualized as a graph) where the nodes represent clusters of data points that are "the same" in some sense, typically according to some filtering function that measures a property of the data. An edge between two nodes indicates that the corresponding clusters share common data points. The equivalence relation in this context identifies points within the same cluster, simplifying the complex structure of the data into a more understandable form.
            
            While both attaching cells in topology and clustering in the Mapper algorithm use equivalence relations to simplify structures, the contexts and goals are different. In topology, cells are attached to build up spaces in a controlled, incremental way. In TDA, the Mapper algorithm is used to reduce high-dimensional data into a simpler form that can still reveal important features of the data's shape.
            
        - do points that are in two clusters become part of the same edge? are they still in both nodes?
            
            In the context of the Mapper algorithm in Topological Data Analysis (TDA), the terms "clusters" and "edges" refer to different elements of the constructed simplicial complex, which is often visualized as a graph. Here's how it works:
            
            1. **Clusters**: The Mapper algorithm first partitions the data set into overlapping neighborhoods based on a filtering function. Within each of these neighborhoods, it applies a clustering algorithm to group the points into clusters.
            2. **Nodes**: Each cluster is then represented as a single node in the Mapper graph. If you have overlapping neighborhoods where the same data point belongs to clusters in each neighborhood, this data point will be part of multiple clusters.
            3. **Edges**: If two clusters (nodes) have a non-empty intersection (meaning they share at least one data point), an edge is created between them in the Mapper graph. This indicates that there is a "path" or connection between the two clusters through the shared data points.
            
            So, to answer your questions:
            
            - **Do points that are in two clusters become part of the same edge?**
                
                Yes, if points are in two different clusters, and those clusters are determined to be connected (i.e., have a non-empty intersection), then an edge is drawn between the two corresponding nodes in the Mapper graph. This edge represents the shared data points between the clusters.
                
            - **Are they still in both nodes?**
                
                Yes, each node represents a cluster, and if a data point is part of two clusters, then it is represented in both of the corresponding nodes. In the graphical representation, such a point contributes to the reason why there is an edge between the two nodes.
                
            
            The Mapper graph, as a result, can reveal the underlying shape or structure of the data by showing how these clusters are connected, giving insights into the high-dimensional or complex structure of the data set.
            
- Contractible: a space can be sent to a point (by a homotopy)
    - nullhomotopic: a property of an identity map. Means the map is homotopic to (same as under homotopy f) a constant map
        - A map (not necessarily the identity) is **nullhomotopic** if it can be continuously deformed into a constant map.
- is a homotopy bewteen functions or spaces?
    
    A homotopy is between functions. More precisely, it's a process that continuously deforms one function into another, within a certain fixed time interval
    
    While we say that the homotopy is between functions, the existence of a homotopy between two identity functions on spaces X and Y often leads to the notion of the spaces themselves being homotopy equivalent. This means that the spaces can be continuously deformed into each other, but it is the functions (in this case, the identity and some constant functions) that are actually being homotopically deformed.
    

- Non-trivail example of “a deformation retraction to a point:: **house with two rooms**
    
    [https://www.youtube.com/watch?v=uI3XPJAsLws&ab_channel=PhysicsforDumbos](https://www.youtube.com/watch?v=uI3XPJAsLws&ab_channel=PhysicsforDumbos)
    
    [https://mathoverflow.net/questions/17551/how-to-show-that-the-bings-house-with-two-rooms-is-contractible](https://mathoverflow.net/questions/17551/how-to-show-that-the-bings-house-with-two-rooms-is-contractible)