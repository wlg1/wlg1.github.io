# 1071. Greatest Common Divisor of Strings

[https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3124997/super-easy-solution-fully-explained-c-python3-java/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3124997/super-easy-solution-fully-explained-c-python3-java/?envType=study-plan-v2&envId=leetcode-75)

The brute force solution is to compare the substring with the rest of each string. However, the KEY trick is to realize that the GCD of the number sequence is ANALOGOUS to the GCD of the strings!

That is, once we use a math operation to find GCD, we just need to get str[0:gcd] and str2[0:gcd] and check if they’re equal.

Two strings with a common numerical gcd doesn’t mean they have the same string at those gcd, so further checks are needed

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = (math.gcd(len(str1), len(str2)))
        if gcd == 0:
            return ""
        for test_str in [str1, str2]:
            if len(test_str) % gcd != 0:
                return ""
            k = int(len(test_str) / gcd)
            for i in range(k):
                if str1[:gcd] != test_str[(i*gcd):(i+1)*gcd]:
                    return ""
        return str1[:gcd]
```

NOTE: Do the above check using a sliding window over each string because need to check whole string, for both strings, has the pattern. Cannot just do:

```
if str1[:gcd] != str2[:gcd]:
            return ""
```

---

Attempts:

- brute force
    
    ```python
    class Solution:
        def gcdOfStrings(self, str1: str, str2: str) -> str:
            # one of the strings must be a divisor of the other string
            # we cannot have a string have chars not part of divisor, else divisor wouldn't divide it
            # the divisor will thus always start at the first char, so we only need to change the end of the substring window
            if len(str1) > len(str2):
                loopStr = str2
                longerStr = str1
            else:
                loopStr = str1
                longerStr = str2
    
            # brute force:
            # check if substring matches next window of string, keep on checking if matches remaining windows. if it matches all of them, then it's a divisor
            GCD_str = ""
            for i in range(0, len(loopStr)):
                substr = loopStr[0:i+1]  #0:3
                # the str len of both strings must be a multiple of the divisor
                if (len(str1) % len(substr) == 0) & (len(str2) % len(substr) == 0):
                    k = int(len(loopStr) / len(substr))
                    isDivisor = True
                    for j in range(2, k):
                        if substr != loopStr[i+1: j*i]:  #3:6
                            isDivisor = False
                            break
                    if isDivisor:
                        GCD_str = substr
                else:
                    continue
    
            if GCD_str:
                if (len(longerStr) % len(GCD_str) == 0):
                    k = int(len(longerStr) / len(GCD_str))
                    for j in range(0, k):
                        if GCD_str != longerStr[j*len(GCD_str): (j+1)*len(GCD_str)]:  #3:6
                            return ""
                else:
                    return ""
    
            return GCD_str
    ```