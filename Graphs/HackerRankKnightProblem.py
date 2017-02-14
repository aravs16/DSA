#!/bin/python3
#https://www.hackerrank.com/contests/rookierank-2/challenges/knightl-on-chessboard
class Graph:

	def __init__(self):
		self.vertList = {}

	def addVertex(self,vertex):
		self.vertList[vertex.id] = vertex

	def addEdge(self,V1,V2,w=None):
		
		if V1.vid not in self.vertList.keys():
			self.vertList[V1.vid] = V1
		if V2.vid not in self.vertList.keys():
			self.vertList[V2.vid] = V2
		vv1 = self.vertList[V1.vid]
		vv2 = self.vertList[V2.vid]
		vv1.addEdge(vv2,w)

	def getAllVertices(self):
		return self.vertList.values()

class Vertex:

	def __init__(self,vid):
		self.vid = vid
		self.connectedTo = {}
		self.color = 'WHITE'
		self.parent = None
		self.d = 0

	def addEdge(self,V,w=None):
		self.connectedTo[V] = w

	def getAdjacentVertices(self):
		return self.connectedTo.keys()

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

numMoves = 0
def print_path(s,v):
	global numMoves
	if v == s:
		return numMoves
	elif v.parent == None:
		# print('No path exists')
		return -1
	else:
		numMoves += 1
		return print_path(s,v.parent)


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
			p = p+1
			v = Vertex(str(x)+','+str(y))
			nm = genMoves(x,y,a,b,n)

			for nmm in nm:
				if nmm not in moveTuples:
					moveTuples.append(nmm)
					g.addEdge(v,Vertex(str(nmm[0])+','+str(nmm[1])))
			
	return g	



n = int(input().strip())
start = None
end = None


for i in range(1,n):
    vals = []
    for j in range(1,n):
        numMoves = 0
        g = KnightMoves(i,j,n)
        for k in g.getAllVertices():
        	if k.vid == '0,0':
        		start = k
        	elif k.vid == str(n-1)+','+str(n-1):
        		end = k
        bread_first_search(start)
        vals.append(print_path(start,end))
    print(' '.join([str(x) for x in vals]))
        

        
        