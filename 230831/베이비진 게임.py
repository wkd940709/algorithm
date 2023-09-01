import sys
sys.stdin = open('input.txt','r')

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
    if tri + runn >= 1:
        return 1
    else:
        return 0

def perm(i):
    global answer
    if i >= 2:
        print(arrA, arrB)
        if babygin(arrA[:i+1]):
            return 1
        elif babygin(arrB[:i+1]):
            return 2

    else:
        for j in range(i, N//2):
            arrA[i], arrA[j] = arrA[j], arrA[i]
            arrB[i], arrB[j] = arrB[j], arrB[i]
            perm(i+1)
            arrA[i], arrA[j] = arrA[j], arrA[i]
            arrB[i], arrB[j] = arrB[j], arrB[i]
    return 0



T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    arrA = []
    arrB = []
    for i in range(N//2):
        arrA.append(arr[i*2])
        arrB.append(arr[i * 2+1])
    print(arrA,arrB)
    print(perm(0))
    print(f'#{tc} {answer}')


