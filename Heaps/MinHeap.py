def  min_heapify(A,i,heap_max_idx):

	heap_max_idx = len(A)-1
	left = 2*i+1
	right = 2*i+2
	smallest = i

	if left <= heap_max_idx and A[left] < A[i]:
		smallest = left

	if right <= heap_max_idx and A[right] < A[smallest]:
		smallest = right

	if i != smallest:
		A[i],A[smallest] = A[smallest],A[i]
		min_heapify(A,smallest,heap_max_idx)


def buildMinHeap(A):

	nonl = (len(A)//2) - 1
	le = len(A)

	for i in range(nonl,-1,-1):
		print(i)
		min_heapify(A,i,le-1)


def  min_heapify_(A,i,heap_max_idx):

	left = 2*i+1
	right = 2*i+2
	smallest = i

	if left <= heap_max_idx and A[left] < A[i]:
		smallest = left

	if right <= heap_max_idx and A[right] < A[smallest]:
		smallest = right

	if i != smallest:
		A[i],A[smallest] = A[smallest],A[i]
		min_heapify_(A,smallest,heap_max_idx)


def buildMinHeap_(A,heap_min_idx):
	nonl = ((heap_min_idx+1)//2)-1
	for i in range(nonl,-1,-1):
		min_heapify_(A,i,heap_min_idx)

def min_heap_sort(A):
	idx = len(A)-1
	for i in range(idx,0,-1):
		buildMinHeap_(A,i)
		A[0],A[i] = A[i],A[0]
		

if __name__ == '__main__':
	A = [6,5,4,3,2,1]
	# buildMinHeap(A)
	# print(A)
	min_heap_sort(A)
	print(A)