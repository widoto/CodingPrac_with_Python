graph = {'verticles':['A','B','C','D','E','F','G'],
         'edges' :[(7,'A','B'), (3,'C','B'), (7,'D','A'), (7,'E','F')]}

parent = dict()
rank = dict()

def make_set(node): #초기화
    parent[node] = node
    rank[node] =0

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    if rank[root1] > rank[root2]:
        parent[root2] = root1

    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] +=1

def kruskal(graph):
    mst = list()
    for node in graph['verticles']:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight,node_v,node_u = edge
        if find(node_v) != find(node_u):
            union(node_v,node_u)
            mst.append(edge)

    return mst