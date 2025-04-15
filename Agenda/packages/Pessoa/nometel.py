class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def dados(self):
        print(f"Nome: {self.nome}\nTelefone: {self.telefone}")
        