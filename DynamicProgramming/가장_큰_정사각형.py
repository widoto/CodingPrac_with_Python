##가장큰 정사각형
N,M = map(int, input().split())
A = [[0 for _ in range(M+1)] for i in range(N+1)]
# DP[i][j] = i,j까지왔을때, 가장 큰 정사각형의 한 변의 길이
# DP[i][j] = min(DP[i-1][j],DP[i-1][j-1],DP[i][j-1]) +1
DP = [[0 for _ in range(M+1)] for i in range(N+1)]
# 이건 그냥 값을 채우는 것
for i in range(N):
    for idx,j in enumerate(list(map(int,list(input())))):
        A[i+1][idx+1] = j

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i][j]: # 만약 1이면
            DP[i][j] = min(DP[i-1][j],DP[i-1][j-1],DP[i][j-1]) +1
# 한 기점을 기준으로 정사각형이 될 수 있도록 하는 위, 아래, 대각선 값이 모두 같은 값(같은 변)을 가져야
# MIN을 해도 같은 결과가 나오니까 다음 +1한 변을 가질 수 있게 되는 것이다.
# 이렇듯 격자 = 무조건 DP이다.
print(max([max(i) for i in DP])**2)