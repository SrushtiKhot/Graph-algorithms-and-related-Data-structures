
from datetime import datetime

class strongly_connected_comps:
   
    def __init__(self, no_of_vertices):  #reads count of vertices from input text file specified
        self.vertex = no_of_vertices
        self.adj_list_graph = [[] for i in range(no_of_vertices)]
	
    def readfile(self,txtfile):  #reads input file from user 
        file1=open(txtfile)
        next(file1)
        for f in file1:
            s=f.split()
            u=int(s[0])
            v=int(s[1])
            self.adj_list_graph[u].append(v)

#Adjacent list of the graph is computed		
    def vertex_order(self, g, traversed):
        traversed[g] = True
        alg=self.adj_list_graph[g]
        for u in alg:
            if not traversed[u]: self.vertex_order(u, traversed)
        self.H.append(g)
  
    #Transpose of initial graph provided in input file
    def transpose_of_graph(self):
        vert=strongly_connected_comps(self.vertex)
        Grev = vert
        v=self.vertex
        for i in range(v):
            for u in self.adj_list_graph[i]: Grev.adj_list_graph[u].append(i)
        return Grev
   
    #Depth first search is performed on  graph
    def depth_first(self, traversed, g):
        traversed[g] = True
        print(f'{g} ', end = "")
        alg2=self.adj_list_graph[g]
        for u in alg2:
            if not traversed[u]: self.depth_first(traversed, u)
	  
#SFinding strongly connected components
    def Strongly_ccomps(self):
        traversed = [False]*self.vertex
        self.H = []
        for i in range(self.vertex):
            if not traversed[i]:
                self.vertex_order(i, traversed)
        for i in range(self.vertex): traversed[i] = False
        Grev = self.transpose_of_graph()
        
        while len(self.H) > 0:
            v = self.H.pop()
            if not traversed[v]:
                Grev.depth_first(traversed, v)
                print()
                
txt=input("Please enter the filename you want to choose\n")
f1=open(txt)
vertices=(int)(f1.readline())	 
f1.close()  
start_time_1= datetime.now()
Grev = strongly_connected_comps(vertices)
Grev.readfile(txt)
Grev.Strongly_ccomps()
end_time_1 = datetime.now()
print('Duration: {}'.format(end_time_1 - start_time_1))