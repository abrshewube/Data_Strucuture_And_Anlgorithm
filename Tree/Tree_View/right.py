class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        

def rightview(root):
    if not root:
        return  []
    result=[]
    max_level=-1
    
    def right_view_helper(node,level):
        nonlocal max_level
        if not node:
            return
        if level>max_level:
            result.append(node.key)
            max_level=level
        right_view_helper(node.right,level+1)
        right_view_helper(node.left,level+1)

    right_view_helper(root, 0)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Get the right view of the binary tree
result = rightview(root)

# Print the result
print("Right View:", result  )          
            
        
        