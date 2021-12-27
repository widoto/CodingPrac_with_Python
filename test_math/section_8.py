import math
print(1.96*math.pow(0.689*0.311/260 + 0.556*0.444/250, 0.5))

#단순 루트 계싼
import math
print(math.pow(0.5149*0.4851*(1/450+1/490),0.5))
#응용문제 11번:  확률변수의 분산과 평균
import math
jesi_list55 = list(map(int,input().split(' ')))
gop_list55 = list(map(float,input().split(' ')))
average55=0
for j in range(len(jesi_list55)):
    average55 += jesi_list55[j] * gop_list55[j]
average55 = average55
print(average55)

sum55=0
for i in range(len(jesi_list55)):
    sum55 += (math.pow(jesi_list55[i] ,2) * gop_list55[i])
print("분산은", sum55 - average55*average55)

#응용문제 19번 표본평균과 표본 분산, gop이 확률이 아닐때
import math
number_lists = list(map(float,input().split(' ')))
average = sum(number_lists)/len(number_lists)
print("소수 몇째자리까지 중간에 잘라야 하는지 확인하시오")
print("표본평균은 ", average)
#
sum22=0
for i in range(len(number_lists)):
     sum22 += (number_lists[i] - average)*(number_lists[i] - average)
print(sum22)
print("개수 1뺀 값인지 확인하시오")
print("표본분산은 ", sum22/(len(number_lists)-1))
print("표본표준편차는 ", math.pow(sum22/(len(number_lists)-1),0.5))
#9.59 4.62 0.65 7.75 16.98 11.78 7.24 10.15 25.49 11.44 10.37 9.33 15.04 12.16 16.63 12.06 9.7 12.46 8.05 19.91 5.58 12.48 4.35 16.41 22.53 17.56 18.4 10.86 27.43 7.39 14.57 11.92 2
#25 29 28 26 22 25 39 20 31 27 23 29 26 29 27 38 27 32 23 23 35 28 25 21 30 35 20 34 29 28 38 26 30 31 27 32 25 29 34 27 23 29 38 27 32 29 27 32 26 26


#심화 30번 표본 평균에서 크기가 u인 표본을 뽑을때
from fractions import Fraction
import math
from itertools import product
from itertools import permutations #이게 자기자신까지 되나?
u = int(input())
jesi_list2 = list(map(int,input().split(' ')))
#gop_list2 = list(map(int,input().split(' ')))
#gop_list2 = [Fraction(1,4), 0.25, Fraction(1,4), 0.25]
gop_list2 = [Fraction(1,4),Fraction(1,4),Fraction(1,4), 0.25]
#가능한 re_jesi_list만들기
re_jesi_list={}
list1=[]
for i in product(jesi_list2, repeat=u):
    list1.append(i)
print(list1)
for i in range(len(list1)):
    if Fraction(sum(list1[i])/u) not in re_jesi_list:
        re_jesi_list[sum(list1[i])/u] = 0
    sum7 =1
    for j in range(u):
        sum7*=(gop_list2[jesi_list2.index(list1[i][j])])
    re_jesi_list[sum(list1[i])/u] += sum7

print(re_jesi_list)
#그에 맞는 re_gop_list
#그걸로 다시 모평균과 모분산 만들기
sum5 =0
#키를 훝어야
for key in re_jesi_list.keys():
    sum5 += key * re_jesi_list[key]
print("표본평균의 평균은 ", sum5)
sum6=0

for key in re_jesi_list.keys():
    sum6 += key *key* re_jesi_list[key]

print("표본평균의 분산은", (sum6 - sum5*sum5))

