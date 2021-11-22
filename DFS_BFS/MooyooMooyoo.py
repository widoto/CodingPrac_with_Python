# flood fill
def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

# 세로줄과 숫자를 바꿀 수 있는 그룹의 최소 원소수를 받는다.
N,K = map(int,input().split())

M = [list(input()) for _ in range(N)]
# 똑같은 판 2개 만들기
ck = new_array(N)
ck2 = new_array(N)

dx,dy = [0,1,0,-1],[1,0,-1,0]

# dfs로 같은 숫자끼리 모여있는 그룹찾기
def dfs(x,y):
    ck[x][y] = True # 방문했다고 확인
    ret =1
    for i in range(4):
        xx,yy = x+dx[i],y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx,yy)
    return ret

# dfs로 같은 숫자끼리의 그룹을 모두 0으로 바꾸기
def dfs2(x,y,val):
    ck2[x][y] = True # 방문한 것으로 바꾸기
    M[x][y] ='0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx,yy,val)

# 밑으로 밀기
def down():
    for i in range(10):
        tmp=[] # 지금 세로방향으로 탐색 중
        for j in range(N):
            if M[j][i]!='0':
                tmp.append(M[j][i])
        # 0이 아닌 부분은 담아둔다.
        for j in range(N - len(tmp)): # 내리면 최소 N-len(tmp)개의 칸은 위에서부터 0이니까
            M[j][i]='0'
        for j in range(N-len(tmp),N): # 이제 밑으로 내려운 숫자들을 처리
            M[j][i] = tmp[j-(N-len(tmp))] # N-len(tmp)부터 N-1까지, 위에서부터 tmp에 먼저 저장됬을 테니까

while(True):
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] =='0' or ck[i][j]: # 빈칸이거나 이미 방문한 곳이라면
                continue
            res = dfs(i,j) # 개수세기
            if res >= K:
                dfs2(i,j,M[i][j]) # 지우기
                exist = True
    if not exist:
        break
    down()# 내리기

for i in M:
    print(''.join(i))