import time
from Graph import Graph
from Vertex import Vertex

def bread_first_search(v):

	q = [v]

	while len(q) > 0:
		curr = q.pop(0)
	
		for a in curr.getAdjacentVertices():
			if a.color == 'WHITE':
				a.color = 'GRAY'
				q.append(a)
				a.parent = curr
				a.d = curr.d+1
		a.color = 'BLACK'

def print_path(s,v):
	if v == s:
		print(v.vid)
	elif v.parent == None:
		print('No path exists')
	else:
		print(v.vid)
		print_path(s,v.parent)


def isWithinRange(x,y,n):
	if x < n and y < n and x >= 0 and y >= 0:
		return True
	return False

def genMoves(x,y,a,b,n):

	newMoves = []
	offsets = [[a,b],[b,a],[-a,-b],[-b,-a],[-a,b],[a,-b],[-b,a],[b,-a]]
	for o in offsets:
		nx = x+o[0]
		ny = y+o[1]
		print('>>',nx,ny,'<<<')
		if isWithinRange(nx,ny,n):
			newMoves.append([nx,ny])

	return newMoves

def KnightMoves(a,b,n):

	p = 0

	moveTuples = [[0,0]]
	g = Graph()

	while len(moveTuples) > 0:

		new = moveTuples[p:]
		if len(new) == 0:
			break;
		for x,y in new:
			print('From',x,y)
			p = p+1
			v = Vertex(str(x)+','+str(y))
			nm = genMoves(x,y,a,b,n)
			print('Possible Moves',nm)
			for nmm in nm:
				if nmm not in moveTuples:
					moveTuples.append(nmm)
					g.addEdge(v,Vertex(str(nmm[0])+','+str(nmm[1])))
			
	return g		

if __name__ == '__main__':

	g = KnightMoves(1,4,5)
	start = None
	end = None
	for i in g.getAllVertices():
		if i.vid == '0,0':
			start = i
			bread_first_search(i)
		if i.vid == '4,4':
			end = i

	print_path(start,end)

	








