# 정수 삼각형
# dp 안쓰고 다 해보면 못푼다.
N = int(input())
# DP[i][j] : i,j에 도착했을때 최댓값
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]+A[i][j])
A = [[0 for _ in range(N+1)] for i in range(N+1)] # 0으로 채우는게 좋다 디피는 # 진짜 값입력하는 곳
DP = [[0 for _ in range(N+1)] for i in range(N+1)] # 이것은 지금 이 자리까지 오기의 최대값을 저장하는 곳
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    for j in range(1,i+1):
        A[i][j] = tmp[j-1]

for i in range(1,N+1):
    for j in range(1,i+1):
        DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]
        # 이거 중요 위 대각선 원소 2개 중 더 큰거 + 현재 값

print(max(DP[-1]))