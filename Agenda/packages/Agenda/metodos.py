from packages.Pessoa.nometel import Pessoa

class Agenda():
    
    def __init__(self,prim,seg,ter,qua):
        self.prim=prim
        self.seg=seg
        self.ter=ter
        self.qua=qua
    def loop(self):
        for i in range(self.count):
            print(i)
