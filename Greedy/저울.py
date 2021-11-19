# 내 풀이
from itertools import permutations
T = int(input())
chu = list(map(int,input().split(' ')))


p_list =[]
for i in range(1,T+1):
    c_list = list(permutations(chu, i))
    for j in range(len(c_list)):
        p_list.append(sum(c_list[j]))

p_list = set(sorted(p_list))
print(p_list)
answer = 1
for i in range(len(p_list)):
    if answer not in p_list:
        break
    else:
        answer += 1

# 시간 초과가 난다.
# 다음과 같은 풀이가 모범
# 탐욕스럽다.
# 정렬한 배열의 원소를 짚어가며 원소를 ans에 더한값보다 작으면 1부터 ans까지는 모두 표현할 수 있다는 뜻이다.

N,A= int(input()),sorted(list(map(int,input().split())))

ans =0
for i in A:
    if i<=ans +1:
        ans +=i
    else:
        break
print(ans+1)





