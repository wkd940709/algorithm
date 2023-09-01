import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0]*N
    cnt = 0
    print(1<<N)
    for i in range(1<<N):
        s = 0
        for j in range(N):
            if i & (1<<j):
                s += arr[j]
        if s == K:
            cnt += 1
        print(i,s)
    print(f'#{tc} {cnt}')


    # if bit[i] == 1:
    #     s += arr[i]