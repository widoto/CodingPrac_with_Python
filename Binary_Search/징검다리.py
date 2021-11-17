# 문제: n개의 바위를 제거했을때 생기는 바위 사이 거리의 최솟값 중 최대값을 구하는 문제
# 이분탐색(최소값중 최대값을 찾아라)
def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    start = rocks[1] - rocks[0]
    for i in range(len(rocks)-1):
        if rocks[i+1] - rocks[i] < start:
            start = rocks[i+1] - rocks[i]
    end = rocks[-1] - rocks[0] # 최소 거리가 될 수 있는 가장 큰값과 작은 값을 초기값으로 설정

    while start <= end:
        mid = (start + end) // 2
        value = 0
        count = 0
        i = 0
        # 첫째 바위도 없어질 수 있다!
        while i != len(rocks):
            if rocks[i] >= value + mid:
                value = rocks[i]
                i += 1
            else: # 바위사이의 거리가 내가 설정한 mid 값보다 작을 때
                j = 1 # 커질 때까지 바위를 제거한다.

                while i+j <= len(rocks)-1 and rocks[i+j] < value + mid:
                    j += 1

                if i+j > len(rocks)-1: # 접근가능한 바위의 인덱스위치를 넘어버렸을때 아예 실행을 중단한다.
                    count += n+1
                    break

                else: # 접근가능한 인덱스 위치이며 제거 후 최소거리를 넘게 되었을 때
                    value = rocks[i + j]
                    count += j
                    i += j+1

        # 마지막 도착지와 바위 사이의 거리도 통과해야!
        if distance < value +mid:
            n += 1

        # 알맞은 답이라면
        if count == n:
            start = mid + 1 # 최소거리를 욕심내서 더 큰 거리를 잡는다.
            answer = mid

        elif count > n: # 제거해야 할 바위가 너무 많았다 = 최소거리를 너무 크게 잡았다.
            end = mid - 1
        else:
            start = mid + 1 # 거리를 너무 작게 잡았다. 최소거리를 욕심내서 더 큰 거리를 잡는다.

    return answer

print(solution(25,[2,14,11,21,17],2))