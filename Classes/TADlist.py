class TADlist:
    def __init__(
        self,
        counters={},
        datastructure='ARRAY_LIST',
        cmpfunction=None,
        key=None,
        filename=None,
        delimiter=","
        ):
        from DISClib.ADT import list as lt
        self.list = lt.newList()
        self.size=0
        self.first = None
        self.last = None
        self.empty = True
        self.counters = counters
        self.pylist = []
        self.lt = lt
    def __str__(self):
        return '''
        class            : TADlist
        created from     : DISClib.ADT.list
        funtions related : DISClib.ADT.list *
        \--------------
        Use the property ".help" to get all commands related
        '''
    
    @property
    def help(self):
        return '''
        .addLast(value):
            Add a value in the last position
        \--------------
        .addFirst(value):
            Add a value in the first position
        \--------------
        .getElement(position)
            Get any value in the list with the position (tad list, python list)
        \--------------
        .delete(position)
            Delete any value in the lists
        \--------------
        .removeFirst()
            Delete first element in the lists
        \--------------
        .removeLast()
            Delete last element in the lists
        .insertElement(position, value)
            Insert an element in any position
        '''
    def addLast(self, value):
        '''
        Add a value in the last position
        '''
        self.lt.addLast(self.list, value)
        self.pylist.append(value)
        self.empty = False
        self.first = self.lt.firstElement(self.list)
        self.last = value
        self.size += 1
    def addFirst(self, value):
        '''
        Add a value in the first position
        '''
        self.lt.addFirst(self.list, value)
        self.pylist.insert(0,value)
        self.empty = False
        self.first = value
        self.last = self.lt.lastElement
        self.size += 1
    
    def getElement(self, position):
        '''
        Get any value in the lists with the position
        '''
        return self.getElement(self.list, position), self.pylist[position-1]

    def delete(self, position):
        '''
        Delete any value in the lists
        '''
        self.lt.deleteElement(self.list, position)
        self.pylist.pop(position-1)
        if position == 1:
            self.first = self.pylist[0]
        elif position == self.size:
            self.last = self.pylist[-1]
        self.size -= 1
        if self.size == 0 :
            self.empty = True
    
    def removeFirst(self):
        '''
        Delete first element in the lists
        '''
        self.lt.removeFirst(self.list)
        self.pylist.pop(0)
        self.first = self.pylist[0]
        self.size -= 1
        if self.size == 0 :
            self.empty = True

    def removeLast(self):
        '''
        Delete last element in the lists
        '''
        self.lt.removeLast(self.list)
        self.pylist.pop()
        self.last = self.pylist[-1]
        self.size -= 1
        if self.size == 0 :
            self.empty = True
    
    def insertElement(self, position, value):
        '''
        Insert an element in any position
        '''
        self.lt.insertElement(self.list, position, value)
        self.pylist.insert(position-1,value)
        if position == 1:
            self.first = value
        elif position == self.size+1:
            self.last = value
        self.size += 1

    def exchange(self, position1, position2):
        '''
        Exchange 2 values with a specific positions
        '''
        self.lt.exchange(self.list, position1, position2)
        temp = self.pylist[position1-1]
        self.pylist[position1-1] = self.pylist[position2-1]
        self.pylist[position2-1] = temp

    def isPresent(self, value):
        '''
        Retruns the value's position
        '''
        return self.lt.isPresent(self.list, value)

