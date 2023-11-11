def left_view(root):
    if root is None:
        return []
    
    result=[]
    max_level=-1
    def left_view_helper(node, level):
        nonlocal max_level
        if not node:
            return None
        if level>max_level:
            result.append(node.key)
            max_level=level
            
        # Recursively traverse the left and right subtrees, incrementing the level.
        left_view_helper(node.left, level + 1)
        left_view_helper(node.right, level + 1)
        
        
    # Start the left view traversal from the root at level 0.
    left_view_helper(root, 0)

    return result