
class Node:
    def __init__(self,data = None):
        self._data = data
        self._next = None 

    #get e set de dado
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,novo):
        self._data = novo

    #get e set de prox

    @property
    def next(self):
        return self._next
    @next.setter
    def next (self,novo):
        self._next = novo    
