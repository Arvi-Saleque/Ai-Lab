import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

def djikstra_from_u(g, u):  # param -> graph and source node
    INF = 10 ** 18
    dist = [INF] * (n + 1)
    dist[u] = 0
    
    pq = []
    heapq.heappush(pq, (0, u))
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d != dist[u]:
            continue
        
        for v, w in g[u]:
            if dist[v] > w + d:
                dist[v] = w + d
                heapq.heappush(pq, (dist[v], v))
    
    return dist

g =  [[] for _ in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    
    
dist = djikstra_from_u(g, 1)

print(*dist[1:])
    

    


