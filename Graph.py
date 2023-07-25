import DisjointList as dl
import DisjointForest as df

class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.components = []
        self.components_number = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    def getComponents(self):
        return self.components

    def getComponentsNumber(self):
        return self.components_number

    def find_connected_components_list_unweighted(self):
        list = dl.ListSet()
        for node in self.nodes:
            list.makeSet(node)
        for edge in self.edges:
            obj1 = edge[0].getObject()
            obj2 = edge[1].getObject()
            if list.findSet(obj1) != list.findSet(obj2):
                list.union(obj1, obj2)
        self.components = list.get_components()
        self.components_number = list.get_components_size()

    def find_connected_components_list_weighted(self):
        list = dl.ListSet()
        for node in self.nodes:
            list.makeSet(node)
        for edge in self.edges:
            obj1=edge[0].getObject()
            obj2=edge[1].getObject()
            if list.findSet(obj1) != list.findSet(obj2):
                list.weightedUnion(obj1, obj2)

    def find_connected_components_forest(self):
        forest = df.Forest()
        for node in self.nodes:
            forest.makeSet(node)
        for edge in self.edges:
            obj1 = edge[0].getObject()
            obj2 = edge[1].getObject()
            if forest.findSet(obj1) != forest.findSet(obj2):
                forest.union(obj1, obj2)

class Node:
    def __init__(self, key):
        self.key = key
        self.object = None

    def setObject(self, object):
        self.object = object

    def getObject(self):
        return self.object

    def getKey(self):
        return self.key
