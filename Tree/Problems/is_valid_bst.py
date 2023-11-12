class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def is_valid_Bst(root):
    """
    Check if a given binary tree is a valid Binary Search Tree (BST).

    Parameters:
    - root: The root node of the binary tree.

    Returns:
    - bool: True if the tree is a valid BST, False otherwise.
    """
    
    def helper(node,min_val=float("-inf"),max_value=float("inf")):
        """
        Helper function for recursive BST validation.

        Parameters:
        - node: The current node in the validation.
        - min_val: The minimum allowed value for the current node.
        - max_val: The maximum allowed value for the current node.

        Returns:
        - bool: True if the subtree rooted at 'node' is a valid BST, False otherwise.
        """
        
        if not node:
            return None
        
        # Check if the current node's value is within the allowed range
        if not(min_val<node.key<max_value):
            return False
         # Recursively check the left and right subtrees with updated ranges
        return(helper(node.left,min_val,node.key) and is_valid_Bst(node.right,node.key,max_value))
    return helper(root)

