from Graph import Graph
from Vertex import Vertex


def DFS(G):
	for v in G.getAllVertices():
		if v.color == 'WHITE':
			depth_first_search(v)
		print('-'*20)

tm = 0

def depth_first_search(v):

	global tm

	v.color = 'GRAY'
	tm = tm+1
	v.d = tm
	print(v.vid,'(',v.d,')',': Discovered')
	

	adjs = v.getAdjacentVertices()

	for a in adjs:
		if a.color == 'WHITE':
			depth_first_search(a)

	v.color = 'BLACK'
	tm = tm+1
	v.f = tm

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
	g.addEdge(v5,v2)
	g.addEdge(v4,v6)
	g.addEdge(v5,v6)
	
	
	
	# depth_first_search(v1)
	# print('*'*10)
	# depth_first_search(v2)

	DFS(g)

