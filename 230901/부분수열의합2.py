import sys
sys.stdin = open("input.txt","r")

def f(i,N,s,K):
    global cnt
    global call
    call += 1
    if i == N:
        if s == K:
            cnt += 1
    elif s > K:
        return
    else:
        f(i+1,N,s+arr[i],K)
        f(i+1,N,s,K)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    call = 0
    f(0,N,0,K)
    print(f'#{tc} {cnt}')




