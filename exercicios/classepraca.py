class Praca:
    def __init__(self, nome: str, bancos: bool, endereco, iluminacao: bool, lazer: list):
        self.nome = nome
        self.bancos = bancos
        self.endereco = endereco
        self.iluminacao = iluminacao
        self.lazer = lazer

    def __str__(self):
        return f"\n-------------\n{self.nome} - {self.endereco}\n-------------"
    
    def adicionar_lazer(self, elemento):
        self.lazer.append(elemento)
    
nova_praca = Praca(
    nome="Praça do Carai", 
    bancos=True,
    endereco="Perto da Casa do Carai",
    iluminacao=True,
    lazer=["Parquinho", "Academia", "Pistas de Caminhada", "Quadra de Futebol"]
)

nova_praca.adicionar_lazer("Quadra de Basquete")

print(nova_praca)
print(nova_praca.lazer)