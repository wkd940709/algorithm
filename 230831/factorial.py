import sys
sys.stdin = open("input.txt","r")

def baby_gin(p):
    run = tri = 0
    if p[0] == p[1] == p[2]:
        tri += 1
    if p[3] == p[4] == p[5]:
        tri += 1
    if p[0] + 2 == p[1] + 1 == p[2]:
        run += 1
    if p[3] + 2 == p[4] + 1 == p[5]:
        run += 1
    if run+tri == 2:
        return 1
    else:
        return 0
def nPk(i,N,K):
    if i == K:
       return baby_gin(p)
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                print(p)
                if nPk(i+1, N, K):
                    return 1
                used[j] = 0
        return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    N = 6
    K = 6
    p = [0]*K
    used = [0]*N
    r = nPk(0,N,K)
    if r:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')