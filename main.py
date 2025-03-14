def sum_of_depths(node):
    def dfs(node, depth = 0):
        if node is None:
            return 0
        
        lvalue = dfs(node.left, depth + 1)
        rvalue = dfs(node.right, depth + 1)
        return max(lvalue, rvalue) + depth
    
    return dfs(node)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9

    print(sum_of_depths(n1))