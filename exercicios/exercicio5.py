
print("Confirme seu nome e sua idade para entrar na balada.")
print("Você pode registrar até 5 pessoas.")

pessoas = 0
lista_pessoas = []

while pessoas != 5:
    
    Nome = input("Digite seu nome: ")
    Idade = int(input("Digite sua idade: "))

    if Idade >= 18:
        print(f"Pessoa registrada. ({Nome})")
        lista_pessoas.append(Nome)

        pessoas += 1

        q1 = int(input("Quer continuar a registrar pessoas? (0 = Não; 1 = Sim) "))

        if q1 == 1:
            continue
        elif q1 == 0:
            break
        else:
            continue
    else:
        print(f"Essa pessoa (bebê) deve ter mais de 18 anos para entrar. ({Nome})")
        q2 = int(input("Quer continuar a registrar pessoas? (0 = Não; 1 = Sim) "))

        if q2 == 1:
            continue
        elif q2 == 0:
            break
        else:
            continue

print("Já tem 5 pessoas registradas.")
print(f"Pessoas registradas: {lista_pessoas}")