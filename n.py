global lista_pessoas
lista_pessoas = []
menores_idade = []

pessoas = 0
# 0 = Parar; 1 = Continuar sem registrar; 2 = Continuar normal.
def continuar(numYes: int, numNo: int, pessoaRegis: str) -> int:
    q = int(input(f"Quer continuar a registrar pessoas? ({numNo} = Não; {numYes} = Sim) "))
    if q == numNo:
        return 0
    elif q >= 1 and pessoaRegis == "registrada":
        return 2
    return 1

def verif_nome(name: str) -> bool:
    if name in lista_pessoas:
        return True
    return False
# 0 = Parar; 1 = Continuar sem registrar; 2 = Continuar normal.
def verificacao(name: str, idade: int) -> int:
    if name in menores_idade and idade >= 18:
        print(f"Não tente falsificar sua idade, jegue. ({name})")

        qs0 = continuar(1, 0, "nao registrada")
        if qs0 == 0:
            return 0
        elif qs0 == 1:
            return 1
        return 2

    if idade >= 18:
        print(f"Pessoa registrada. ({name})")
        lista_pessoas.append(name)

        qs1 = continuar(1, 0, "registrada")
        if qs1 == 0:
            return 0
        elif qs1 == 1:
            return 1
        return 2
    else:
        print(f"Essa pessoa (bebê) deve ter mais de 18 anos para entrar. ({name})")
        menores_idade.append(name)

        qs2 = continuar(1, 0, "nao registrada")
        if qs2 == 0:
            return 0
        elif qs2 == 1:
            return 1
        return 2

print("Confirme seu nome e sua idade para entrar na balada.")
print("Você pode registrar até 5 pessoas.")

while pessoas != 5:
    nome = input("Digite seu nome: ")

    verificar_nome = verif_nome(nome)
    if verificar_nome:
        print("Essa pessoa já está registrada.")
        continue

    idade = int(input("Digite sua idade: "))
    verifpessoa = verificacao(nome, idade)
    if verifpessoa == 0:
        break
    elif verifpessoa == 1:
        continue
    else:
        pessoas += 1
        continue

print(f"{len(lista_pessoas)} pessoas foram registradas.")
print(f"Pessoas registradas: {lista_pessoas}")