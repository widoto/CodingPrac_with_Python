def bfs(graph):
    # for 문이 돌아갈 때마다 visited를 초기화 하지 않아서 네트워크의 수가 온전히 갱신되도록
    visited=list()
    count=0
    for key in graph.keys():
        if key in visited:
            continue
        need_visit=list()
        need_visit.append(key)
        while need_visit:
            node = need_visit.pop(0)
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])
        # 서로 다른 네트워크의 수를 갱신한다.
        count += 1
    return count

def solution(n,computers):
    # 딕셔너리를 새로 만들어 준다.
    graph={}
    for i in range(len(computers)):
        graph[i]=[]
    for i in range(len(computers)):
        for j in range(i,len(computers)):
            if computers[i][j]==1 and i!=j:
                graph[i].append(j)
                graph[j].append(i)
    return bfs(graph)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))