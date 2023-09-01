import sys
sys.stdin = open("input.txt","r")

def f(i,j,s):
    global min_val
    if i == j or j>=N:
        return
    elif i == N-1 and j == 1:
        s += arr[i][j]
        if min_val > s:
            min_val = s
        return
    else:
        for k in range(1, N):
            f(i+1, j, s+arr[i][j])
            f(i, j+1, s+arr[i][j])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = (N+N)*100
    f(0,0,0)
    print(min_val)