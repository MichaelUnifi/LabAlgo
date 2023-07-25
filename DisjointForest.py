import Graph
class Object:
    def __init__(self, node):
        self.node = node
        self.parent = self

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
        obj = Object(node)
        node.setObject(obj)
        self.sets.append(obj)

    def findSet(self, obj):
        if obj != obj.parent:
            obj.parent = self.findSet(obj.parent)
        return obj.parent

    def link(self, obj1, obj2):
            self.sets.remove(self.findSet(obj2))
            obj2.parent = obj1

    def union(self, obj1, obj2):
        self.link(self.findSet(obj1), self.findSet(obj2))
