import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ## 연속한 1의 개수를 이용해서 풀기
    cnt = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and arr[i][j]+1 == arr[ni][nj]:
                    cnt[arr[i][j]] = 1
    max_cnt = 0
    max_start = 0
    c = 0
    for i in range(N*N,0,-1):
        if cnt[i] == 1:
            c += 1
            if max_cnt < c:
                max_cnt = c
                max_start = i
            elif max_cnt == c:
                max_start = i
        else:
            c = 0
    print(max_start,max_cnt+1)
