def solution(N, number):
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. 원리
    # i는 1부터 7까지이고, s[i]는 i+1개의 N이 있다.
    # i = 3일때, N은 4개이며, 따라서 1+3을 계산하기 위하여 j은 0과 2여야 한다.
    # 즉, N의 개수와 인덱스 숫자는 같지 않음을 조심해야 한다.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer