# Numpy

[https://numpy.org/doc/stable/reference/arrays.html](https://numpy.org/doc/stable/reference/arrays.html)

- [https://www.hackerrank.com/challenges/np-arrays/problem](https://www.hackerrank.com/challenges/np-arrays/problem)
    
    ```python
    import numpy
    
    def arrays(arr):
        # complete this function
        # use numpy.array
        arr = numpy.flip(arr)  # need to store flip
        return numpy.array(arr, float) # return as numpy not lst
    
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)
    ```
    
-