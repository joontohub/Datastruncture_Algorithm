import sys

import sys
import heapq


V = int(input())
E = int(input())
INF = sys.maxsize


K = 0

dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    
    while heap:
        wei, now = heapq.heappop(heap)

        
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            
            
            next_wei = w + wei
            
            if next_wei < dp[next_node]:
                
                dp[next_node] = next_wei
                
                heapq.heappush(heap,(next_wei,next_node))


for _ in range(E):
    u, v, w = map(int, input().split())
    
    graph[u].append((w, v))


Dijkstra(K)
print(0, end=' ')
for i in range(1,V):
    print("inf" if dp[i] == INF else dp[i],end =" ")
def Dijkstra(n,m,H):
    inf = sys.maxsize

    dist = [inf] * n
    

    dist[0] = 0
  
    
    while len(H):
        u = H.delete_min()
        a = 0
        for v in u:
            if v != inf:
                if dist[v] > dist[a] + v:
                    dist[v] = dist[a] + v
        a += 1
    return dist
    




Graph = []
inf = sys.maxsize

n = int(input())
m = int(input())

graph = [[inf] * n for i in range(m)]
H = Heap(graph)
for i in range(m):
    u,v,w = map(int,input().split())
    graph[u][v] = w


print(Dijkstra(n,m,H))

