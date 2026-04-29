cadastrados = []

def verificar_usuario(usua: tuple, lista: list) -> bool:
    if usua in lista:
        print("Já está cadastrado! (Tente novamente.)\n")
        return True
    
    lista.append(usua)
    print("Cadastrado com sucesso!\n")
    return False

def continuar(numero: str) -> int | None:
    try:
        numero = int(numero)
        return numero
    except ValueError:
        print("\n ⚠️ ERRO! Por favor, digite números.")

def mostrar_cadas(lista_cadas: list) -> bool:
    quanti_cadas = len(cadastrados)
    if quanti_cadas != 0:
        print("\n-------------------------------")
        print("Usuários Cadastradas:")
        for nome, senha in lista_cadas:
            print(f"Usuário: {nome}\nSenha: {senha}\n")
        print("-------------------------------\n")
    return False

print("\n----------------------------")

while True:
    mostrar_cadas(cadastrados)
    nome_usua = input("Digite seu nome de usuário: ")

    try:
        senha = int(input("Digite sua senha (Deve possuir só números): "))
    except ValueError:
        print("\n ⚠️ ERRO! A senha deve possuir apenas números. (Tente novamente.)")
        continue

    usua_e_senha = (nome_usua, senha)

    verif_usua = verificar_usuario(usua_e_senha, cadastrados)
    if verif_usua:
        continue

    pergunta = "Quer continuar a cadastrar? (1 = Sim; 0 = Não) "
    if continuar(input(pergunta)) == 1:
        continue
    break

mostrar_cadas(cadastrados)