palavra_compl = "MANTEIGA"
letras_correta = {
    i: letra for i, letra in enumerate(palavra_compl)
}
letras_vazias = {
    i: "_" for i, letra in enumerate(palavra_compl)
}
letras_usadas = []

letras_restan = 0

quanti_membros = 6
membros_adic = 0
membros = {
    "Part1": "",
    "Part2": "",
    "Part3": ""
}

def mostrar_membros(t1: str, t2: str, t3: str):
    if not t1 == "":
        print(t1)
    if not t2 == "":
        print(t2)
    if not t3 == "":
        print(t3)

def adicionar_membros(adicionado: int) -> int:
    if adicionado < 6:
        if adicionado == 0:
            membros["Part1"] = " O"
            adicionado += 1
            return adicionado
        elif adicionado == 1:
            membros["Part1"] = " O"
            membros["Part2"] = "(_)"
            adicionado += 1
            return adicionado
        elif adicionado == 2:
            membros["Part1"] = "  O"
            membros["Part2"] = "<(_)"
            adicionado += 1
            return adicionado
        elif adicionado == 3:
            membros["Part1"] = "  O"
            membros["Part2"] = "<(_)>"
            adicionado += 1
            return adicionado
        elif adicionado == 4:
            membros["Part1"] = "  O"
            membros["Part2"] = "<(_)>"
            membros["Part3"] = " |"
            adicionado += 1
            return adicionado
        elif adicionado == 5:
            membros["Part1"] = "  O"
            membros["Part2"] = "<(_)>"
            membros["Part3"] = " | |"
            adicionado += 1
            return adicionado
    return adicionado
        
def verificar_letra(letr: str) -> str:
    if letr in letras_usadas:
        print("\nEssa letra já foi usada KKKKKK")
        return "usado"
    
    for i, letra in enumerate(palavra_compl):
        if letras_correta[i] == letr:
            print("\nAcertou uma das palavras!")
                
            return "acertou"
    print(f"\nERROUKKKKKKK ({letr})")
        
    return "errou"

def verificar_jogo(members: int) -> bool:
    if members == 6:
        return True
    return False
        
print("\n--- Jogo Da Forca! ---")
print("Adivinhe qual é a palavra e ganhe nada.")
print("DICA: Na maioria das vezes, é adicionado em um pão.")

while letras_restan != len(palavra_compl):
    verificacao = verificar_jogo(membros_adic)
    if verificacao == True:
        mostrar_membros(membros["Part1"], membros["Part2"],  membros["Part3"])
        print("Desculpa, mas você perdeu!")
        print(f"A palavra era: {palavra_compl}")
        break
    
    mostrar_membros(membros["Part1"], membros["Part2"],  membros["Part3"])

    print(*letras_vazias.values())
        
    letra_inserida = str(input("Digite uma letra: ")).upper()
    
    le = verificar_letra(letra_inserida)
    if le == "acertou":
        letras_usadas.append(letra_inserida)
        
        for i, letra in enumerate(palavra_compl):
            if letras_correta[i] == letra_inserida:
                letras_vazias[i] = letra_inserida
                letras_restan += 1
        
        continue
    elif le == "usado":
        continue
    elif le == "errou":
        letras_usadas.append(letra_inserida)
        quanti = adicionar_membros(membros_adic)
        membros_adic = quanti
        print(membros_adic)
        continue
    
if not membros_adic == 6:
    print("VOCÊ VENCEU!!!")
    print(f"A palavra era: {palavra_compl}\n")
    