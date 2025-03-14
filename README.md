# Sums depths of a binary tree.
Calculate sum of depths of a given binary tree. Suppose a deepest node of a binary tree is at level 4, staring level is 0. Algorithm should return 0 + 1 + 2 + 3 + 4 = 10.

Input:
Following binary tree is given.

        1           -> level 0
     /     \
    2       3       -> level 1  
   / \     / \ 
  4   5   6   7     -> level 2
 / \
8   9               -> level 3 

Output:
0 + 1 + 2 + 3 = 6

## Solution:
Termination condition of the dfs is when a node is None. Terminated node should return 0. Since it doesn't alter addition. Upper levels should add their level to the returned sum (choose max one).

        1  return 6 + 0
     /     \
    2       3  return 5 + 1
   / \     / \ 
  4   5   6   7  return 2 + 3
 / \     returns 3 + 0
8   9    depth = 3, depth + max(ret_values_of_child_nodes) 
|   |  returns 0
0   0  depth = 4
