class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def lowest_common_ancestor(root, node1, node2):
    if not root:
        return None
    if root==node1 and root==node2:
        return root
        
    left_lca=lowest_common_ancestor(root.left,node1,node2)
    right_lca=lowest_common_ancestor(root.right,node1,node2)
    
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca
    
    
    