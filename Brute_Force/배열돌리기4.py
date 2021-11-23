# 배열돌리기4
from copy import deepcopy
N,M,K = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)] # 본 배열판을 설정
Q = [tuple(map(int,input().split())) for _ in range(K)] # 어디 점을 기준으로 회전할지 알려줌(K개)
dx,dy = [1,0,-1,0],[0,-1,0,1] # 남서북동
ans = 10000

def value(arr):
    return min([sum(i) for i in arr]) # 답을 구하는 과정

def convert(arr,qry):
    (r,c,s) = qry
    r,c = r-1,c-1
    new_arr = deepcopy(arr)
    for i in range(1,s+1):
        # 중심점으로부터 대각선 방향 애들 주목
        rr,cc = r-i,c+i
        for w in range(4): # 회전하는 거지
            for d in range(i*2):
                rrr,ccc = rr+dx[w],cc+dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr,cc =rrr,ccc
    return new_arr

def dfs(arr,qry):
    global ans
    if sum(qry) == K: # 쿼리 다체크했으면
        ans = min(ans,value(arr)) # 최소값 구하기
        return
    for i in range(K):
        if qry[i]:
            continue
        new_arr = convert(arr,Q[i]) # 본 배열판과 이번 회차의 기준점
        qry[i] = 1 # 이 기준점을 썼다는 확인
        dfs(new_arr,qry) # 다시 반복, 이때 다음 회전을 위해 dfs를 가는 것임.+ 순서 바꿔 해볼라고.
        qry[i] = 0# 줬다 뺐는 백트래킹 기법, 다른 기준점에서는 초기화된 배열판으로 써야 하니까.

dfs(A,[0 for i in range(K)])
    # 비트마스크 기법: 어떤 쿼리를 채크했는지 확인하는 것. 각각을 이진수로 변환을 해준다.
    # 체크 배열을 이진수로 변환했다.
print(ans)