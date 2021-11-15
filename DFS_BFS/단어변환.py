# 한 글자만 다른지 살펴봐주는 코드
def compare(node, words):
    c=0
    for i in range(len(node)):
        if node[i] != words[i]:
            c+=1
    if c==1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    # 현재의 노드를 visited 처리할 것인지, 다음 노드를 visited 처리할 것인지 정해야함.
    visited = [begin]
    need_visit =[]
    # 각 노드별로 count를 세기 위하여 튜플 이용
    need_visit.append((begin,0))
    answer = 1000000001

    while need_visit:
        node = need_visit.pop()
        Node = node[0]
        for i in range(len(words)):
            if(compare(Node,words[i])) and words[i] not in visited:
                if words[i]==target: # 다음 단어가 답이라면 visited 처리는 하지 않는다.
                    answer = min(answer, node[1]+1)
                    continue
                visited.append(words[i])
                need_visit.append((words[i],node[1]+1))

    return answer

print(solution("hit","cog",[["hot", "dot", "dog", "lot", "log"]]))