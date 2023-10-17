# Valid Anagram

Prob: find if two strings are anagrams

Soln: count each character frequency. If same frequency, they're anagrams

<<<

GENR: Counts → Use hashmap

Compare counts → Compare hashmaps

Prob: [Check if two sequences are combinations of each other](https://www.notion.so/Check-if-two-sequences-are-combinations-of-each-other-54e7449c27464c4792215aa42bb6324c?pvs=21) 

Soln: count each character frequency. If same frequency, they are

<<<

GENR ISSUE: Python- Obtain value of hashmap, but not sure if it’s there, and don’t want error

SOLN: hashmap.get(key, V) will return V if key not there

<<<

GENR: If there’s a condition where you don’t need to check the entire structure to know it’s False, check this condition sometime before checking the entire structure

Eg) To check if anagram:

for c in hashmap_1:  # check the counts of 2 hashmaps equal

if hashmap_1[c] ! = hashmap_2.get(c, 0): #but they must have exact same keys

return False

<<<

STM: Sort takes O(n) memory, but O(1) is optimized