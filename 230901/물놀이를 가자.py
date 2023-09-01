# import sys
# sys.stdin = open("input.txt","r")

from collections import deque

def bfs():
    q = deque()
    visited = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0
    # print(arr)
    while q:
        i, j = q.popleft()
        for di, dj in [[1,0],[0,1],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 'L' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))
                # print(f'{i, j, visited}')
    s = 0
    for i in range(N):
        for j in range(M):
            s += visited[i][j]
    # print(visited)
    return s

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {bfs()}')