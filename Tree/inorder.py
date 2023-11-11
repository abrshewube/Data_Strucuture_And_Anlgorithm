class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal(node):
    """
    Perform Inorder Traversal (LNR) of a binary tree.
    
    Parameters:
    - node: The root node of the binary tree.
    """
    if node is not None:
        # Traverse the left subtree
        inorder_traversal(node.left)
        
        # Visit the root (Print or perform an operation)
        print(node.key, end=" ")
        
        # Traverse the right subtree
        inorder_traversal(node.right)

# Example usage:
# Construct a simple binary tree:
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

# Perform Inorder Traversal
print("Inorder Traversal:")
inorder_traversal(root)
