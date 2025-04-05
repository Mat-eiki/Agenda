from packages import Agenda,Pessoa

def workspace():
    entrada = input("Por favor, insira seu nome e telefone, respectivamente, separados por vírgula: ")
    nome, telefone = entrada.split(",")
    nome.nome()
    telefone.telefone()
    agenda=Agenda()
    agenda.loop(100)
    
if __name__=="__main__":
    workspace()
    