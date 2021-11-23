# 고난도 문제

TC= int(input())
S,DP = 0,0

def f(i,j):
    global S,DP
    if i==j:
        return 0
    if DP[i][j] != -1:
        return DP[i][j]
    for k in range(i,j):
        tmp= f(i,k) + f(k+1,j) + S[j] - S[i-1]
        if DP[i][j] == -1 or DP[i][j] > tmp:  # 한번도 값을 채우지 않았거나 새로 구한 값이 기존 값보다 작다면
            DP[i][j] = tmp
    return DP[i][j]

def process():
    global S,DP
    # 최소힙으로 풀었던 기억이 있다.
    N,A = int(input()),list(map(int,input().split()))
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] : DP[k+1][j] + sum(A[i]~A[j])
    S,DP = [0 for _ in range(N+1)], [[-1 for _ in range(N+1)] for i in range(N+1)]
    for i in range(1,N+1): S[i] = S[i-1] + A[i-1]
    print(f(1,N))

for _ in range(TC):
    process()