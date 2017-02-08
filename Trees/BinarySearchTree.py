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

	def numChildren(self):
		if self.left == None  and self.right == None:
			return 0
		elif self.left == None or self.right == None:
			return 1
		else: return 2



def insertBST(head,node):

	if node.data > head.data and head.right == None:
		head.insertRight(node)
	elif node.data < head.data and head.left == None:
		head.insertLeft(node)
	elif node.data < head.data:
		insertBST(head.left,node)
	else:
		insertBST(head.right,node)

def inOrder(node):

	if node:
		inOrder(node.left)
		print(node.data)
		inOrder(node.right)


# Find height of the BST
def findH(node):

	if node:
		return 1+max(findH(node.left),findH(node.right))
	else:
		return 0

def printLeaves(node):

	if node:
		if node.left == None and node.right == None:
			print(node.data)
		else:
			printLeaves(node.left)
			printLeaves(node.right)



def searchBST(head,data):

	if not head:
		return 

	if head.data == data:
		print('Found')
	elif data > head.data:
		searchBST(head.right,data)
	else:
		searchBST(head.left,data)


def levelOrderTraversal(node):

	q = [node]

	while len(q) > 0:
		curr = q[0]
		print(curr.data)
		if curr.left != None:
			q.append(curr.left)
		if curr.right != None:
			q.append(curr.right)
		q.pop(0)


def printLevelOrder(node):

	q = [node]

	while len(q) > 0:
		
		lev = ''

		for i in q:
			if i.left != None:
				lev = lev+' ('+str(i.left.data)+')'
			lev = lev+''+str(i.data)
			if i.right != None:
				lev = lev + '(' + str(i.right.data) +') '
		print(lev)

		qt = q[:]

		for i in qt:
			if i.left != None:
				q.append(i.left)
			if i.right != None:
				q.append(i.right)
			q.pop(0)



def findLowestInRight(node):

	if node:
		if node.left == None:
			return node
		else:
			findLowestInRight(node.left)

def numChildren(node):
	if node.left == None  and node.right == None:
		return 0
	elif node.left == None or node.right == None:
		return 1
	else: return 2



def searchAndDeleteNode(node,data):

	if not node:
		return

	if node.data == data :
		if node.parent == None:
			print('One node tree')
			return

        # Node with no children
		if node.left == None and node.right == None:
			if node.parent.left == node:
				node.parent.left = None
			else:
				node.parent.right = None

        # Node with one child
		if node.numChildren() == 1:
			if node.data >= node.parent.data:
				# right child
				if node.left != None:
					node.parent.right = node.left
				else:
					node.parent.right = node.right
			else:
				# left child
				if node.left != None:
					node.parent.left = node.left
				else:
					node.parent.left = node.right

		if node.numChildren() == 2:
			nl = findLowestInRight(node.right)
			node.data = nl.data
			searchAndDeleteNode(node.right,nl.data)

	else:
		if data > node.data:
			searchAndDeleteNode(node.right,data)
		else:
			searchAndDeleteNode(node.left,data)


 global curr
    if root != None:
        if check_binary_search_tree_(root.left):
            if root.data <= curr:
                return False
            else:
                curr = root.data
                if check_binary_search_tree_(root.right):
                    return True
    else:
        return True
        


def printDiv():
	print('-'*10)

if __name__ == '__main__':

	l = [1,2,6,4,3,7,0]

	n5 = Node(5)

	for i in l:
		insertBST(n5,Node(i))

	inOrder(n5)
	printDiv()
	print(findH(n5))
	printDiv()
	printLeaves(n5)
	searchBST(n5,7)
	printDiv()
	levelOrderTraversal(n5)
	printDiv()
	searchAndDeleteNode(n5,1)
	levelOrderTraversal(n5)
	insertBST(n5,Node(1))
	printDiv()
	levelOrderTraversal(n5)
	searchAndDeleteNode(n5,0)
	printDiv()
	levelOrderTraversal(n5)




