from packages.Pessoa.nometel import Pessoa
from packages.Agenda.metodos import Agenda

def workspace():
    agenda=Agenda()
    agenda.loop()
if __name__=="__main__":
    workspace()
    