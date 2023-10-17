# GP- To avoid nested loops, add separate loops

Instead of a nested loop, use two sep loops to eval everything first

When comparing elements of arrays or the same array, to avoid nested loops, add separate loops. When you compare an element with every other element, that’s O(n^2) because of a nested loop. 

Eg) This means using a loop outside first to get the max first, then compare each element in the array with the max. This avoids comparing each element with every other element to find the max again (redundant)

More specific:

[GP- use two sep loops for before i and after i](GP-%20use%20two%20sep%20loops%20for%20before%20i%20and%20after%20i%2032dec152a93a4bd780df5798ecbbc158.md)