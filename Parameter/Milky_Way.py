C,M = list(), list()

for i in range(3):
    a,b = map(int,input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i%3
    nxt = (idx+1)%3
    # 현재양 -(다음 비커에서 부족한 양) > 0 : 현재 비커에서 주고도 남늠다.
    # 현재양 -(다음 비커에서 부족한 양) < 0 : 현재 비커에서 주면 우유가 부족하다.
    M[idx],M[nxt] = max(M[idx]-(C[nxt]-M[nxt]),0),min(C[nxt],M[nxt]+M[idx])

for i in M:
    print(i)