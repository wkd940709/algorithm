import sys
sys.stdin = open("input.txt","r")

def perm(i, N):
    global max_val
    global cnt
    global answer
    if i == N and cnt == K:
        if max_val < int(''.join(arr)):
            max_val = int(''.join(arr))
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            if i != j:
                cnt += 1
            # if cnt == K and max_val < int(''.join(arr)):
            #     max_val = int(''.join(arr))
            # if i+1<N:
            perm(i+1, N)
            arr[i], arr[j] = arr[j], arr[i]
            if i != j:
                cnt -= 1

T = int(input())
for tc in range(1,T+1):
    arr, K = input().split()
    arr = list(arr)
    K = int(K)
    N = len(arr)
    cnt = 0
    max_val = 0
    perm(0,N)
    print(f'#{tc} {max_val}')