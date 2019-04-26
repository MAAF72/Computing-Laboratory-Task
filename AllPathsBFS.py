#BFS -> Queue
from collections import defaultdict 
   
class Graph: 
   
    def __init__(Self, Vertex) : 
        Self.V = Vertex  
        Self.Graph = defaultdict(list)
		
def AddEdge(G, Source, Destination) :
	G.Graph[Source].append(Destination)
	
def PrintAllPaths(G, Source, Destination) :
	Queue = []
	Path = []
	Path.append(Source)
	Queue.append(Path)
	while Queue :
		#print("=============")
		#print("Current Queue : {}".format(Queue))
		Path = Queue[0].copy()
		Queue.pop(0)
		#print("Current Path : {}".format(Path))
		Last = Path[len(Path) - 1]
		if Last == Destination :
			print(Path)
		
		#print("Neighbor of {} is {}".format(Last, G.Graph[Last]))
		for i in G.Graph[Last] :
			#print("Visiting : {}".format(i))
			#print("Old Path : {}".format(Path))
			if i not in Path : 
				NewPath = Path.copy() #Kalau gak make copy, jika NewPath diubah, maka Path juga keubah malah kayak pointer
				#https://www.programiz.com/python-programming/methods/list/copy
				NewPath.append(i)
				#print("Get a new path : {}".format(NewPath))
				Queue.append(NewPath)

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