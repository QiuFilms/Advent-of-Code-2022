import string
f = open("input.txt")
grid = {}

def formatData(coordinates,value):
    global startPoint, endPoint

    if "S" in value:
        startPoint = coordinates
        return string.ascii_lowercase.index("a")

    if "E" in value:
        endPoint = coordinates
        return string.ascii_lowercase.index("z")
    return string.ascii_lowercase.index(value)


for index, line in enumerate(f):
    data = line.strip()

    for x in range(len(data)):
        coordinates = (index, x)
        grid[coordinates] = formatData(coordinates,data[x])


class Point:
    def __init__(self, point):
        self.point = point
        self.neighbours = self.__neighbours()

    def __neighbours(self):
        height, width = list(grid)[-1]
        y, x = self.point

        neighbours = list()
        if x+1 <= width and (grid[self.point] >= grid[(y, x+1)] or grid[self.point] + 1 == grid[(y, x+1)]):
            neighbours.append((y, x+1))
        if x-1 >= 0 and (grid[self.point] >= grid[(y, x-1)] or grid[self.point] + 1 == grid[(y, x-1)]):
            neighbours.append((y, x-1))
        if y+1 <= height and (grid[self.point] >= grid[(y+1, x)] or grid[self.point] + 1 == grid[(y+1, x)]):
            neighbours.append((y+1, x))
        if y-1 >= 0 and (grid[self.point] >= grid[(y-1, x)] or grid[self.point] + 1 == grid[(y-1, x)]):
            neighbours.append((y-1, x))

        if neighbours:
            return neighbours
        return None

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def BFS(self, point):
        visited = list()
        queue = list()
        queue.append([point,0])
        visited.append(point)
 
        while queue:
            value, distance = queue.pop(0)
            neighbours = Point(value).neighbours

            if value == endPoint:
                print(distance)
                break
            for i in neighbours:
                if i not in visited:  
                    queue.append([i, distance+1])
                    visited.append(i)

graph = Graph(grid)
graph.BFS(startPoint)
