
class Fila:
    def __init__(self,itens = []):
        self._itens = itens

    def vazia(self):
        return self._itens == []

    def add(self,item):
        self._itens.insert(0,item)    

    def remove(self):
        self._itens.pop(0)
    def size(self):
        return len(self._itens)    
    def topo (self):
        return self._itens[len(self._itens)-1]
    def __len__(self):
      return len(self._itens)        