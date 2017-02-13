from Graph import Graph
from Vertex import Vertex


def breadth_first_search(v):

	q = [v]

	while len(q)>0:

		curr = q.pop(0)
		print(curr.vid,'(',curr.d,')')
		adjs = curr.getAdjacentVertices()
		lev = []
		for a in adjs:
			if a.color == 'WHITE':
				lev.append(a)
				a.color = 'GRAY'
				a.parent = curr
				q.append(a)
				a.d = curr.d +1
		curr.color = 'BLACK'


def print_path(G,s,v):
    
    if v.vid == s.vid:
    	print(s.vid)
    elif v.parent == None:
    	print('No Path Exists')
    else:
    	print(v.vid)
    	print_path(G,s,v.parent)



if __name__ == '__main__':

	v1 = Vertex(1)
	v2 = Vertex(2)
	v3 = Vertex(3)
	v4 = Vertex(4)
	v5 = Vertex(5)
	v6 = Vertex(6)

	g = Graph()
	g.addEdge(v1,v2)
	g.addEdge(v1,v3)
	g.addEdge(v2,v4)
	g.addEdge(v3,v5)
	g.addEdge(v4,v6)
	g.addEdge(v5,v6)

	breadth_first_search(v1)
	print_path(g,v1,v5)



