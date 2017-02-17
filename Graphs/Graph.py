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
		# print(vv1.vid,'>',[i.vid for i in vv1.getAdjacentVertices()])
		# print(V1.vid,'>',[i.vid for i in V1.getAdjacentVertices()])
		# V2.addEdge(V1,w)

	def getAllVertices(self):
		return self.vertList.values()

	def getVertex(self,vid):
		for v in self.getAllVertices():
			if v.vid == vid:
				return v