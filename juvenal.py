'''
Created on 11 de ago de 2017

@author: CGCavalcante
'''
class Noh():
    def __init__(self,id=None):
        self.node = id
        self.pai = None
        self.filhos = []
        
    def setnode(self,id):
        self.node = id
        
    def getnode(self):
        return self.node
    
    def setpai(self,id):
        self.pai = id
        
    def getpai(self):
        return self.pai
    
    def setFilhos(self,id):
        self.filhos.append(id)
        
    def getFilhos(self,id,operador):
        return self.filhos

