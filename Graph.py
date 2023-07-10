class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges