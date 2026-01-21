# this are for CP problem submission 
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    

vis = {}

def dfs(u):
    vis[u] = 1
    for v in g[u]:
        if v not in vis:
            dfs(v)
        
        
ans = []

for u in range(1, n + 1):
    if u not in vis:
        dfs(u)
        ans.append(u)
        
print(len(ans) - 1)
for i in range(1, len(ans)):
    print(f"{ans[0]} {ans[i]}")
    
    
