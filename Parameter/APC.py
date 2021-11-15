# 내 풀이
N,L,K=map(int,input().split())
level =[]
for _ in range(N):
    sub1,sub2 = map(int,input().split())
    if sub2<=L:
        level.append(2)
        continue
    elif sub1<=L:
        level.append(1)

level = sorted(level,reverse=True)
answer=0
current_k =0

for i in range(len(level)):
    if current_k>=K:
        break
    if level[i]==1:
        answer+=100
    else:
        answer+=140
    current_k+=1

print(answer)

# 정석 풀이
N,L,K = map(int,input().split())

easy,hard =0,0

for i in range(N):
    sub1,sub2 = map(int,input().split())
    if sub2 <=L:
        hard +=1
    elif sub1<=L:
        easy+=1

# hard문제
ans = min(hard,K)*140
# easy
if hard<K:
    ans+=min(K-hard,easy)*100
print(ans)
# 리스트를 굳이 만들지 않아도 변수를 할당하여 해결할 수도 있었다.