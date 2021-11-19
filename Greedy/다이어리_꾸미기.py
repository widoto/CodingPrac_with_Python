# 핵심은 N을 표현하는 것이 아니라 N까지 표현하는것이다.

# 모범 풀이
N = input()
S = '1'*len(N)

if len(N) ==1:
    print(1)

elif int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)

