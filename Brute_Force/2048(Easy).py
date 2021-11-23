from copy import deepcopy # 함수의 내용은 복사하되 주소값은 복사하지 않는다.
N = int(input())

Board = [list(map(int,input().split())) for i in range(N)]
# 네방향 다하지말고 한 방향으로만 하고 맵을 돌려주는 것이 맞다.

def rotate90(B,N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j] # 구십도 회전

    return NB

def convert(lst, N): #가짜로 회전
    new_list = [i for i in lst if i]
    for i in range(1,len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *=2
            new_list[i]=0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))

def dfs(N,B,count):
    ret= max([max(i) for i in B]) #가장 큰 숫자
    if count ==0: # 주어진 기회를 다썼으면 답을 반환
        return ret

    for _ in range(4):
        X = [convert(i,N) for i in B] # 네 방향으로 회전하라
        if X!=B: #원래 판과 다르다면
            ret = max(ret,dfs(N,X,count-1)) #다시 맥스값 추출
        B = rotate90(B,N) # 진짜 회전하기
    return ret


print(dfs(N,Board,5)) # NxN에다가 최대 5번을 이동시켜라.