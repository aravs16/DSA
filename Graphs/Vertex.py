class Vertex:

	def __init__(self,vid):
		self.vid = vid
		self.connectedTo = {}
		self.color = 'WHITE'
		self.parent = None
		self.d = 0
		self.heap_idx = None # For use in priority queues

	def addEdge(self,V,w=None):
		self.connectedTo[V] = w

	def getAdjacentVertices(self):
		return self.connectedTo.keys()

	def getEdgeWeight(self,V):
		return self.connectedTo[V]