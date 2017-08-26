'''
Created on 11 de ago de 2017

@author: CGCavalcante
'''
class Noh():
    def __init__(self,gufs=None):
        
        self.node = gufs
        self.pai = None
        self.fidireito = None
        self.fiesquerdo = None
        
    def setnode(self,id):
        self.node = id
        
    def getnode(self):
        return self.node
    
    def setpai(self,id):
        self.pai = id
        
    def getpai(self):
        return self.pai
    
    def setFidireito(self,gufs):
        self.fidireito= gufs
        
    def getFidireito(self):
        return self.fidireito

    def setFiesquerdo(self,gufs):
        self.fiesquerdo= gufs
        
    def getFiesquerdo(self):
        return self.fiesquerdo