# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    # 컨테이너 개수, 트럭 개수
    N, M = list(map(int,input().split()))
    # 화물 무게
    W = list(map(int,input().split()))
    # 트럭 최대 적재중량
    T = list(map(int,input().split()))
    W.sort()
    T.sort()
    answer = 0
    while T and W:
        if W[-1] <= T[-1]:
            answer += W.pop()
            T.pop()
        else:
            W.pop()
    print(f'#{tc} {answer}')

