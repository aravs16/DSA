from Graph import Graph
from Vertex import Vertex
import sys

class PriorityQueueDJK:

    def __init__(self,G):
        self.vert_list = [i for i in G.getAllVertices()]
        self.vert_idxs = {}
        idx = 0
        for v in self.vert_list:
            self.vert_idxs[v] = idx
            idx = idx+1
        self.heap_len  = len(self.vert_list)
        self.build_heap()

    def min_heapify(self,i):
        li = 2*i+1
        ri = 2*i+2
        smallest = i
        if li < self.heap_len and self.vert_list[li].d < self.vert_list[smallest].d:
            smallest = li
        if ri < self.heap_len and self.vert_list[ri].d < self.vert_list[smallest].d:
            smallest = ri
        if i != smallest:
            self.vert_list[i], self.vert_list[smallest] = self.vert_list[smallest], self.vert_list[i]
            self.vert_idxs[self.vert_list[i]] = i
            self.vert_idxs[self.vert_list[smallest]] = smallest
            self.min_heapify(smallest)

    def build_heap(self):
        nl = (self.heap_len//2)-1
        for i in range(nl,-1,-1):
            self.min_heapify(i)

    def extract_min(self):
        minm = self.vert_list[0]
        self.vert_list[0] = self.vert_list[-1]
        self.vert_list.pop()
        self.heap_len = len(self.vert_list)
        if len(self.vert_list) != 0:
            self.vert_idxs[self.vert_list[0]] = 0
        self.build_heap()
        return minm

    def get_queue_size(self):
        return self.heap_len

    def find_vert_idx(self,vid):
        for i in range(self.heap_len):
            if self.vert_list[i].vid == vid:
                return i
        return -1

    def change_vert_value(self,v,newval):
        vrtx_i = self.vert_idxs[v]
        self.vert_list[vrtx_i].d = newval
        while vrtx_i//2 >= 0:
            if self.vert_list[vrtx_i//2].d > self.vert_list[vrtx_i].d:
                temp = self.vert_list[vrtx_i//2]
                self.vert_list[vrtx_i//2] = self.vert_list[vrtx_i]
                self.vert_list[vrtx_i] = temp
                self.vert_idxs[self.vert_list[vrtx_i]] = vrtx_i
                self.vert_idxs[self.vert_list[vrtx_i//2]] = vrtx_i//2
            else:
                break
            vrtx_i = vrtx_i//2

    def change_vert_value_(self,v,newval):
        vrtx_i = self.find_vert_idx(v.vid)
        self.vert_list[vrtx_i].d = newval
        print(self.vert_list[vrtx_i//2].d,self.vert_list[vrtx_i].d,vrtx_i,vrtx_i//2)
        while vrtx_i//2 >= 0:
            if self.vert_list[vrtx_i//2].d > self.vert_list[vrtx_i].d:
                print('Yes')
                temp = self.vert_list[vrtx_i//2]
                self.vert_list[vrtx_i//2] = self.vert_list[vrtx_i]
                self.vert_list[vrtx_i] = temp
            else:
                break
            vrtx_i = vrtx_i//2


class Djikstras:

    def __init__(self,G,start):
        for v in G.getAllVertices():
            v.d = sys.maxsize
            v.parent = None
            start.d = 0
        self.pq = PriorityQueueDJK(G)

    def run(self):
        s = []
        while self.pq.get_queue_size() != 0:
            node = self.pq.extract_min()
            s.append(node)
            for v in node.getAdjacentVertices():
                if v not in s:
                    # print('Relaxing',node.vid,v.vid)
                    self.relax_edge(node,v)

    def add_weights(self,val1,val2):
        if val1 == sys.maxsize or val2 == sys.maxsize:
            return sys.maxsize
        elif val1 == -1*sys.maxsize or val2 == -1*sys.maxsize:
            return -1*sys.maxsize
        else:
            return val1+val2
    
    def relax_edge(self,v1,v2):
        if v2.d > self.add_weights(v1.d, v1.getEdgeWeight(v2)):
            v2.parent = v1
            self.pq.change_vert_value(v2, self.add_weights(v1.d, v1.getEdgeWeight(v2)))
        else: return None
    
    def find_path(self,start,end):
        if start == end:
            print(start.vid)
            return 1
        elif end.parent == None:
            print('No path exists')
            return -1
        else:
            print(end.vid)
            return self.find_path(start,end.parent)



if __name__ == '__main__':

    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)
    v7 = Vertex(7)
    v8 = Vertex(8)
    v9 = Vertex(9)

    g = Graph()
    g.addEdge(v1,v2,1)
    g.addEdge(v1,v3,10)

    g.addEdge(v2,v4,4)
    g.addEdge(v2,v5,17)

    g.addEdge(v4,v3,1)
    g.addEdge(v4,v5,17)
    g.addEdge(v3,v5,1)

    g.addEdge(v5,v6,1)
    g.addEdge(v6,v4,1)

    dj = Djikstras(g,v1)
    dj.run()
    dj.find_path(v1,v6)
