class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.list = None

    def getKey(self):
        return self.key

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
        list = List(node)
        self.set.append(list)


    def findSet(self, node):
        return node.getList().getHead()

    def union(self, node1, node2):
        list1 = node1.getList()
        list2 = node2.getList()
        self.set.remove(list2)
        list1.getTail().setNext(list2.getHead())
        list1.setTail(list2.getTail())
        node = list2.getHead()
        while node != None:
            node.setList(list1)
            node = node.getNext()
        list1.setSize(list1.getSize() + list2.getSize())

    def weightedUnion(self, node1, node2):
        if node1.getList().getSize() >= node2.getList().getSize():
            self.union(node1, node2)
        else:
            self.union(node2, node1)


class List:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.size=1
        node.setList(self)

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setHead(self, node):
        self.head = node

    def setTail(self, node):
        self.tail = node

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size
