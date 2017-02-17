from Graph import Graph
from Vertex import Vertex
import sys

def add_weights(va1,va2):
	if va1 == sys.maxsize or va2 == sys.maxsize:
		return sys.maxsize
	elif va1 == -1*sys.maxsize or va2 == -1*sys.maxsize:
		return -1*sys.maxsize
	else:
		return va1+va2

def relax_edge(v1,v2):
	# print('Relaxing edges:',v1.vid,'w:',v1.d,' ',v2.vid,'w:',v2.d)
	# print(add_weights(v1.d, v1.getEdgeWeight(v2)))
	if v2.d > add_weights(v1.d, v1.getEdgeWeight(v2)):
		v2.d = add_weights(v1.d, v1.getEdgeWeight(v2))
		v2.parent = v1
	# print('Relaxed weights:',v1.d,v2.d)

def initialize_(G,start):
	for v in G.getAllVertices():
		v.parent = None
		v.d = sys.maxsize

	start.d = 0

def bellman_ford(G,v):

	initialize_(G,v)
	status = 1

	vertices = G.getAllVertices()
	lv = len(vertices)

	for i in range(1,lv-1):
		for vr in vertices:
			for e in vr.getAdjacentVertices():
				# print(vr.vid,' > ',e.vid,'=>',e.d)
				relax_edge(vr,e)

	for i in range(1,lv-1):
		for vr in vertices:
			for e in vr.getAdjacentVertices():
				if e.d > add_weights(vr.d,vr.getEdgeWeight(e)):
					e.d = -1*sys.maxsize
					print('FAILED: NEGATIVE CYCLE')
					status = -1
					
	return status

def find_path(s,v):
	
	if s.vid == v.vid:
		print(s.vid,'*****')
		return s
	elif v == None:
		return -1
	elif v.parent == None:
		return -1
	else:
		print(v.vid,'*****')
		return find_path(s,v.parent)

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
	g.addEdge(v4,v5,-1)
	g.addEdge(v5,v6,-1)
	g.addEdge(v6,v4,-1)

	status = bellman_ford(g,v1)
	if status != -1:
		i = find_path(v1,v4)
	for v in g.getAllVertices():
		print(v.vid,'=>',v.d)
	





