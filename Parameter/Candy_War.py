T = int(input())

for _ in range(T):
    c = int(input())
    child = list(map(int,input().split()))
    # 홀수개의 캔디를 가진 아이들에게짝수개로 맞추어주는 과정
    for i in range(len(child)):
        if child[i]%2==1:
            child[i]+=1
    answer=0
    while True:
        # 모든 아이들의 캔디 개수가 같으면 중단
        if len(set(child))==1:
            break
        # 옆 친구에게 나누어줄 캔디 준비
        half_child=[]
        for i in range(len(child)):
            half_child.append(child[i]//2)
            child[i] = child[i]//2
        # 나누어주기
        for j in range(1,len(child)):
            child[j] += half_child[j-1]
        child[0] += half_child[-1]
        # 다시 홀수개의사탕을 가진 아이들에게 사탕을 보충해줌.
        for i in range(len(child)):
            if child[i]%2==1:
                child[i]+=1
        answer+=1

    print(answer)

# 정석풀이
def check(N,candy):
    for i in range(N):
        if candy[i]%2==1:
            candy[i]+=1
    return len(set(candy))==1

def teacher(N,candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx]%2:
            candy[idx] +=1
        candy[idx]//=2
        tmp_lst[(idx+1)%N] = candy[idx]

    for idx in range(N):
        candy[idx]+=tmp_lst[idx]

    return candy

def process():
    N,candy = int(input()),list(map(int,input().split()))
    cnt=0
    while not check(N,candy):
        cnt+=1
        candy = teacher(N,candy)
    print(cnt)

for i in range(int(input())):
    process()

# 함수로 나누어 풀면 더 보기 좋다.