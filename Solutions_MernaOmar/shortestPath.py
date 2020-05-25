import collections
import heapq
import sys


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
vertices = int(input("Please Enter Number Of Cities "))
routes = int(input("Please Enter Number Of Routes "))
edges=[]
cities=[]


for d in range(routes) :
        print("\nAdding New Route: ")
        v1 = int(input("Please Enter The Source  "))
        if v1 not in cities:
            if len(cities) != vertices:
                cities.append(v1)

            else:
                print("You Have Exceeded The Specified Number For Cities")
                break

        v2 = int(input("Please Enter The Destination "))

        if v2 not in cities:
            if len(cities) != vertices:
                cities.append(v2)

            else:
                  print("You Have Exceeded The Specified Number For Cities")
                  break


        while v2 == v1 :
            print("WARNING :  The Destination Can't Be Also The Source  ")
            v1 = int(input("Please Enter The Source  "))
            v2 = int(input("Please Enter The Destination "))

        hours = int(input("Please Enter The time "))
        cost = int(input("Please Enter The cost "))
        addEdges(edges,v1,v2,hours,cost)
        d = + 1
x=1
while x==1:
        source = int(input("Please Enter Source City Of The Journey"))
        dest = int(input("Please Enter Destination City Of The Journey"))
        while source == dest:
                print("WARNING :  The Destination Can't Be Also The Source  ")
                v1 = int(input("Please Enter Source City Of The Journey"))
                v2 = int(input("Please Enter Destination CityOf The Journey "))
        print(shortestPath(edges, source, dest,M))

        x= input("Do You want to check another path? \nYes = Enter 1\nNo= Enter 0")
        while (x is not '0' and x is not  '1'):
            x = input("WARNING :  Invalid Value, Do You Want To Check Another Path? \nYes = Enter 1\n No = Enter 0")












