
def dijkstra(start_node,graph):
    unvisited={} #Dictionary
    visited={}

    for node in graph:
        unvisited[node]=float('inf')
    print(unvisited)    
       
    current=start_node
    current_distance=0
    unvisited[current]=current_distance


    while True:
        for neigbour_node, distance in graph[current].items():
            if neigbour_node not in unvisited:
                continue
            newDistance=current_distance + distance
            if unvisited[neigbour_node] is float('inf') or unvisited[neigbour_node]>newDistance:
                   unvisited[neigbour_node]=newDistance

        visited[current]=current_distance
        del unvisited[current]

        if not unvisited:
             break


        unvisited_items= [node for node in unvisited.items()]
        sorted_unvisited_items=sorted(unvisited_items,key=lambda x:x[1])
        current,current_distance=sorted_unvisited_items[0]
    
    
    return  visited  



start_node='A'
graph = {
    'B': {'A': 5, 'D': 35, 'E': 10},
    'A': {'B': 5, 'C': 10},
    'D': {'B': 35, 'C': 20, 'E': 10},
    'C': {'A': 10, 'D': 20, 'E': 30},
    'E': {'B': 10, 'D': 10, 'C': 30}
    }

result=dijkstra(start_node,graph)
print(result)