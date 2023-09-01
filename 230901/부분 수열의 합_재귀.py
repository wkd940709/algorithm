# import sys
# sys.stdin = open("input.txt","r")

def bit_operation(i,s):
    global cnt
    global call
    call += 1
    if i == N:
        if s == K:
            cnt += 1
    elif s > K:
        return
    else:
        bit_operation(i+1,s+arr[i])
        bit_operation(i+1,s)
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    call = 0
    bit_operation(0, 0)
    print(f'#{tc} {cnt}')