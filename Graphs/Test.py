class Test:

	def __init__(self,id,value):
		self.id = id
		self.value = value


if __name__ == '__main__':

	t1 = Test(1,'Value1')
	l = [t1]
	d = {}
	d[1]=t1

	d[1].value = 'Value2'

	print(l[0].value)
