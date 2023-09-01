# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):

    bin = input()
    tri = list(map(int, input()))

    length_tri = len(tri)
    length_bin = len(bin)

    bin = int(bin, 2)
    arr_bin = [0]*length_bin

    for i in range(length_bin):
        arr_bin[i] = bin ^ (1<<i)
        # print(arr_bin)

    for i in range(length_tri):
        num1 = 0
        num2 = 0
        for j in range(length_tri):
            if i != j:
                num1 = num1*3 + tri[j]
                num2 = num2*3 + tri[j]
                # print(f'{i,j} {num1, num2}')
            else:
                num1 = num1*3 + (tri[j]+1)%3
                num2 = num2*3 + (tri[j]+2)%3
                # print(f'{i,j} {num1, num2}')
        if num1 in arr_bin:
            answer = num1
            break
        if num2 in arr_bin:
            answer = num2
            break
    print(f'#{tc} {answer}')

