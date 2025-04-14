import Metodos.Add as func
import Metodos.Rmv as func
import Metodos.edit as func
import Metodos.list as func

contatos= {}
print("Agenda de contatos em python \n Para começar digite um comando: \n add [nome] [número] \n rmv [nome] ou [número] \n edit [nome] [novo nome] ou [número] [novo número] \n list (lista de contatos) \n stop (finaliza o programa)")

comando = ""
while comando != "stop":
    comando = input()
    comando, nome, numero = comando.split()
    if comando == "add":
        func.Adicionar(contatos, nome, numero) 
    elif comando == "rmv":
        func.Remover(contatos, nome, numero)
    elif comando == "edit":
        func.editar()
    elif comando == "list":
        func.lista(contatos[nome])