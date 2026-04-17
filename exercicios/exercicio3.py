completa = "EU SOU UM JEGUE"
incompleta = "EU SOU UM __GUE"
faltando = "JE"

s_usadas = []

print(incompleta)

while True:
    p = input("Que sílaba está faltando?").upper()

    if p == faltando:
        print("Acertou.")
        break
    elif p in s_usadas:
        print(f"Já foi usada, jegue. ({p})")
    else:
        print("Não, burro.")
        s_usadas.append(p)
        print(s_usadas)