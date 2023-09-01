# import sys
# sys.stdin = open("input.txt","r")
def subset(i,N):
    global cnt
    if i == N:
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += arr[j]
        if s == K:
            cnt += 1
    else:
        bit[i] = 1
        subset(i+1,N)
        bit[i] = 0
        subset(i+1,N)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0]*N
    cnt = 0
    subset(0, N)
    print(f'#{tc} {cnt}')

