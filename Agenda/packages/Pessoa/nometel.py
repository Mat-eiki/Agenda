class Pessoa:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dados(self):
        print(f"Nome: {self.a}\nTelefone: {self.b}")