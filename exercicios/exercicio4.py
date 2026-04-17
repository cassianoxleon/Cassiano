cadastros = []

while True:
    print(cadastros)

    n = input("Digite o seu nome: ")
    i = int(input("Digite sua idade: "))

    dados = {
        "Nome": n,
        "Idade": i
    }

    if dados in cadastros:
        print("Essa pessoa já tá cadastrada.")
    else:
        cadastros.append(dados)
        print(dados)
    
    print(cadastros)

    pergunta = input("Quer continuar a cadastrar? ").upper()

    if not pergunta == "SIM":
        break