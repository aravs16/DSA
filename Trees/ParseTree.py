class Node:

	def __init__(self,data):

		self.left = None
		self.right = None
		self.data = data
		self.parent = None

	def insertLeft(self,node):
		self.left = node
		self.left.parent = self
		return node

	def insertRight(self,node):
		self.right = node
		self.right.parent = self
		return node


""" Building a Parse Tree from a given expression """
def buildParseTree(exp):

	operators =['+','-','*']
	brackets = ['(',')']

	startNode = Node(None)

	stck = [startNode]

	for i in exp:
        # Rule 1: if open bracket insert left child and navigate to it
        # This is because we are expecting a left operand
		if i == '(':
			curr = stck[-1]
			lchild = curr.insertLeft(Node(''))
			stck.append(lchild)

        # Rule 2: if it is a digit assign the current node it's value and move up
        # This is because we now expect an operator which is always parent of a number in parse tree
		if i.isdigit():
			stck[-1].data = i
			stck.pop()

        # Rule 3: If it is an operator then assign the operator to current node and move down to right child
		if i in operators:
			curr = stck[-1]
			rchild = curr.insertRight(Node(None))
			curr.data = i
			stck.append(rchild)
        
        # Rule 4: Just move back one level up. End of expression.
		if i == ')':
			stck.pop()

	return startNode

def inOrder(node):

	if node:
		inOrder(node.left)
		print(node.data)
		inOrder(node.right)

def preOrder(node):

	if node:
		print(node.data)
		preOrder(node.left)
		preOrder(node.right)


def postOrder(node):

	if node:
		postOrder(node.left)
		postOrder(node.right)
		print(node.data)


"""Evaluate a parse tree.
   Do a post order traversal. If it is an operand then insert in to stack.
   If you find an operator, pop last two operands fromt the stack and apply operator and append back in to stack"""
import operator
opers ={'+':operator.add,'-':operator.sub,'*':operator.mul}
value = None
stck = []
operators =['+','-','*']
def evalExp(node):
	global stck
	global value
	if node:
		evalExp(node.left)
		evalExp(node.right)
		if node.data in operators:
			i = int(stck.pop())
			j = int(stck.pop())
			stck.append(opers[node.data](j,i))
		else:
			stck.append(node.data)

"""Just an enabler function"""
def evaluate(head):
	global stck
	evalExp(head)
	print(stck[0])



if __name__ == '__main__':

	head = buildParseTree('(((((3*2)*3)+4)*2)-6')
	# inOrder(head)
	# preOrder(head)
	postOrder(head)
	evaluate(head)



