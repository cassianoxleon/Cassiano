class Conta:
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def __str__(self):
        return self

pergun = input("Você é retardado? ").upper()
if pergun == "SIM":
    print("Claro.")
else:
    print("Você é sim.")