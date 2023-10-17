# G- During certain recursions, add up each case in the return

Eg) In “****Count Good Nodes in a Binary Tree”,**** each node adds +=1 if it’s good. It only NEEDS TO RETURN 1 because the function calling it will add 1 to its sum variable. It doesn’t need to sum into a record variable that’s being passed down to each case.

Remember to update the values before going into the recursive cases