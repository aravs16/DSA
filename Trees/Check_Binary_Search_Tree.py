class Node:

	def __init__(self,data):

		self.left = None
		self.right = None
		self.data = data
		self.parent = None

	def insertLeft(self,node):
		self.left = node
		self.left.parent = self

	def insertRight(self,node):
		self.right = node
		self.right.parent = self


""" 

Solution: 
Idea is that Inorder traversal of a Binary Search Tree always gives a sorted order.
So we do an inorder traversal of the tree keeping track of the last visited node and check if the current node is greater than last visited node.

"""

curr = -999999
def checkBST(node):

	global curr

	if node:

		if checkBST(node.left):
			if node.data > curr:
				curr = node.data
				return checkBST(node.right)
			else:
				return False

		else: return False

	else:
		return True


if __name__ == '__main__':

	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)
	n7 = Node(7)
	n8 = Node(8)
	n9 = Node(9)
	

	n5.insertLeft(n3)
	n5.insertRight(n7)
	n3.insertLeft(n2)
	n3.insertRight(n6)
	n7.insertLeft(n1)
	n7.insertRight(n9)

	print(checkBST(n5))