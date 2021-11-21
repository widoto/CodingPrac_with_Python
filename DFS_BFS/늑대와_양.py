# 늑대와 양

R,C= map(int, input().split())
M = [list(input()) for i in range(R)]

dx,dy=[0,1,0,-1],[1,0,-1,0]

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j]=='W':
            for w in range(4):
                ii,jj = i + dx[w], j+ dy[w]
                if ii<0 or ii==R or jj<0 or jj==C:
                    continue
                if M[ii][jj]=='S':
                    # 늑대 바로 옆에 양이 있으면 울타리를 설치할 수 없다.
                    ck = True
if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j]='D'
    for i in M:
        print(''.join(i))