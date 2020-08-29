from min_he_que import MinQueue
class Node:
    def __init__(self, label):
        self.label = label


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class WeightedGraph:
    def __init__(self):
        super().__init__()
        self.vertices = {}
        self.adjacencyList = {}

    def addNode(self, label):
        node = Node(label)
        if label not in self.vertices:
            self.vertices[label] = node
        if label not in self.adjacencyList:
            self.adjacencyList[node] = []

    def addEdge(self, start, end, weight):
        node = self.__getNode(start)
        self.adjacencyList.get(node).append(Edge(start, end, weight))
        node = self.__getNode(end)
        self.adjacencyList.get(node).append(Edge(end, start, weight))

    def shortestPath(self, start, end):
        visited = []
        shortest_path = {}
        self.__setShortestPaths(start, shortest_path)
        previous_path = {}
        node = self.vertices.get(start)
        self.__findShortestPath(visited, shortest_path, previous_path, node, end)
        path = self.__getPath(previous_path, end)
        print(f"Shortest Path = '{path}' with weight {shortest_path.get(end)}")

    def hasCycle(self):
        cycle = False
        for key in self.adjacencyList.keys():
            visited = []
            cycle = self.__checkCycle(visited, key, cycle, parent=None)
            if cycle:
                break
        return cycle

    def spanningTree(self):
        spanning_tree = {}
        visited = []
        node = self.__getKey()
        self.__findSpanningTree(node, spanning_tree, visited)
        self.__showSpanningTree(spanning_tree)

    def display(self):
        for key in self.adjacencyList.keys():
            print(f'{key.label} connected with {self.__getEdges(key, self.adjacencyList)}')

    def __getEdges(self, key, graph):
        edges = []
        for edge in graph.get(key):
            edges.append(f'{edge.start}->{edge.end}({edge.weight})')
        return edges

    def __getWeight(self, key):
        weight = []
        for weights in self.adjacencyList.get(key):
            weight.append(weights.weight)
        return weight

    def __getNode(self, start):
        for key in self.adjacencyList.keys():
            if key.label == start:
                return key

    def __findShortestPath(self, visited, shortest_path, previous_path, node, end):
        if node.label is None or node.label == end:
            return
        if node.label in visited:
            return
        visited.append(node.label)
        queue = MinQueue()
        for edge in self.adjacencyList.get(node):
            queue.enqueue(edge.weight, edge)
            if edge.weight + shortest_path.get(node.label) < shortest_path.get(edge.end):
                shortest_path[edge.end] = edge.weight + shortest_path.get(node.label)
                previous_path[edge.end] = edge.start
        sort_queue = []
        while not queue.isEmpty():
            sort_queue.append(queue.dequeue())
        for node in sort_queue:
            node = self.vertices.get(node[1].end)
            self.__findShortestPath(visited, shortest_path, previous_path, node, end)

    def __setShortestPaths(self, start, shortest_path):
        for key in self.vertices.keys():
            if key == start:
                shortest_path[key] = 0
            else:
                shortest_path[key] = 99999

    def __getPath(self, previous_path, end):
        get_nodes = end
        path = []
        path_string = ''
        while previous_path.get(get_nodes) is not None:
            path.append(previous_path.get(get_nodes))
            get_nodes = previous_path.get(get_nodes)
        for i in range(len(path)-1, -1, -1):
            path_string += path[i]
        return path_string

    def __checkCycle(self, visited, key, cycle, parent):
        visited.append(key.label)
        for node in self.adjacencyList.get(key):
            if node.end in visited and node.end != parent:
                cycle = True
                return cycle
            elif node.end != parent:
                parent = key.label
                key = self.vertices.get(node.end)
                self.__checkCycle(visited, key, cycle, parent)
        if cycle is not True:
            return False

    def __getKey(self):
        first_key = 0
        for key in self.adjacencyList.keys():
            first_key = key
            break
        return first_key

    def __findSpanningTree(self, node, spanning_tree, visited):
        visited.append(node.label)
        if spanning_tree.get(node) is None:
            spanning_tree[node] = []
        small_edge = self.__getSmallEdge(node, visited)
        if small_edge[1].end not in visited:
            spanning_tree.get(node).append(small_edge[1])
            key = self.vertices.get(small_edge[1].end)
            for edge in self.adjacencyList.get(key):
                if edge.weight == small_edge[1].weight:
                    spanning_tree[key] = [edge]
            node = key
            self.__findSpanningTree(node, spanning_tree, visited)

    def __getSmallEdge(self, node, visited):
        queue = MinQueue()
        for edge in self.adjacencyList.get(node):
            queue.enqueue(edge.weight, edge)
        small_edge = queue.dequeue()
        while small_edge[1].end in visited and not queue.isEmpty():
            small_edge = queue.dequeue()
        return small_edge

    def __showSpanningTree(self, spanning_tree):
        for key in spanning_tree.keys():
            print(f"{key.label} connected to {self.__getEdges(key, spanning_tree)}")


weightGraph = WeightedGraph()
weightGraph.addNode('a')
weightGraph.addNode('b')
weightGraph.addNode('c')
weightGraph.addNode('d')
weightGraph.addEdge('a', 'b', 3)
weightGraph.addEdge('a', 'c', 1)
weightGraph.addEdge('b', 'c', 2)
weightGraph.addEdge('b', 'd', 4)
weightGraph.addEdge('c', 'd', 5)
weightGraph.display()
print(weightGraph.hasCycle())
weightGraph.spanningTree()

