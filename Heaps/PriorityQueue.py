def max_heapify(A,node_idx,heap_max_idx):

	left = 2*node_idx+1
	right = 2*node_idx+2

	largest = node_idx

	if left <= heap_max_idx and A[left] > A[node_idx]:
		largest = left
	
	if right <= heap_max_idx and A[right] > A[largest]:
		largest = right

	if largest != node_idx:
		A[node_idx],A[largest]= A[largest],A[node_idx]
		max_heapify(A, largest, heap_max_idx)

def build_max_heap(A,l):
	leaf_start = (l//2)-1
	for i in range(leaf_start,-1,-1):
		max_heapify(A,i,l-1)

def heap_max(heap):
	return heap[0]

def extract_max(heap):
	max = heap[0]
	heap[0] = heap[-1]
	heap.pop()
	max_heapify(heap,0,len(heap)-1)
	return max

def insert_to_heap(A,new):
	A.append(new)
	build_max_heap(A,len(A))

def delete_from_heap(A,i):
	A[i],A[-1] = A[-1],A[i]
	A.pop()
	build_max_heap(A,len(A))

def increase_key(A,i,key):

	if i < 0 or i > len(A):
		return -1

	A[i] = key

	while i >= 0:
		if A[i//2] < A[i]:
			A[i//2], A[i] = A[i], A[i//2]
			i  = i//2
		else:
			break


if __name__ == '__main__':
	A = [3,2,1,4,5,6]
	build_max_heap(A,len(A))
	
	print(A)
	print(heap_max(A))
	print(extract_max(A))
	print(extract_max(A))
	print(extract_max(A))

	A = [3,2,1,4,5,6]
	build_max_heap(A,len(A))
	increase_key(A,5,9)
	print(A)

	print('-'*10)
	A = [3,2,1,4,5,6]
	build_max_heap(A,len(A))
	delete_from_heap(A,2)
	print(A)

	insert_to_heap(A,99)
	print(A)





