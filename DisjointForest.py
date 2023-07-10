class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class Forest:
    def __init__(self):
        self.sets = []

    def getSet(self):
        return self.sets

    def makeSet(self, node):
        self.sets.append(node)

    def findSet(self, node):
        if node != node.getParent():
            node.setParent(self.findSet(node.getParent()))
        return node.getParent()


    def link(self, node1, node2):
            self.sets.remove(self.findSet(node2))
            node2.setParent(node1)


    def union(self, node1, node2):
        self.link(self.findSet(node1), self.findSet(node2))
