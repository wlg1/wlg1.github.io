# GP- Check if all elements in array are UNIQUE in O(n)

If we compare each element with all other elements, that’s O(n^2). So instead, use sets:

`len(counts.values()) == len(list(set(counts.values())))`

[G- unique → set](G-%20unique%20%E2%86%92%20set%20abaa66d957f24458905fffee9595ac7f.md) 

Related to:

[GP- Find different DISTINCT elements of 2 arrays](GP-%20Find%20different%20DISTINCT%20elements%20of%202%20arrays%20bf70d5c4a39746cf9cf56b77826ffada.md)