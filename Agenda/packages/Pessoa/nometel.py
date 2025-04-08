class Pessoa:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dados(self):
        print(f"Nome: {self.a}\nTelefone: {self.b}")
        
    def to_dict(self):
        return {"a": self.a, "b": self.b}

    @classmethod
    def from_dict(cls, data):
        return cls(data["a"], data["b"])