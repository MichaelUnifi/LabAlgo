import Graph

class Object:
    def __init__(self, node):
        self.node = node
        self.next = None
        self.list = None

    def getNode(self):
        return self.node

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getList(self):
        return self.list

    def setList(self, list):
        self.list = list


class ListSet:
    def __init__(self):
        self.set = []

    def getSet(self):
        return self.set

    def makeSet(self, node):
        obj = Object(node)
        node.setObject(obj)
        list = List(obj)
        self.set.append(list)

    def findSet(self, obj):
        return obj.list.head

    def union(self, obj1, obj2):
        list1 = obj1.getList()
        list2 = obj2.getList()
        self.set.remove(list2)
        list1.tail.setNext(list2.head)
        list1.setTail(list2.tail)
        node = list2.head
        while node != None:
            node.setList(list1)
            node = node.next
        list1.setSize(list1.size + list2.size)

    def weightedUnion(self, obj1, obj2):
        if obj1.list.size >= obj2.list.size:
            self.union(obj1, obj2)
        else:
            self.union(obj2, obj1)

    def get_components(self):
        components = []
        for list in self.set:
            components.append(list.head.node.getKey())
        return len(components)

    def get_components_size(self):
        components = []
        for list in self.set:
            components.append(list.size)
        return components


class List:
    def __init__(self, obj):
        self.head = obj
        self.tail = obj
        self.size=1
        obj.setList(self)

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setHead(self, obj):
        self.head = obj

    def setTail(self, obj):
        self.tail = obj

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size
