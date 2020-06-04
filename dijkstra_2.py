import sys
import heapq

class Heap:
    def __init__(self,L=[]):
        self.A = L
    def __str__(self):
        return str(self.A)
    def __len__(self):
        return len(self.A)

    def heapify_down(self,orig_k,n):
        k = orig_k[0]
        if 2*k +1 :
            while 2*k + 1 < n:
                L,R = 2*k + 1 , 2*k + 2
                if L < n and self.A[L] > self.A[k]:
                    m = L    
                else:
                    m = k
                if R < n and self.A[R] > self.A[m]:
                    m = R
            
                if m != k:
                    self.A[k], self.A[m] = self.A[m], self.A[k]
                    k = m

                else: break
        else:
            return
    def insert(self,key):
        self.A.append(key)
        self.heapify_down(key,len(self)-1)
        print(self)

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1,-1,-1):
            self.heapify_down(k,n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1,-1,-1):
            self.A[0],self.A[k] = self.A[k],self.A[0]
            n = n - 1
            self.heapify_down(0, n)

    def delete_min(self):
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1],self.A[0] 
        self.A.pop()
        self.heap_sort() #whi cant 
        return key


def Dijkstra(start):
    
    dp[start] = 0
    H = Heap()
    H.insert((0,start))

    while H:
        now, weight = H.delete_min()
        print(now,weight)
        if dp[now] < weight:
            print("1a1")
            continue
        print(graph)
        for next_node, w in graph[now]:
            print("ffff")
            print(next_node,w,weight,"sdaf")
            next_weight = w + weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                H.insert((next_node,next_weight))

V = int(input())
E = int(input())
INF = sys.maxsize

#시작점 K
K = 0
#가중치 테이블 dp
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]


#초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    #(가중치, 목적지 노드) 형태로 저장
    graph[u].append((v,w))


Dijkstra(K)
for i in range(1,V+1):
    print("inf" if dp[i] == INF else dp[i],end =" ")
print()
