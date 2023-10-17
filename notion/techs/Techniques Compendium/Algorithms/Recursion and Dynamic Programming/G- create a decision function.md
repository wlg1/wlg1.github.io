# G- create a decision function

Each node in tree can have branching decision VALUES

G- VALUE at node = max(VALUE of decision 1, VALUE of decision 2)

Eg) The value adds by node, so it will add values of other nodes to get the value of a decision

The recursive function usually outputs the value. So the value is a recursive function, and the values of its decisions use the recursive function again.

Fill in this equation using the following info:

1. Describe ideas on how to obtain the recursive function’s output value. 
    1. What is its key type VS its value type? # concretely defines what value type you need to output. key type is the sub-problem type. each sub-problem has an “optimum value”.
    2. How does it output the value by obtaining values from sub-problems
    3. What are axiomatic base cases that provides the first return?
    4. Separate out what is put into output from current level, VS what is put into output from recursive levels [the sub-problems]
        
        Eg) rob(i) = arr[i] + sub-problem_solns
        
        Eg) rob(i) = arr[i] + rob(arr[i+2:n])  # fill in later on once define subprob
        
2. What are the sub-problems “vaguely described in general”?
    
    Eg) a sub-array of houses valid to rob from current decision node
    
3. What are the branching decisions that use the sub-problems?
    1. Find by creating a branching decision tree

Often, you go back and forth among the 3 steps to refine your definitions; it’s not sequential completion.