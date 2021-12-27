# #단순 nCr 계산하기
# import math
# print(math.factorial(5)/math.factorial(3)/math.factorial(2))

#응용문제 11번에서 15번 이항 누적 확률 분포표

import math
n = int(input())
success = int(input())
suc_rate= float(input())
sum = 0
for i in range(0,success+1):
    term = (math.factorial(n) / math.factorial(i)/math.factorial(n-i) * math.pow(suc_rate, i) * math.pow(1-suc_rate, n-i))
    print(term)
    sum += term
print(sum)

# #이항분포의 확률 질량함수 그니까 하나만 계산할때
import math
my = 5
suc = 1
my_rate = 0.25
result = math.factorial(my) / math.factorial(suc)/ math.factorial(my-suc) * math.pow(my_rate, suc) * math.pow(1-my_rate, my-suc)
print(result)

# #정규분포
# import math
# bun_san = float(input())
# seung = -1 * math.pow(1-1,2)/2 *bun_san *bun_san
# my_ans = 1/math.pow(2*math.pi,0.5)/bun_san*math.exp(seung)


