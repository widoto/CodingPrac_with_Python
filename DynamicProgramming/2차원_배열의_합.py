# 배열의 크기 설정
N,M = map(int, input().split())
# 배열에 수 채우기
A = [list(map(int,input().split())) for _ in range(N)]
# DP[i][j]=1,1부터 (i,j)까지의 부분합
DP = [[0 for i in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]+ A[i-1][j-1]
        # DP[i][j]까지의 합은 위/왼쪽방향의 칸까지의 합 - 그 두 칸까지의 합 중 겹치는 부분빼고 + 현재 있는 칸의 값을 더함

for _ in range(int(input())):
    i,j,x,y = map(int,input().split())
    print(DP[x][y]- DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])

    # 여기서 주의할 것은 A는 1부터 시작하는 것을 고려하지 않았고, DP는 고려하였다.
    # 따라서 A의 인덱스는 DP보다 1씩 좌표가 작다.