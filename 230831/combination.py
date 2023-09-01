def ncr(n,r):
    if r == 0:
        print(tr)
    elif n<r:
        return
    else:
        tr[r-1] = a[n-1]    # a[n-1] 조합에 포함되는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)         # a[n-1] 조합에 포함안되는 경우

a = [1,2,3,4,5]
N = 5
R = 3
tr = [0]*R
ncr(N,R)


