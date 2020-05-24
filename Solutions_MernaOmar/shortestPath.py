import collections
import heapq


def shortestPath(edges, source, destination,M):
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
                    cost=cost+(total_time*M)
                print('The total hours is ', total_time)
                print('The total cost is ', cost, '$')
                print('The shortest path is ', path)
                return('Done')
            # visit neighbours

            for c, neighbour, t in graph[node]:
                if neighbour not in visited:

                    heapq.heappush(queue, (cost+c, neighbour, time+t,  path))
    return ("Doesn't exist")
def addEdges(edges,v1,v2,hours,cost):

    edges.append((v1, v2, hours, cost))




M = int(input("Please Enter Amount M "))
vertices = int(input("Please Enter Number Of Citites "))
routes = int(input("Please Enter Number Of Routes "))
edges=[]
cities=[]
x=1
while x ==1:
    for x in range(routes) :

        v1 = int(input("enter the source  "))
        if v1 not in cities:
            if len(cities) != vertices:
                cities.append(v1)

            else:
                print("You have exceeded the specified number for cities")
                break

        v2 = int(input("enter the destination "))
        if v2 not in cities:
            if len(cities) != vertices:
                cities.append(v2)

            else:
                  print("You have exceeded the specified number for cities")
                  break


        while v2 == v1 :
            print(" the estination can't be also the source  ")
            v1 = int(input("enter the source  "))
            v2 = int(input("enter the destination "))

        hours = int(input("enter the time "))
        cost = int(input("enter the cost "))
        addEdges(edges,v1,v2,hours,cost)
        x = + 1
    source = int(input("Please Enter Source City"))
    dest = int(input("Please Enter Destination City"))
    print("Find the shortest path between cities")

    print(shortestPath(edges, source, dest,M))

 






