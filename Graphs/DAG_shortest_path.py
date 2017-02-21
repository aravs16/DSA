from Graph import Graph
from Vertex import Vertex
import sys


time = 0
top_sort = []

def add_weights(va1,va2):
	if va1 == sys.maxsize or va2 == sys.maxsize:
		return sys.maxsize
	elif va1 == -1*sys.maxsize or va2 == -1*sys.maxsize:
		return -1*sys.maxsize
	else:
		return va1+va2

def DFS_top_sort(G,v):

	global time
	time = time+1
	v.color = 'GRAY'
	v.d = time
	for vs in v.getAdjacentVertices():
		if vs.color == 'WHITE':
			DFS_top_sort(G,vs)
	v.color = 'BLACK'
	time = time+1
	v.f = time
	top_sort.insert(0,v)


def initialize_v():

	global top_sort
	for v in top_sort:
		v.parent = None
		v.d = sys.maxsize
	top_sort[0].d = 0


def relax_edge(v1,v2):

	if v2.d > add_weights(v1.d, v1.getEdgeWeight(v2)):
		v2.parent = v1
		v2.d = add_weights(v1.d, v1.getEdgeWeight(v2))


def dag_shortest_path(G,v):

	DFS_top_sort(G,v)
	print('After Topological Sort')

	for i in top_sort:
		print(i.vid,'>',i.d,'>',i.f)

	initialize_v()
	print('After initialize()')
	for i in top_sort:
		print(i.vid,'>',i.d,i.parent)

	for v in top_sort:
		for va in v.getAdjacentVertices():
			relax_edge(v,va)

	print('After relaxing all')

	for v in top_sort[1:]:
		print(v.vid,'>',v.d,'>',v.parent.vid)

def find_path(start,end):

	if start == end:
		print(start.vid)
		return 1
	elif end.parent == None:
		print('No path exists')
		return -1
	else:
		print(end.vid)
		return find_path(start,end.parent)

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
	g.addEdge(v1,v2,1)
	g.addEdge(v1,v3,2)
	g.addEdge(v2,v4,3)
	g.addEdge(v3,v4,3)

	dag_shortest_path(g,v1)
	find_path(v1,v4)
	


