from packages.Pessoa.nometel import Pessoa
import json
class Agenda():
    
    def __init__(self):
        self.contatos= self.carregar_de_json()
        
    def adicionar(self, nome, telefone):
        nova_pessoa = Pessoa(nome, telefone)
        self.contatos.append(nova_pessoa)
        nova_pessoa.dados() 
        self.salvar_em_json()
        print("Contato adicionado com sucesso!\n")
        
    def salvar_em_json(self, arquivo="contatos.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.contatos], f, ensure_ascii=False, indent=4)

    def carregar_de_json(self, arquivo="contatos.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Pessoa.from_dict(d) for d in dados]
        except FileNotFoundError:
            return []
        
    def loop(self):
        while True:
            print("------Menu da Agenda------")
            print("1- Adicionar contato\n2- Visualizar contato\n3- Editar contato\n4- Excluir contato\n")
            opcao=input("Escolha uma opção\n")
            if opcao == "1":
                entrada = input("Digite o nome e telefone separados por espaço: ")
                nome, telefone = entrada.split(" ")
                self.adicionar(nome, telefone)