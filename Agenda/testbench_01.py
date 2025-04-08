from packages.Pessoa.nometel import Pessoa
from packages.Agenda.metodos import Agenda

def workspace():
    entrada = input("Por favor, insira o primeiro nome e telefone, respectivamente, separados por vírgula: ")
    nome, telefone = entrada.split(" ")
    confirmar=Pessoa(nome,telefone)
    confirmar.dados()
if __name__=="__main__":
    workspace()
    