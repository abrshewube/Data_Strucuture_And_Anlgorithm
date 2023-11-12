class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def max_depth(root):
    if not root:
        return 0
    left_depth=max_depth(root.left)
    right_depth=max_depth(root.right)
    
    return max(left_depth,right_depth)+1

# Example usage:
# Construct a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Find the maximum depth of the binary tree
tree_depth = max_depth(root)

# Print the result
print("Maximum Depth of the binary tree:", tree_depth)
    
    
    