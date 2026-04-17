usuario = "Alguém1234"

a = input("Digite seu nome de usuário: ")
print(a)

if a == usuario:
    print("Verifique se é você mesmo usando o FaceID")
else:
    print(f"cai fora, {a}.")
    n = 1
    while n < 4:
        print(f"Bloqueando sua conta... ({n})")
        n += 1
        if n == 4:
            print("Bloqueado com sucesso.")