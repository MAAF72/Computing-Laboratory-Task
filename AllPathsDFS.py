#DFS -> Stack   
from collections import defaultdict 
   
class Graph: 
   
    def __init__(Self, Vertex) : 
        Self.V = Vertex  
        Self.Graph = defaultdict(list)
		
def AddEdge(G, Source, Destination) :
	G.Graph[Source].append(Destination)
	
def FindPath(G, Source, Destination, Visited, Path) :
	Visited[Source] = True
	Path.append(Source)
	
	if Source == Destination :
		print(Path)
	else :
		for i in G.Graph[Source] :
			if not Visited[i] :
				FindPath(G, i, Destination, Visited, Path)
				
	Path.pop() #Pop last element from Path alias Pop Source from Path
	Visited[Source] = False
	
def PrintAllPaths(G, Source, Destination) :
	Visited = [False]*(G.V)
	
	Path = []
	
	FindPath(G, Source, Destination, Visited, Path)
	
G = Graph(4) 
AddEdge(G, 0, 1) 
AddEdge(G, 0, 2) 
AddEdge(G, 0, 3) 
AddEdge(G, 2, 0) 
AddEdge(G, 2, 1) 
AddEdge(G, 1, 3) 
   
Source = 2
Destination = 3
print("All different paths from {} to {} :".format(Source, Destination))
PrintAllPaths(G, Source, Destination)