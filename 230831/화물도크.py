# import sys
# sys.stdin = open("input.txt","r")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda a: a[1])
    arr = [[0, 0]] + arr
    j = 0
    cnt = 0
    for i in range(1, N+1):
        if arr[i][0] >= arr[j][1]:
            j = i
            cnt += 1
    print(f'#{tc} {cnt}')
