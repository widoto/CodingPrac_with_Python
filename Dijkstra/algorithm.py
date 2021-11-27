import heapq

my_graph ={
    'A':{'B':8, 'C':3},
    'B':{},
    'C':{'E':3,'F':5}
}

def dijkstra(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start]=0

    queue =[]
    heapq.heappush(queue,[distances[start],start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent,weight in graph[current_node].items():
            distance = current_distance+weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance,weight])
    return distances

print(dijkstra(mygraph,'A'))
