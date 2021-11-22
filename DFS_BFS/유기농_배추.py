import sys
sys.setrecursionlimit(10000)

N = int(input())
# dfs는 스택 외에도 재귀
def dfs(x,y):
    global field
    field[x][y]=0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] <= height-1 and y+dy[i] >= 0 and y+dy[i] <= width-1:
            if field[x+dx[i]][y+dy[i]] ==1:
                dfs(x+dx[i],y+dy[i])


for _ in range(N):
    width,height,baechoo = map(int,input().split(' '))
    field = [[0 for j in range(width)] for i in range(height)]
    for _ in range(baechoo):
        x,y = map(int,input().split(' '))
        field[y][x] = 1

    bug=0
    # dfs를 스택이 아닌 재귀로 쓸거라면 처음부터 필드를 포문으로 돌리기.
    # 함수에 보내지 말고.
    for i in range(height):
        for j in range(width):
            if field[i][j] ==1:
                dfs(i,j)
                bug+=1

    print(bug)

# 모범 풀이
# flood fill느낌 유기농 배추
import sys
sys.setrecursionlimit(10000)
T = int(input())
B = []
ck =[]
dx,dy =[1,0,-1,0],[0,1,0,-1]
# 재귀함수의 깊이를제한하는 코드가 있어야됨
def dfs(x,y):
    global B,ck
    if ck[x][y]==1:
        return
    ck[x][y]=1
    for i in range(4):
        xx,yy = x+dx[i],y+dy[i]
        if B[xx][yy]==0 or ck[xx][yy]==1:
            continue
        dfs(xx,yy)

def process():
    global B,ck
    M,N,K = map(int, input().split())
    B =[[0 for i in range(50+2)] for _ in range(50+2)]
    ck = [[0 for i in range(50 + 2)] for _ in range(50 + 2)] # 탐색했다는 체크리스트
    for _ in range(K):
        X,Y= map(int,input().split())
        B[Y+1][X+1] =1
    ans=0
    for i in range(1,N+1): # 플러드 필은 완전탐색 할 수 밖에
        for j in range(1,M+1): # 시간복잡도는 탐색하는 맵의 크기
            if B[i][j]==0 or ck[i][j]==1:
                continue
            dfs(i,j)
            ans+=1
    print(ans)

for _ in range(T):
    process()