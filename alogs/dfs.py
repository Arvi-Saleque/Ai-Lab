import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
vis = [[False]*m for _ in range(n)]

def valid(x, y):
    if 0 <= x < n and 0 <= y < m and not vis[x][y] and grid[x][y] == '.': 
        return True;
    return False;
    
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
    
def dfs(x, y):
    vis[x][y] = 1
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if valid(nx, ny):
            dfs(nx, ny)
            
            
ans = 0
for i in range(0, n):
    for j in range(0, m):
        if valid(i, j):
            ans += 1
            dfs(i, j)
            
            
print(ans)
