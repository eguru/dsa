import sys
from collections import OrderedDict


class Graph(object):

    def __init__(self, vertices):
        self.vertices = OrderedDict()
        for vertex in vertices:
            self.vertices.setdefault(vertex, [])

    def addEdge(self, u, v):
          self.vertices[u].append(v)

    def explore(self, vertex, visited, stack):
        visited[vertex] = True
        for child in self.vertices[vertex]:
            if not visited[child]:
                self.explore(child, visited, stack)
        # parent vertex should have all its children in the stack
        # if not then we have a cycle
        for child in self.vertices[vertex]:
            if str(child) not in stack:
                print "Child not in stack, possible cycle: ", child
                print "Children of vertex: ", vertex, " => ", self.vertices[vertex]
                print "Stack: ", stack
        stack.insert(0, str(vertex))            

    def topological_sort(self):
        stack = []
        visited = { v:False for v in self.vertices }
        for vertex in self.vertices:
            if not visited[vertex]:
                self.explore(vertex, visited, stack)

        print ", ".join(stack)

def alpha():
    vertices = list("ABCDEFGH")
    g = Graph(vertices)

    g.addEdge(vertices[0], vertices[2]) # A - C
    g.addEdge(vertices[1], vertices[2]) # B - C
    g.addEdge(vertices[1], vertices[3]) # B - D
    g.addEdge(vertices[2], vertices[4]) # C - E
    g.addEdge(vertices[3], vertices[5]) # D - F
    g.addEdge(vertices[4], vertices[7]) # E - H
    g.addEdge(vertices[4], vertices[5]) # E - F
    g.addEdge(vertices[5], vertices[6]) # F - G

    g.topological_sort()   

def numeric():
    vertices = [1, 2, 3]
    g = Graph(vertices)

    g.addEdge(vertices[0], vertices[1]) # 1 - 2
    g.addEdge(vertices[1], vertices[2]) # 2 - 3
    g.addEdge(vertices[2], vertices[0]) # 3 - 1
    g.topological_sort()

def numeric1():
    vertices = [2, 3, 4, 5]
    g = Graph(vertices)

    g.addEdge(vertices[0], vertices[1]) # 2 - 3
    g.addEdge(vertices[0], vertices[2]) # 2 - 4
    g.addEdge(vertices[1], vertices[3]) # 3 - 5
    g.addEdge(vertices[2], vertices[3]) # 4 - 5
    g.topological_sort()  

def numeric2():
    vertices = [5, 7, 3, 11, 8, 2, 9, 10]
    g = Graph(vertices)
    edges = (
            (5,11), 
            (7,11), 
            (7,8), 
            (3,8), 
            (3,10), 
            (11,2), 
            (11,9), 
            (11,10), 
            (8,9), 
    )
    for u,v in edges:
        g.addEdge(u,v)

    g.topological_sort()   

def numeric3():
    vertices = [5, 4, 2, 0, 1, 3]
    g = Graph(vertices)
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    g.topological_sort()   

def beta():
    vertices = list("ABCD")
    g = Graph(vertices)
    g.addEdge("A", "B")
    g.addEdge("B", "C")
    g.addEdge("C", "D")
    g.addEdge("D", "A")
    g.topological_sort()   

if __name__ == "__main__":

    if sys.argv[1] == "a":
        alpha()
    elif sys.argv[1] == "b":
        beta()       
    elif sys.argv[1] == "0":
        numeric()       
    elif sys.argv[1] == "1":
        numeric1()       
    elif sys.argv[1] == "2":
        numeric2()
    elif sys.argv[1] == "3":
        numeric3()


