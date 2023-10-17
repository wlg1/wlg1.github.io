# 238. Product of Array Except Self

Two loops:

The first is for the product of all elements BEFORE index i

The second is for the product of all elements AFTER index i

Remember to start at different indices (2nd and 2nd last) 

When looping: 

- 2nd last is len(nums)-2 because len(nums)-1 is LAST ind
- Remember, reverse range takes THREE ARGS (-1 is last)
- End at the index that’s NOT being evaluated

[GP- To avoid nested loops, add separate loops](GP-%20To%20avoid%20nested%20loops,%20add%20separate%20loops%2082da24b9d22149cfbd5982d5082f6e06.md) 

[GP- use two sep loops for before i and after i](GP-%20use%20two%20sep%20loops%20for%20before%20i%20and%20after%20i%2032dec152a93a4bd780df5798ecbbc158.md)