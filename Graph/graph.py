class Node:
    def __init__(self, string):
        self.label = string


class Graph:
    def __init__(self):
        super().__init__()
        self.vertices = {}
        self.adjacencyList = {}

    def addNode(self, label):
        node = Node(label)
        if label not in self.vertices:
            self.vertices[label] = node
        if label not in self.adjacencyList:
            self.adjacencyList[node ] = []

    def removeNode(self, label):
        if label not in self.vertices:
            return
        self.vertices.pop(label)
        self.__removeAdjacency(label)
        self.__removeAdjEdge(label)

    def addEdge(self, start, end):
        start = self.vertices.get(start)
        end = self.vertices.get(end)
        self.adjacencyList.get(start).append(end)

    def removeEdge(self, start, end):
        start, end = self.__removeNodeValues(start, end)
        if end in self.adjacencyList.get(start):
            self.adjacencyList.get(start).remove(end)

    def depthTransverse(self, node):
        transversed = []
        self.__depthTransverse(transversed, node)
        return transversed

    def breadthTransverse(self, node):
        queue = [node]
        transversed = []
        self.__breadthTransverse(queue, transversed)
        return transversed

    def topologicalSort(self):
        stack = []
        if not self.hasCycle():
            self.__topologicalSort(stack, self.__getTopologyKey())
        else:
            return "Graph have Cycle. So topological Sort can't perform"
        return self.__popStack(stack)

    def hasCycle(self):
        cycle = False
        for key in self.adjacencyList.keys():
            visited = []
            cycle = self.__checkCycle(visited, key, cycle)
            if cycle:
                break
        return cycle

    def display(self):
        for key in self.adjacencyList.keys():
            print(f'{key.label} connected to {self.__getEdges(key)}')

    def __getEdges(self, key):
        connections = []
        for node in self.adjacencyList.get(key):
            connections.append(node.label)
        return connections

    def __removeAdjacency(self, label):
        for node in self.adjacencyList.keys():
            if node.label == label:
                remove_node = node
        self.adjacencyList.pop(remove_node)

    def __removeAdjEdge(self, label):
        for key in self.vertices.keys():
            self.removeEdge(key, label)

    def __removeNodeValues(self, start, end):
        for node in self.adjacencyList.keys():
            if node.label == start:
                start = node
        for node in self.adjacencyList.get(start):
            if node.label == end:
                end = node
        return start, end

    def __depthTransverse(self, transversed, node):
        if node in transversed:
            return
        if node is None:
            return
        transversed.append(node)
        for key in self.adjacencyList.keys():
            if key.label == node:
                node = key
        if self.adjacencyList.get(node) is not None:
            for obj in self.adjacencyList.get(node):
                self.__depthTransverse(transversed, obj.label)

    def __breadthTransverse(self, queue, transversed):
        if len(queue) > 0:
            if queue[0] not in transversed:
                transversed.append(queue[0])
            for key in self.adjacencyList.keys():
                if key.label == queue[0]:
                    nodes = key
            if self.adjacencyList.get(nodes) is not None:
                for node in self.adjacencyList.get(nodes):
                    queue.append(node.label)
            queue.pop(0)
            self.__breadthTransverse(queue, transversed)

    def __topologicalSort(self, stack, key):
        if key is None:
            return
        if key.label not in stack:
            for node in self.adjacencyList.get(key):
                self.__topologicalSort(stack, node)
            if key.label not in stack:
                stack.append(key.label)

    def __getTopologyKey(self):
        for key in self.adjacencyList.keys():
            return key

    def __popStack(self, stack):
        topological_sort = ''
        for i in range(len(stack)-1, -1, -1):
            topological_sort += stack[i]
        return topological_sort

    def __checkCycle(self, visited, key, cycle) -> bool:
        visited.append(key.label)
        for node in self.adjacencyList.get(key):
            if node.label in visited:
                cycle = True
                return cycle
            else:
                return self.__checkCycle(visited, node, cycle)
        if cycle is not True:
            return False



graph = Graph()
graph.addNode('x')
graph.addNode('a')
graph.addNode('b')
graph.addNode('p')
graph.addEdge('x', 'a')
graph.addEdge('x', 'b')
graph.addEdge('a', 'p')
graph.addEdge('b', 'p')
graph.addEdge('p', 'x')
graph.display()
#print(f'Depth Transverse : {graph.depthTransverse("a")}')
#print(f'Depth Transverse : {graph.breadthTransverse("a")}')
print(graph.topologicalSort())