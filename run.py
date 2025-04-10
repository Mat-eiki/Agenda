import Metodos.Add as func
import Metodos.Rmv as func

contatos= {}
print("Agenda de contatos em python \n Para começar digite um comando: \n Add [nome] [número] \n Rmv [nome] ou [número] \n Edit [nome] [novo nome] ou [número] [novo número] \n List (lista de contatos salvos)")

comando = ""
while comando != "stop":
    comando = input()
    comando, nome, numero = comando.split()
    if comando == "Add":
        func.Adicionar(contatos, nome, numero) 
    elif comando == "Rmv":
        func.Remover(contatos, nome, numero)