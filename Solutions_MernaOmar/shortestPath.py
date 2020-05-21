import collections
import heapq

def shortestPath(edges, source, destination):
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for start, end, t, c in edges:
        graph[start].append((c, end, t))
    # create a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, 0, [])], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    while queue:
        (cost, node, time, path) = heapq.heappop(queue)
        # visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # hit the destination
            if node == destination:
                if time==1:
                    total_time=time
                    cost = cost + (total_time * 100)
                else:
                    total_time = time+1
                    cost=cost+(total_time*100)
                print('The total hours is ', total_time)
                print('The total cost is ', cost, '$')
                print('The shortest path is ', path)
                return('Done')
            # visit neighbours
            for c, neighbour, t in graph[node]:
                if neighbour not in visited:

                    heapq.heappush(queue, (cost+c, neighbour, time+t,  path))
    return ("Doesn't exist")

if __name__ == "__main__":
    edges = [
        (1, 2, 1, 250),
        (1, 3, 1, 300),
        (1, 4, 2, 700),
        (2, 4, 1, 300),
        (3, 4, 1, 200),
    ]

    print("Find the shortest path between cities")
    print(edges)
    print("1 -> 4:")
    print(shortestPath(edges, 1, 4))