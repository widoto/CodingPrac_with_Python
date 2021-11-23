import copy
# 가장 큰 증가부분 수열
N,A = int(input()),list(map(int,input().split()))
# DP[i]: i까지 왔을때, 합의최대
DP = copy.deepcopy(A)
# 자기 자신이답이 될 수도 있어
for i in range(1,N):
    for j in range(i):
        # 만약 지금 이 자리가 앞에 원소보다 큰 값이면 걔까지 더한 값이 지금 있는 값의 최대이다.
        if A[i] > A[j]:
            DP[i] = max(A[i] + DP[j],DP[i])

print(max(DP))
# 가장 큰 값을 출력한다.