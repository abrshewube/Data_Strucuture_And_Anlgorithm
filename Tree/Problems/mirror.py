class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def mirror_binary_tree(root):
    """
    Mirror or invert a binary tree.

    Parameters:
    - root: The root node of the binary tree.

    Returns:
    - Node: The root of the mirrored binary tree.
    """
    if not root:
        return None

    # Recursively mirror the left and right subtrees
    mirrored_left = mirror_binary_tree(root.right)
    mirrored_right = mirror_binary_tree(root.left)

    # Swap the left and right children
    root.left, root.right = mirrored_left, mirrored_right

    return root

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

# Mirror the binary tree
mirrored_root = mirror_binary_tree(root)

# Function to print the tree in-order for verification
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

# Print the original and mirrored trees for verification
print("Original tree (in-order):")
inorder_traversal(root)
print("\nMirrored tree (in-order):")
inorder_traversal(mirrored_root)
