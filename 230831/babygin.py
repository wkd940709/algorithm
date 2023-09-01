def babygin(arr):
    tri = runn = 0
    if arr[0] == arr[1] == arr[2]:
        runn += 1
    if arr[3] == arr[4] == arr[5]:
        runn += 1
    if arr[0]+2 == arr[1]+1 == arr[2]:
        tri += 1
    if arr[3]+2 == arr[4]+1 == arr[5]:
        tri += 1
    if tri + runn == 2:
        return 1
    else:
        return 0

def perm(i, N):
    global answer
    if i == N:
        if babygin(arr):
            answer = 'Baby Gin'
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            perm(i+1, N)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input()))
    N = len(arr)
    answer = 'Lose'
    perm(0,N)
    print(f'#{tc} {answer}')