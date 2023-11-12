class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    """
    Find the diameter of a binary tree.

    Parameters:
    - root: The root node of the binary tree.

    Returns:
    - int: The diameter of the binary tree.
    """
    def height_and_diameter(node):
        """
        Helper function to calculate the height and diameter of a subtree.

        Parameters:
        - node: The current node in the recursion.

        Returns:
        - Tuple: A tuple containing the height and diameter of the subtree.
        """
        if not node:
            return 0, 0

        # Recursively calculate the height and diameter of the left subtree
        left_height, left_diameter = height_and_diameter(node.left)

        # Recursively calculate the height and diameter of the right subtree
        right_height, right_diameter = height_and_diameter(node.right)

        # The height of the current subtree is the maximum of the left and right subtree heights, plus 1
        current_height = max(left_height, right_height) + 1

        # The diameter of the current subtree is the maximum of three values:
        # 1. Diameter of the left subtree
        # 2. Diameter of the right subtree
        # 3. The sum of the heights of the left and right subtrees
        current_diameter = max(left_diameter, right_diameter, left_height + right_height)

        return current_height, current_diameter

    # Call the helper function to get the height and diameter of the entire tree
    _, tree_diameter = height_and_diameter(root)

    return tree_diameter

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

# Find the diameter of the binary tree
tree_diameter = diameter_of_binary_tree(root)

# Print the result
print("Diameter of the binary tree:", tree_diameter)
