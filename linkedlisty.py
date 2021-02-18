class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def append(self, value):
        new_node = Node(value)
        if self.headval is None:
            self.headval = new_node
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextVal = new_node

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
