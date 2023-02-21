def inp():
    return(int(input()))


from collections import defaultdict

class Graph():
    def __init__(self,v):
        self.graph = defaultdict(list)
        self.V = v
        self.vertices = []
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:

            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[v] = False
        return False
 
    def isCyclic(self):
        visited = {}
        recStack = {}
        for v in self.vertices:
            visited[v] = False
            recStack[v] = False
        
        for node in self.vertices:
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

n = inp()

g = Graph(n)

for _ in range(n):
    ineq = input()
    
    if ineq[0] not in g.vertices:
        g.vertices.append(ineq[0])

    if ineq[4] not in g.vertices:
        g.vertices.append(ineq[4])

    if ineq[2] == '>':
        g.addEdge(ineq[0], ineq[4])
    
    else:
        g.addEdge(ineq[4], ineq[0])

if g.isCyclic() == 1:
    print(":(")
else:
    print(":)")