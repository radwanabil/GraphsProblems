class Maze:
    def __init__(self, size):
        self.maze = [[0 for i in range(size)] for i in range(size)]

    def set_maze(self, row, col, val):
        self.maze[row][col] = val

    def solve_maze(self):
        coordinates = [0, 0]
        X = coordinates[0]
        Y = coordinates[1]
        goal = len(self.maze[0]) - 1
        visited = []
        list = []
        list.append(coordinates)

        while len(list) != 0:
            temp = list[-1]  # temp = COORDINATES (x,y)
            x = temp[0]
            y = temp[1]
            if x == goal and y == goal:
                break
            if temp not in visited:
                Input = False

            if 0 <= y + 1 < len(self.maze[1]) and self.maze[x][y + 1] == 0 and [x, y + 1] not in visited:
                list.append([x, y + 1])
                Input = True

            elif 0 <= y - 1 < len(self.maze[1]) and self.maze[x][y - 1] == 0 and [x, y - 1] not in visited:
                list.append([x, y - 1])
                Input = True

            elif 0 <= x + 1 < len(self.maze[1]) and self.maze[x + 1][y] == 0 and [x + 1, y] not in visited:
                list.append([x + 1, y])
                Input = True

            elif 0 <= x - 1 < len(self.maze[1]) and self.maze[x - 1][y] == 0 and [x - 1, y] not in visited:
                list.append([x - 1, y])
                Input = True

            visited.append(temp)
            if not Input:
                list.pop()

        if len(list) == 0:
            print('No valid path')
            return
        else:
            for i in range(len(list)):
                print(list[i])
            return



maze = int(input( "please enter N: "))


m = Maze(maze)
print("please enter values for maze, row by row: ")
for i in range(maze):
  inp= input()
  for j in range(maze):
      value = int(inp[j])

      m.set_maze(i,j,value)



m.solve_maze() 