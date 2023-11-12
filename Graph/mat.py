class Graph:
    def __init__(self,vertice) :
        self.vertice=vertice
        self.graph=[]
        
    def add_edge(self,u,v,w):
        self.graph.append((u,v,w))
        
    def find_parent(self,parent,i):
        if parent[i]==i:
            return i
        return self.find_parent(parent,parent[i])
    
        