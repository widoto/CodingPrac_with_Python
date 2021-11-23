DP = [1,0,0,0,0,0,0,0]

def nxt(state):
    tmp = [0 for _ in range(8)]
    # 주의사항: 이 TMP가 바로 STATE에적용되는 것이 아님을 알면 쉽게 이해할 수 있다.
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    return tmp

for i in range(int(input())):
    DP = nxt(DP)
print(DP[0]% 1000000007)