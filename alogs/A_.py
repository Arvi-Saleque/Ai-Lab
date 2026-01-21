import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

def h_of_n(g, u):  # param -> graph and source node
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
gr =  [[] for _ in range(n + 1)]

cost = {}

for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))
    cost[(u, v)] = w
    
    
harr = h_of_n(g, n) # lest our goal node n

# start node 1

start = 1
goal = n



INF = 10 ** 18
dist = [INF] * (n + 1)
parent = [-1] * (n + 1)

pq = []

heapq.heappush(pq, (harr[start], 0, start)) # f = g + h, g, start

while pq:
    fn, gcur, u = heapq.heappop(pq)
    
    if gcur != dist[u]:
        continue
    
    if u == goal:
        break
    
    for v, w in  g[u]:
        newg = w + gcur
        if newg < dist[v]:
            dist[v] = newg
            parent[v] = u
            heapq.heappush(pq, (harr[v] + newg, newg, v))
        

if dist[goal] == INF:
    print("No path found")
else:
    print(dist[goal])

    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(*path)
    
    

    


