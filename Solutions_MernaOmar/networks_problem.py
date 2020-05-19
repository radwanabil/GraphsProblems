import queue


class Network:
    def __init__(self, vertices):
        self.size = vertices
        self.edges = [[0 for i in range(vertices)] for i in range(vertices)]

    def add_edge(self, v1, v2):
        v1 = v1 - 1
        v2 = v2 - 1
        self.edges[v1][v2] = 1
        self.edges[v2][v1] = 1

    def calculate_distance(self, start, distance):  # GET PATH IS USED TO PRINT ALL CONNECTIONS OF A SINGLE GIVEN POINT
        start = start - 1

        q = queue.Queue()
        q.put(start)
        visited = [start]
        dis = [-1] * self.size
        dis[start] = 0
        while not q.empty():
            x = q.get()
            for i in range(self.size):
                # print(self.edges[x][i])
                if self.edges[x][i] == 1:
                    if dis[i] == -1:
                        dis[i] = dis[x] + 1
                        q.put(i)
        counter = 0
        for i in range(len(dis)):
            if (dis[i] == distance):
                counter = counter + 1
        print(counter)
        for i in range(len(dis)):
            if (dis[i] == distance):
                print(start + 1, i + 1)


N = Network(9)
N.add_edge(1, 2)
N.add_edge(2, 3)
N.add_edge(1, 7)
N.add_edge(2, 4)
N.add_edge(4, 7)
N.add_edge(7, 8)
N.add_edge(3, 4)
N.add_edge(7, 6)
N.add_edge(5, 6)
N.add_edge(9, 7)
N.calculate_distance(4, 2)
