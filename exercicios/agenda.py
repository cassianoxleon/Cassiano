data_eventos = {
    "lalal": [1, 2, 3]
}
eventos = []
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

def verif_data(numDia: int, numMes: int, numAno: int) -> bool:
    if numDia >= 31:
        print("\n ⚠️ Dia inválido!")
        return True
    if numMes >= 12:
        print("\n ⚠️ Mês inválido!")
        return True
    if numAno <= 2025:
        print("\n ⚠️ Esse ano já passou!")
        return True
    return False

print("\n//------------------ 📅 Agenda 1.0 ------------------//")

while True:
    try:
        print("--------------------------------")
        dia = int(input("Digite o Dia do evento: "))
        mes = int(input("Digite o Mês do evento: "))
        ano = int(input("Digite o Ano do evento: "))
        print("--------------------------------")
    except TypeError as error:
        print(f"\n ⚠️ Erro no tipo! ({error})")
    except TypeError as error:
        print(f"\n ⚠️ Erro no valor! ({error})")

    if verif_data(dia, mes, ano):
        continue

    titulo = input("Escreva o Título que você quer dar a esse evento: ")

    nome_mes = ""
    if mes in meses:
        nome_mes = meses[mes]
    
    print(f"\nTítulo: {titulo}. Data: {dia} de {nome_mes}, {ano}\n")
    pergun = input("O Título e a Data está correta? (''SIM'' = sim; ''NÃO'' = não) ").upper()
    if pergun != "SIM" and pergun != "NÃO":
        print("\n ⚠️ Resposta inválida!\nRecomeçando...")
        continue
    if pergun == "SIM":
        data_eventos[titulo] = [dia, mes, ano]
        eventos.append(titulo)
        print("Evento adicionado com sucesso!")
    else:
        print("Recomeçando...")
        continue

        continuar = input("Continuar a adicionar eventos? (''SIM'' = sim; ''NÃO'' = não) ").upper()
    if pergun != "SIM" and pergun != "NÃO":
        print("\n ⚠️ Resposta inválida!\nTerminando...")
        break
    if pergun == "SIM":
        continue
    else:
        break
        
