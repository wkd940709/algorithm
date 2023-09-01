def f(i, j, s, N):
    global min
    if i>=N:
        f(i-1, j + 1, s + arr[i][j], N)
    if j>=N:
        f(i + 1, j - 1, s + arr[i][j], N)
    elif i == N-1 and j==N-1:
        s += arr[i][j]
        if min > s:
            min = s
    else:
        f(i, j+1, s+arr[i][j], N)
        # print(i, j)
        f(i+1, j, s+arr[i][j], N)
    return min
min = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(f(0, 0, 0, N))