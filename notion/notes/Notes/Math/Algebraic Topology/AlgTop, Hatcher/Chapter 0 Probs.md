# Chapter 0 Probs

0.1 to 0.13 are deformation retractions

0.14 to 0.29 are cell complex homotopic equivalences

---

- 0.1
    - Scratchwork
        - Guess that the deleted point on torus is mapped to the intersecting point of 2 circles
        - Guess the longitude is mapped to one circle, and meridian mapped to second
        
        ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled.png)
        
    - Interpret Solution
        
        [https://chat.openai.com/c/10b8774a-891b-42db-8940-2a197cc449be](https://chat.openai.com/c/10b8774a-891b-42db-8940-2a197cc449be)
        
        - explain this more intuitively in easier terms, relating it to what it has to do with two intersecting circles
            
            ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%201.png)
            
        
        This text describes a process that takes a square (representing a torus with a point removed) and continuously shrinks it down to its boundary, which consists of two intersecting circles. Imagine pinching the center of a square made of a flexible material and stretching it outward until only the edges remain, forming the shape of the number "8". The function \( f_t(x, y) \) gradually morphs each point inside the square towards this boundary over time \( t \), from \( t = 0 \) (the start, where the square is unchanged) to \( t = 1 \) (the end, where the square becomes the two circles).
        
        Non-AI: 
        
        Because the gluing diagram boundaries of a torus are two circles (The meridian lines run vertically around the torus, and the longitude lines run horizontally), the problem means to deform the interior of the torus onto its boundaries, making it hollow. 
        
        The reason we can do this when there’s a deleted point is because this hole (void) is the “hollow” part. Without it, the filled interior has no hole, and is thus not topologically equivalent to the 2 circles intersecting at a point. 
        
    - Poss reasoning to soln
        
        [https://riemannianhunger.wordpress.com/solutions-to-algebraic-topology-by-allen-hatcher/hatcher-0-1/](https://riemannianhunger.wordpress.com/solutions-to-algebraic-topology-by-allen-hatcher/hatcher-0-1/)
        
        1. Get definition of torus and convert in terms of the square *gluing diagram*
        2. Realize the 2 circles intersecting at a point is the same as the boundary of the gluing diagram, which is a boundary of a square
            1. Instead of transforming the torus to its boundaries, transform its gluing diagram to its boundaries- this is an easier problem
        3. Find the domain and range spaces of the deformation retraction function. The torus gluing diagram is in R^2 (or $I \times I$, where $I \in [-1,1]$) and its boundary is in R^2, so is R^2 to R^2, or f(x,y).
        4. The deformation retraction function is a homotopy family $f_t (x,y)$. A homotopy is a continuous transformation from one function to another, parameterized by t in the interval [0,1]. 
            1. Let’s try to use a simple model first. A linear homotopy uses the form $f_t = (1-t)*f_0 + (t)*f_1$. Thus, we need to find $f_0$ and $f_1$. 
                - What is linear homotopy
                    
                    The specific form \( (1 - t)f_0 + tf_1 \) is a common example of a linear homotopy, which is a particular type of homotopy between two functions \( f_0 \) and \( f_1 \). In this linear homotopy, for each point \( x \) in the space, the point is transformed from \( f_0(x) \) to \( f_1(x) \) in a straight line as \( t \) varies from 0 to 1.
                    
                    However, not all homotopies need to be linear. The general requirement for a family of functions \( H(x, t) \) to be a homotopy between two functions \( f \) and \( g \) is that:
                    
                    1. \( H(x, 0) = f(x) \) for all \( x \) (this is the function at the start of the homotopy).
                    2. \( H(x, 1) = g(x) \) for all \( x \) (this is the function at the end of the homotopy).
                    3. \( H \) is continuous in both \( x \) and \( t \).
                    
                    The form \( H(x, t) = (1 - t)f(x) + tg(x) \) is just the simplest example, where the transformation from \( f \) to \( g \) is done in a straight line or in a "linear" fashion with respect to \( t \). This is convenient and easy to visualize, but more complex homotopies can involve much more intricate paths and methods of transformation, as long as they satisfy the continuity requirement.
                    
            2. SIDENOTE: In detail, a def ret is a process by which a space is continuously shrunk to a subspace in such a way that the subspace remains fixed
                - Def: def ret
                    
                    ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%202.png)
                    
                - Def: homotopy
                    
                    ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%203.png)
                    
        5. f_0 is just f(x,y)
        6. To find f_1, the equation for the boundary of a square is
            
            ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%204.png)
            
        7. Sub them in to obtain this function:
            
            ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%205.png)
            
            This is a homotopy family from spaces
            
            ![Untitled](Chapter%200%20Probs%2030aa872a87d444ecb9d6df63025e9e46/Untitled%206.png)
            
        8. Check it’s continuous (?)
    - Generalize reasoning to soln
        - GEN PROB: Find a function (that’s a type of homotopy)
            - GEN SOLN: Try to fill in linear homotopy equation first
        - GEN PROB: find a homotopy/homeomorphism function for a shape
            
            Hard because what’s the equation for that complicated shape?
            
            - GEN SOLN: see the shape as its gluing diagram, and transform that instead
            - WHY: The gluing diagram shows the topology and has easier equations in 2D, so is easier for our minds to both visualize and model as equations
    - Compare scratchwork to soln
        - Mistake: The deleted point of the torus was not seen as FULLY going through the entire torus, but just one part of its surface. The gluing diagram shows it as fully going through.
        - Did not know the definition of homotopy family, and that def ret is a type of one. Thus, didn’t know needed to find f_0 and f_t
- 0.2
    - Scratchwork
        
        This sounds like 0.1, but with shrinking instead of stretching.