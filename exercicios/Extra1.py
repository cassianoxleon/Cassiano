dados = {
    "User": "",
    "Email": "",
    "Senha": ""
}

contas = []

p1 = input("Digite seu nome de usuário: ")
print(p1)

dados["User"] = p1

p2 = input("Crie uma senha: ")
print(p2)

dados["Senha"] = p2

p3 = input("Agora digite seu email: ")
print(p3)

tries = 0
while 0 < 3:
    verif = int(input("Enviamos um código para seu email, informe seu código: "))
    codigo = 123456

    if verif == codigo:
        print("Conta criada com sucesso.")
        contas.append(dados["User"])
        break
    else:
        tries += 1
        print(f"Código inválido, tente novamente ({tries})")

    if tries == 3:
        print("Você chegou no limite de tentativas.")
        print("Bloqueando sua conta...")
        break
    