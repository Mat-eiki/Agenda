from click import clear
from packages.Pessoa.nometel import Pessoa
import os

class Agenda():
    
    def __init__(self):
        self.contatos=[]
        
    def adicionar(self, nome, telefone):
        pessoa=Pessoa(nome,telefone)
        self.contatos.append(pessoa)
        
    def remover(self, termo):
        for pessoa in self.contatos:
            if pessoa.nome==termo:
                self.contatos.remove(pessoa)
                
    def editar(self,editar):
        for pessoa in self.contatos:
            if editar==pessoa.nome:
                novo_nome,novo_telefone=input("Insira o novo nome e telefone separados por espaço:").split(" ")
                pessoa.nome=novo_nome
                pessoa.telefone=novo_telefone
                return "Operacao concluida com sucesso."
        return "Pessoa não encontrada."
    
    def ver(self,ver):
        for pessoa in self.contatos:
            if ver==pessoa.nome:
                return f"{pessoa.nome}-{pessoa.telefone}"
        return "Pessoa não encontrada"
    
    def loop(self):
        while True:
            print("------Menu da Agenda------")
            print("1- Adicionar contato\n2- Visualizar contato\n3- Editar contato\n4- Excluir contato\n5- Sair\n")
            opcao=input("Escolha uma opção\n")
            if opcao == "1":
                entrada = input("Digite o nome e telefone separados por espaço: ")
                nome, telefone = entrada.split(" ")
                self.adicionar(nome, telefone)
            elif opcao=="2":
                ver=input("Insira o nome de quem queres visualizar\n")
                print(self.ver(ver))
            elif opcao=="3":
                editar=input("Insira qual contato tu queres editar:\n")
                print(self.editar(editar))
            elif opcao=="4":
                termo=input("Insira o nome ou o telefone de quem você quer excluir da agenda:\n")
                self.remover(termo)
            elif opcao=="5":
                print("Saindo...")
                break