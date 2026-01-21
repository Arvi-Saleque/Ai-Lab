# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 10:59:15 2026

@author: Softlab
"""

import heapq

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]


start = (n - 1, 0)
goal = (0, m - 1)

def hfn(x, y) -> int:
    return x + abs(y - m + 1);

def valid(x, y):
    if 0 <= x < n and 0 <= y < m and grid[x][y] == '.':
        return True
    return False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def greedy_best():
    pq = []
    u, v = start
    heapq.heappush(pq, (hfn(u, v), u, v))   # pq h(n) nodes
    vis = [[False]*m for _ in range(n)]

    INF = 10**18
    dist = [[INF]*m for _ in range(n)]
    dist[u][v] = 0
    
    no_nodes = 0
    
    while pq:
        d, u, v = heapq.heappop(pq)
        
        if vis[u][v]:
            continue
        
        vis[u][v] = 1
        no_nodes += 1
        
        if (u, v) == goal:
            break
        
        for i in range(0, 4):
            nx = u + dx[i]
            ny = v + dy[i]
            
            if valid(nx, ny):
                if dist[nx][ny] > dist[u][v] + 1:
                    dist[nx][ny] = dist[u][v] + 1
                    heapq.heappush(pq, (hfn(nx, ny), nx, ny))
            
    return no_nodes, dist[goal[0]][goal[1]] if dist[goal[0]][goal[1]] != INF else -1



def Astar():
    pq = []
    u, v = start
    heapq.heappush(pq, (hfn(u, v), 0, u, v)) # pq f=g+h, g  nodes
    INF = 10 ** 18
    dist = [[INF]*m for _ in range(n)]
    dist[u][v] = 0
    
    no_nodes = 0
    
    while pq:
        d, curg, u, v = heapq.heappop(pq)
        
        if curg != dist[u][v]:
            continue
        
        no_nodes += 1
        
        if (u, v) == goal:
            break
        
        for i in range(0, 4):
            nx = u + dx[i]
            ny = v + dy[i]
            
            if valid(nx, ny):
                if dist[nx][ny] > curg + 1:
                    dist[nx][ny] = curg + 1
                    heapq.heappush(pq, (curg + 1 + hfn(nx, ny), dist[nx][ny], nx, ny))
            
    return no_nodes, dist[goal[0]][goal[1]] if dist[goal[0]][goal[1]] != INF else -1


    
a, b = greedy_best()
print(f"greedy_best nodes={a} dist={b}")

a, b = Astar()
print(f"A* nodes={a} dist={b}")