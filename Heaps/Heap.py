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


def heap_sort(A):
	li = len(A)
	for i in range(li,1,-1):
		build_max_heap(A,i)
		A[0],A[i-1] = A[i-1],A[0]


if __name__ == '__main__':
	A = [3,4,5,1,2,6]
	heap_sort(A)
	print(A)

