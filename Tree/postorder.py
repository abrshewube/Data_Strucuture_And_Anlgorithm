# postorder  traversal

class Node:
    def __init__(self,key) :
        self.key=key
        self.left=None
        self.right=None
    
    
def post_traveral(node):
    if node is not None:
        post_traveral(node.left)
        post_traveral(node.right)
        print(node.key,end=",")
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform Postorder Traversal
print("Postorder Traversal:")
post_traveral(root)