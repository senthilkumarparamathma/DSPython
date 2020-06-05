from collections import defaultdict

class Graph:
    def __init__(self):
        # adjacency list implemenation #dictionary . { key1: [a], key2 : [a,b]}
        #self.graph = {}
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        '''
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)
        '''
        self.graph[start].append(end)

    def bfs(self, start):
        visited = {}
        queue = []
        queue.append(start)
        resultpath = []
        while queue:
            s = queue.pop(0)
            visited[s] = 1
            resultpath.append(s)
            print(s)
            for nearestnode in self.graph[s]:
                if nearestnode not in visited:
                    queue.append(nearestnode)
                    visited[nearestnode] = 1
        print(resultpath)
        return resultpath
        # Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.

    def dfs(self, start):
        visited = {}
        stack = []
        stack.append(start)
        resultpath = []
        while stack:
            s = stack.pop()
            visited[s] = 1
            resultpath.append(s)
            print(s)
            for node in self.graph[s]:
                if node not in visited:
                    stack.append(node)
                    visited[s] = 1
        print(resultpath)
        return resultpath
        # Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.


    #Find if there is a path between two vertices in a directed graph
    # we can use BFS apporach  and if start and end match then there is path between node
    def isPathBetweenNode(self, start, end):
        visited = {}
        queue = []
        queue.append(start)
        #resultpath = []
        while queue:
            s = queue.pop(0)
            visited[s] = 1
            #resultpath.append(s)
            if s == end:
                return True
            # print(s)
            for nearestnode in self.graph[s]:
                if nearestnode not in visited:
                    queue.append(nearestnode)
                    visited[nearestnode] = 1
        # print(resultpath)
        return False



    def pathBetweenNodeBFS(self,start,end):
        visited = {}
        queue = []
        queue.append(start)
        resultpath = []
        while queue:
            s = queue.pop(0)

            visited[s] = 1
            resultpath.append(s)
            if s ==end:
                print("----path--{0}".format(resultpath))
                return resultpath
            #print(s)
            for nearestnode in self.graph[s]:
                if nearestnode not in visited:
                    queue.append(nearestnode)
                    visited[nearestnode] = 1
        #print(resultpath)
        return resultpath


    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
       # if not self.graph.has_key(start):
           # return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: return newpath
        return None


    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
       # if not self.graph.has_key(start):
            #return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    #Depth First Traversal can be used to detect a cycle in a Graph
    def isCycle(self, start):
        visited = {}
        stack = []
        stack.append(start)
        while stack:
            s = stack.pop()
            # print(visited)
            if s in visited.keys() and visited[s] == True:
                return True
            visited[s] = True
            stack.extend(self.graph[s])
        return False

    def checkCycle(self):
        vertex = []

        for v in self.graph.keys():
            vertex.append(v)

        for v in vertex:
            if self.isCycle(v):
                return True

        return False

g = Graph()

'''
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.addEdge(0, 4)
g.addEdge(5,6)
'''

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)

'''
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(7, 7)
'''

print ("Following is Breadth First Traversal"
       " (starting from vertex 1)")
g.bfs(1)

print ("Following is Depth First Traversal"
       " (starting from vertex 1)")
g.dfs(1)
# [1, 3, 5, 6, 7, 2, 4]


print(g.isPathBetweenNode(5,6))
print(g.isPathBetweenNode(1,6))


print("path by BFS :")
g.pathBetweenNodeBFS(0,5)



print("**find_path**")
print(g.find_path(0,5))
print("~~find_all_paths~~")
print(g.find_all_paths(0,5))


g = Graph()


g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(6, 7)
#g.addEdge(5,2)
g.addEdge(1,3)

print("Is Cycle :{0}".format(g.checkCycle()))


#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
