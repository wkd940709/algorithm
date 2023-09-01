# import sys
# sys.stdin = open("input.txt","r")

def search(i,j,s):
    global min_val
    if i>=N or j>=N:
        return
    elif i == N-1 and j == N-1:
        s += arr[i][j]
        if min_val > s:
            min_val = s
        return
    else:
        s += arr[i][j]
        search(i, j + 1,s)
        search(i + 1, j, s)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    min_val = (13+13)*10
    search(0,0,s)
    print(f'#{tc} {min_val}')
