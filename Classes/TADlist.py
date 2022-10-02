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
            Add a value:any in the TAD list    
        '''
    def addLast(self, value):
        '''
        Add a value:any in the TAD list
        '''
        self.lt.addLast(self.list, value)
        self.empty = False
        self.first = self.lt.firstElement(self.list)
        self.last = value
        self.size += 1

