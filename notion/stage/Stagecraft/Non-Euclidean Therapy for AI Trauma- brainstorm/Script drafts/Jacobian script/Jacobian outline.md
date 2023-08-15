# Jacobian outline

1. Use 2D: f(p) = (h1(p), h2(p)) ; p = (x1, x2)
    1. p = (2,3) and f(p)
    2. h1(x1) (eg. x1^2)
    3. h1(x1,x2) (eg. = x1^2 + x2 = 4+7 = 11)
    4. h2(x1,x2)
    5. remove f and h(p) to declutter
    - fig (no need plot in 3D if no specific fns)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled.png)
        
2. Explain dx and dh graphically, and d/dx as basis of tangent space to get tangent vector. Show coordinates starting from (0,0) of tangent space. Have it in a colored square different from rest of manifold
    - How do we define "A derivative measures how much something changes in response to a small change in something else." in relation to tangent space basis vectors? What is in response to a small change in the basis vector?
        
        The connection with our derivative idea: When you compute the derivative of a function in the direction of a basis vector, you're essentially asking, "If I make a small change in the direction of this specific basis vector, how much does my function change?”
        
    1. d/dx1 and d/dx2 is tangent space at p. Each p has its own tangent space with these basis vectors.
    2. v in tangent space. have actual values, where the origin of the tangent space is (0,0). they are not defined relative to the manifold space, but relative to the tangent space at its point p
    3. value of v by red and blue components
    4. Jacobian J_f maps to tangent space at f(p)
    - explanation
        - The Jacobian matrix represents how small changes in x and y (the basis vectors of the domain space) affect u and v (in the target space).
            - Specifically, the entry du/dx tells you how much u changes for a small change in x, holding y constant, and similarly for the other entries of the Jacobian matrix.
            - The columns of the Jacobian matrix represent the rates of change of the functions u(x, y) and v(x, y) with respect to the variables x and y.
        
    - fig
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%201.png)
        
3. Show this:
    1. Jacobian matrix (may say J_h after demo h is from f)
        
        Show the 2D mat visuals again, but this time:
        
        nap / ear —> dh_1 / dx_1
        
    2. “Abuse of notation” for demo purposes add ratio next to dh/dx of “d/dh_1 / d/dx_1” ; we are not actually dividing by the partial derivatives, and “d/dh_1 / d/dx_1” ratio is not an actual mathematical expression
    3. From first row of J, map red to dh1, then blue to dh1
        1. show again as close up of tangent spaces
    4. Calculate SPECIFICS now- dh/dx1 = 2x1 = 2(2) = 4
        1. Fill in Jacobian values one by one. Closeup of equations and J
            1. (only first row)
            2. as an analogy, think of this like slope: does it depend on it? no. in higher dim, this is not the slope, but for demo purposes only, it suffices in 2D.
        2. substitute them into equation 1
        3. show again as close up of tangent spaces
    5. second row of J, map red to dh2, then blue to dh2
        1. fill jacobian again, this time for second row
        2. show again as close up of tangent spaces
    6. combine into u (but keep each component and formula)
        1. y = x/2
        2. show again as close up of tangent spaces
    - What function would require a 2x2 jacobian? Give an example
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%202.png)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%203.png)
        
    - Apply to this point (2,3)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%204.png)
        
    - What do we multiply the Jacobian by? For the Jacobian at (2,3), do we multiply again by (2,3)?
    - Calculate what you just said to find a tangent vector in the tangent space of H given a tangent vector in the tangent space of X
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%205.png)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%206.png)
        
    - figs (in visio); overlap with faded x1, x2 axes in davinci
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%207.png)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%208.png)
        
        ![Untitled](Jacobian%20outline%2096c2d1bccc7e41339d6663ad9d922e12/Untitled%209.png)
        
    

Have specific point p = (2,3) and v = (0.3, 0.7), but don’t give specific functions

$\frac{\partial h_1}{\partial x_1} = 2x_1 = 2(2) = 4$

$\frac{\partial h_1}{\partial x_2} = 1$

$\frac{\partial }{\partial h_1}$

$\frac{\partial }{\partial x_2}$

${\color{yellow} J} = \begin{bmatrix}
\color{red}\frac{\partial h_1}{\partial x_1} & \color{blue}\frac{\partial h_1}{\partial x_2} \\
\\
\color{red}\frac{\partial h_2}{\partial x_1} & \color{blue}\frac{\partial h_2}{\partial x_2}
\end{bmatrix}$

$J^{-1} = \begin{bmatrix}
\color{orange}\frac{\partial x_1}{\partial h_1} & \color{green}\frac{\partial x_1}{\partial h_2} \\
\\
\color{orange}\frac{\partial x_2}{\partial h_1} & \color{green}\frac{\partial x_2}{\partial h_2}
\end{bmatrix}$

$\begin{bmatrix}
\frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\\\
\frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} \\\\
\frac{\partial f_3}{\partial x} & \frac{\partial f_3}{\partial y}
\end{bmatrix}$

$h_1(x_1) = {x_1}^2$

$h_1(x_1, x_2) = {x_1}^2 + x_2$

$h_2(x_1, x_2) = {x_1} + x_2$

$\begin{bmatrix}
\color{red}\frac{\partial h_1}{\partial x_1} & \color{blue}\frac{\partial h_1}{\partial x_2} \\
\\
\color{red}\frac{\partial h_2}{\partial x_1} & \color{blue}\frac{\partial h_2}{\partial x_2}
\end{bmatrix}

\begin{bmatrix}
0.3 \\
\\
0.7 \\
\end{bmatrix}$

$Jv = u$

$\begin{bmatrix}
\color{red}\frac{\partial h_1}{\partial x_1} & \color{blue}\frac{\partial h_1}{\partial x_2} \\\\
\color{red}\frac{\partial h_2}{\partial x_1} & \color{blue}\frac{\partial h_2}{\partial x_2}
\end{bmatrix}
\begin{bmatrix}
0.3 \\\\
0.7 \\
\end{bmatrix} = \begin{bmatrix}
0.3 *{\color{red}\frac{\partial h_1}{\partial x_1}} + 0.7*{\color{blue}\frac{\partial h_1}{\partial x_2}} \\\\
0.3*{\color{red}\frac{\partial h_2}{\partial x_1}} + 0.7*{\color{blue}\frac{\partial h_2}{\partial x_2}}
\end{bmatrix}$

- Reasons for (7, 5) instead of (5, 7):
    - Shows v and u in diff directions
    - Shows 2x_1 as derivative first, so not all derivatives are just “1” but an eqn
    
    We want a derivative to get u such that h1 >> h2. This allows us to fit h1 and h1 red blue with more space.
    
    But we also want f2 >> f1.
    
    if f2 = x1 + x2, then f2(p) = 5
    
    if f2 = x1 + x2^2, then f2(p) = 2+9 = 11
    
    J[2nd row] = d/dh2 = (0.3)*1 + (0.7) * (2*3) = 0.3 + 4.5 = 4.8 — too big
    
    Try f2 = 2*x2. Then f2 = 6, d/dh2 = (0.7) * 2 = 1.4
    
    Choose (7, 11) because visually it’s esier to place f(p) higher on the h2-axis