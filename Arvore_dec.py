'''
Created on 20 de ago de 2017

@author: CGCavalcante
'''
from juvenal import Noh

class arvore():
    def __init__(self):
        self.raiz = None
        self.antes = None
        self.lista = None
        
    def arquivo(self):
        decide = open('treloso.txt', 'r+')
        l_decide = decide.readlines()
        decide.close
        
        for indice, elemento in enumerate(l_decide):
            l_decide[indice] = elemento.split()
        
        return l_decide
    
    def construir(self):
        arq = self.arquivo()
        for i in arq:
            num = i.count('|')
                
            if self.antes == None:
                self.antes = num
                pai = None
            elif self.antes == num:
                pai = pai.getpai()
                
            elif self.antes > num:
                volta = antes - num
                while volta > 0:
                    pai = pai.getpai().getpai()
                    volta-=1
            
            if self.raiz == None:
                no = Noh(i[num:])
                self.raiz = no
                pai = no
            else:
                if '<' in i:
                    if ':' in i:
                        a = i.index(':')
                        folha = Noh(i[a+1:])
                        no = Noh(i[num:a])
                        no.setFiesquerdo(folha)
                        folha.setpai(no)
                        no.setpai(pai)
                        pai.setFiesquerdo(no)
                        pai = no
                    else:
                        no = Noh(i[num:])
                        no.setpai(pai)
                        pai.setFiesquerdo(no)
                        pai = no
                        
                elif '>=' in i:
                    if ':' in i:
                        a = i.index(':')
                        folha = Noh(i[a+1:])
                        no = Noh(i[num:a])
                        no.setFidireito(folha)
                        folha.setpai(no)
                        no.setpai(pai)
                        pai.setFidireito(no)
                        pai = no
                        
                    else:
                        no = Noh(i[num:])
                        no.setpai(pai)
                        pai.setFidireito(no)
                        pai = no

a = arvore()
a.construir()