# Preorder  traversal

#  Node declaration

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    
def preorder(node):
    if node is not None:
        # vist the node for the root
        print(node.key,end="")
        
        # traverse the left tree
        
        preorder(node.left)
        
        preorder(node.right)
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform Preorder Traversal
print("Preorder Traversal:")
preorder(root)     
       
        
        
        
        
        
     