def top_view(root):
    if not root:
        return []
    result=[]
    
    top_dic={}
    def top_helper(node,level,distance):
        nonlocal top_dic
        
        if distance not in top_dic or level<top_dic[distance][0]:
            top_dic[distance]=(level,node.key)
        
        top_helper(node.left,level+1,distance-1)
        top_helper(node.right,level+1,distance-1)
    top_helper(root,0,0)
    sorted_top_view = sorted(top_dic.items(), key=lambda x: x[0])
    result = [value[1] for value in sorted_top_view]

    return result