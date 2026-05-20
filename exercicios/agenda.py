data_eventos = {}
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

def verif_data(numDia: int, numMes: int, numAno: int, numHora: int, numMin: int) -> bool:
    if numDia >= 32 or numDia <= 0:
        print("\n ⚠️ Dia inválido!")
        return True
    if numMes >= 13 or numMes <= 0:
        print("\n ⚠️ Mês inválido!")
        return True
    if numAno <= 2025:
        print("\n ⚠️ Esse ano já passou!")
        return True
    if numHora >= 24 or numHora <= -1:
        print("\n ⚠️ Hora inválida!")
        return True
    if numMin >= 60 or numMin <= -1:
        print("\n ⚠️ Minutos inválida!")
        return True
    return False

def mostrar_eventos():
    print("--\n 🗓️  Eventos Agendados:")
    if len(eventos) == 0:
        print("Nada foi agendado ainda.")
    else:
        for evento in eventos:
            day, month, year = data_eventos[evento][0]
            hour, mins = data_eventos[evento][1]
            print(f"{evento} - Data: {day} de {month}, {year}. Horário: {hour}:{mins}")
        print("--")

print("\n//------------------ 📅 Agenda 1.0 ------------------// (19/05/2026)")
mostrar_eventos()

while True:
    try:
        print("--------------------------------")
        dia = int(input("Digite o Dia do evento: "))
        mes = int(input("Digite o Mês do evento: "))
        ano = int(input("Digite o Ano do evento: "))
        hora = int(input("Digite a hora do evento: "))
        minutos = int(input("Por fim, digite os minutos do evento: "))
        print("--------------------------------")
    except TypeError as error:
        print(f"\n ⚠️ Erro no tipo! ({error})")
        print("Recomeçando...")
        continue
    except ValueError as error:
        print(f"\n ⚠️ Erro no valor! ({error})")
        print("Recomeçando...")
        continue

    if verif_data(dia, mes, ano, hora, minutos):
        continue

    titulo = input("Escreva o Título que você quer dar a esse evento: ")

    nome_mes = ""
    if mes in meses:
        nome_mes = meses[mes]
    
    print(f"\nTítulo: {titulo} - Data: {dia} de {nome_mes}, {ano}. Horário: {hora}:{minutos}\n")
    
    pergun = input("O Título, a Data e o Horário estão corretos? (''SIM'' = Sim; ''NAO'' = Não) ").upper()
    if pergun != "SIM" and pergun != "NAO":
        print("\n ⚠️ Resposta inválida!\nRecomeçando...")
        continue
    if pergun == "SIM":
        data_eventos[titulo] = [(dia, mes, ano), (hora, minutos)]
        eventos.append(titulo)
        print("Evento agendado com sucesso!")
    else:
        print("Recomeçando...")
        continue
    
    mostrar_eventos()
    
    continuar = input("Quer continuar a agendar mais eventos? (''SIM'' = Sim; ''NAO'' = Não) ").upper()
        
    if continuar != "SIM" and continuar != "NAO":
        print("\n ⚠️ Resposta inválida!\nTerminando...")
        break
    if continuar == "SIM":
        continue
    else:
        break
print("---------------------------------------")
mostrar_eventos()
