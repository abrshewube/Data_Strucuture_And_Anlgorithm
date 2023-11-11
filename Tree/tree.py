import sys
sys.setrecursionlimit(10**6)

#A binary tree is a hierarchical data structure composed of nodes,
# where each node has at most two children, which are referred to as 
# the left child and the right child. The topmost node in a tree is called the root.

# 1 . Binary Tree Node declaration using Manual (Node declaration)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Manual construction of a binary tree:
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

   
    
    
    
# 2 From a Sorted Array:
#If you have a sorted array, you can construct a binary search tree (BST)
# by recursively choosing the middle element as the root.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    
def sorted_array_to_bst(arr, start, end):
    if start>end:
        return None
    
    mid=start+end//2
    root=Node(arr[mid])  
    root.left=sorted_array_to_bst(arr,start,mid+1) 
    root.right=sorted_array_to_bst(arr,mid+1,end)
    
    
    return root

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.key, end=' ')
    inorder(node.right)

# Example usage:
sorted_array = [1, 2, 3, 4, 5]
root = sorted_array_to_bst(sorted_array, 0, len(sorted_array) - 1)

# Perform inorder traversal and print the values
inorder(root)



#3. From Traversals:
#If you have the inorder and preorder (or postorder) 
# traversals of a tree, you can construct the tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None
    root_value=preorder.pop(0)
    root=Node(root_value)
    inorder_index=inorder.index(root_value)
    
    root.left=build_tree(inorder[:inorder_index],preorder)
    root.right=build_tree(inorder[inorder_index+1:],preorder)
    return root

# Example usage:
inorder_seq = [4, 2, 5, 1, 3]
preorder_seq = [1, 2, 4, 5, 3]
root = build_tree(inorder_seq, preorder_seq)






