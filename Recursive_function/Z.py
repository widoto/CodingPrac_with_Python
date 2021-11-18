# 내 풀이
def solve(n,x,y):
    global result
    if n==2:
        if x== X and y==Y:
            print(result)
            return
        result+=1

        if x== X and y+1 ==Y:
            print(result)
            return
        result+=1

        if x+1 == X and y==Y:
            print(result)
            return
        result+=1

        if x+1 == X and y+1 ==Y:
            print(result)
            return
        result+=1

        solve(n/2,x,y)
        solve(n / 2, x, y+n/2)
        solve(n / 2, x+n/2, y)
        solve(n / 2, x+n/2, y+n/2)

result =0
N,X,Y = map(int,input().split(' '))
solve(2**N,0,0)

# 모범 풀이
# 더 간결하지만 아직은 재귀를 완전히 이해할 수 있도록 풀어서 쓰는 것이 나은 것 같다.
N,r,c = map(int,input().split())

# z : 0,0을 기준으로 x,y의 숫자
def Z(sz,x,y):
    if sz==1:
        return 0
    sz//=2
    for i in range(2):
        for j in range(2):
            if x<sz*(i+1) and y<sz*(j+1): # 두칸이다
                return (i*2+j) *sz*sz + Z(sz,x-sz*i,y-sz*j)

print(Z(2**N,r,c))