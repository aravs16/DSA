from Graph import Graph
from Vertex import Vertex


def DFS(G):
	for v in G.getAllVertices():
		if v.color == 'WHITE':
			depth_first_search(v)
		print('-'*20)


tm = 0
cycles = False
top_sort = []

def depth_first_search(v):

	global tm
	global cycles
	global top_sort

	v.color = 'GRAY'
	tm = tm+1
	v.d = tm
	print(v.vid,'(',v.d,')',': Discovered')

	adjs = v.getAdjacentVertices()

	for a in adjs:
		""" 
		Topological sort is only possible on a directed 'acyclic' graph
        So check if there are cycles in the graph
        If there is an edge to a discovered but unfinished vertex, it is a back edge => cycle 
        """
		if a.color == 'GRAY':
			cycles = True
			# break if you need to
		if a.color == 'WHITE':
			depth_first_search(a)

	v.color = 'BLACK'
	tm = tm+1
	v.f = tm
	## NOTE: It is always efficient to append to a list than to insert at 0
	## But appending will give us the reverse order of topological sort
	## Or you can use a fixed sized array and start filling it up in the reverse
	## This is possible because we already know the number of vertices
	top_sort.insert(0,v)

	print(v.vid,'(',v.f,')',': Finished')
	


if __name__ == '__main__':

	v1 = Vertex(1)
	v2 = Vertex(2)
	v3 = Vertex(3)
	v4 = Vertex(4)
	v5 = Vertex(5)
	v6 = Vertex(6)
	v7 = Vertex(7)
	v8 = Vertex(8)
	v9 = Vertex(9)

	g = Graph()

	g.addEdge(v1,v2)
	g.addEdge(v1,v3)
	g.addEdge(v2,v4)
	g.addEdge(v3,v5)
	g.addEdge(v4,v6)
	g.addEdge(v5,v6)

	DFS(g)

	print([str(i.vid)+'-->' for i in top_sort],cycles)


