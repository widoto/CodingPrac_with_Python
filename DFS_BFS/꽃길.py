'''
N = int(input())
flower_list =[]
for _ in range(T):
    f_list = list(map(int,input().split(' ')))
    flower_list.append(f_list)

cost_list=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(1,N-1):
    for j in range(1,N-1):
        cost= flower_list[i][j]
        cost += flower_list[i + dx[0]][j + dy[0]]
        cost += flower_list[i + dx[1]][j + dy[1]]
        cost += flower_list[i + dx[2]][j + dy[2]]
        cost += flower_list[i + dx[3]][j + dy[3]]
        cost_list.append((cost,i,j))

buy = False
final_cost1 = cost_list[0]
final_cost2 = cost_list[1]
final_cost3 = cost_list[2]

while not buy:
'''
# 이렇게 하면 너무 복잡해진다. 같은 자리인지 확인할 수있는 더 효율적인 방법이 필요하다.

# 모범 풀이

N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

ans = 10000

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]


def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N # 크기 줄이기
        y = flower % N # 크기 줄이기
        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return 10000

        for w in range(5):
            flow.append((x + dx[w], y + dy[w]))
            ret += G[x + dx[w]][y + dy[w]]

    if len(set(flow)) != 15: # 정말 중요하다. 같은 자리가 점유당하는지 확인 위해 set을 쓴다!
        return 10000
    return ret


for i in range(N * N):
    for j in range(i + 1, N * N):
        for k in range(j + 1, N * N):
            ans = min(ans, ck([i, j, k]))

print(ans)



