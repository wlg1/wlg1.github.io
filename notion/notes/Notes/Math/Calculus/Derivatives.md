# Derivatives

[Derivative formulas through geometry | Chapter 3, Essence of calculus](https://youtu.be/S0_qX4VJhMQ)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%201.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%202.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%203.png)

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%204.png)

- df vs d(1/x) ? avoid this fallacy.
    
    ${x * d(\frac{1}{x})}$
    
    ${dx * (\frac{1}{x})}$
    
    $$
    df = x * d(\frac{1}{x}) + dx * (\frac{1}{x})
    $$
    
    This is a fallacy that mixes up adding squares geometrically with the Cartesian coordinate representation of the function. The square example above is NOT on the Cartesian coordinate. Thus, we cannot add squares on the Cartesian coordinate to get Df like we did for the geometric no coordinate representation. Instead we just examine the vertical y-axis. 
    

$$
d(\frac{1}{x}) = \frac{1}{(x + dx)} - \frac{1}{x} = \frac{x}{(x + dx)*x} - \frac{x+dx}{x*(x+dx)} = 
$$

$$
= \frac{x - (x + dx)}{(x + dx)*x} = \frac{- dx}{x^2 + dx*x} = \frac{- 1}{x^2} dx
$$

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

### [Polar Coordinates:](../Trigonometry%20b26a4065a8ea4ce28cbea6bb4c3ab69a/Polar%20Coordinates%209b869db478544856aec499c96898eb27.md)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%205.png)

sin is the height. As the arc length changes, the height goes up 

The highest, sin = 1, is at theta = pi/2 = 90 degrees

The lowest, sin = -1, is at theta = -pi/2) = 270 degrees

In polar coordinates above, this is a circle because we only plot by (r, theta), despite theta at pi/2 and at -pi/2 having the same y-value. 

- In polar coordinates, why can there be a circle? I thought functions cannot have the same x coordinate be sent to 2 different y coordiantes? So x=0 has two y-coordinates (r and -r)?
    
    In polar coords, each point on the circle can be uniquely identified by its radial distance and angle, (r, θ), and the equation r = constant does not represent a function in the sense that there is not a unique output for each input. Instead, it represents a curve in the polar plane, and each point on the curve has a unique pair of polar coordinates (r, θ).
    
    Thus, the “domain” is (r, θ), and the “image” is the point p(r, θ). This function p() does not violate function properties where adomain point can only be sent to one image point.
    
    This is why defining a function isn’t always by looking geometrically at the cartesian coordinates with the “vertical line test”; one should refer to the definition of what is in the domain and image, and see if the domain points are sent to unique image points.
    

### ${f(\theta)} = {y = r * sin(\theta) = sin(\theta)}$:

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%206.png)

<<<

Green triangles are [similar](../Trigonometry%20b26a4065a8ea4ce28cbea6bb4c3ab69a/Similar%20Triangles%20a6464122a42248d49080c68d07aea0bc.md). Thus, the same theta used to define polar coordinates is the angle between d(sin(th)) and d(th).

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%207.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%208.png)

---

[**Visualizing the chain rule and product rule | Chapter 4, Essence of calculus**](https://www.youtube.com/watch?v=YG15m2VwSjA&t=184s&ab_channel=3Blue1Brown)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%209.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%2010.png)

### Product Rule

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%2011.png)

### Chain Rule

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%2012.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%2013.png)

![Untitled](Derivatives%204fee928e4d25473692d694d69b5545c0/Untitled%2014.png)