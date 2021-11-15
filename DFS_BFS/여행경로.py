from collections import defaultdict
# 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 값을 디폴트값으로 지정한다.

def dfs(graph, N, key, footprint):
    # N: 도달한 역의 개수, key: 현재 역. footprint: 방문 히스토리
    if len(footprint) == N + 1:
        return footprint # 모든 장소 방문시 종료

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp) # 깊이 우선 재귀!

        graph[key].insert(idx, country) # 다시 원상북구(다음 키값을 위해)

        if ret:
            return ret # 찾는 것이 나오면 중단하고 답내기. 알파벳 정렬 했으니 먼저 나오는 답이 답이다.


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets: # [a,b][b,c]로 칸이 2개 = 정거장은 칸+1개
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort() # 알파벳순 정렬

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# 최단 + 중복이없음 = 일반 dfs
# 최단 + 중복있음 = 재귀 dfs(feat.원상복구)