# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ## 연속한 1의 개수를 이용해서 풀기
    cnt_lst = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] == arr[i][j]+1:
                    cnt_lst[arr[i][j]] = 1
    cnt = 0
    max_cnt = 0
    max_start = 0
    for i in range(N*N,0,-1):
        if cnt_lst[i] == 1:
            cnt += 1
            if max_cnt <= cnt:
                max_cnt = cnt
                max_start = i
        else:
            cnt = 0
    print(f'#{tc} {max_start} {max_cnt+1}')
