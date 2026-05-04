
def somar(*args):
    return sum(args)

def subtrair(*args):
    vlr = 0
    for i in args:
        vlr -= i
    return vlr

def multipli(*args):
    vlr = 0
    for i in args:
        vlr * i
    return vlr

def dividir(*args):
    vlr = 0
    for i in args:
        vlr / i
    return vlr

print("\n-- Calculadora V1 --\n")

while True:
    the_nums = []
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        the_nums.append(num1)
        the_nums.append(num2)
        while True:
            continuar = int(input("Adicionar mais números? (0 = Não; 1 = Sim.) "))
            if continuar <= 0:
                break

            num = float(input("\nDigite outro número: "))
            the_nums.append(num)

        perg = input("------------------------\nQue tipo de operação fazer com esses número?\n(somar = +; subtrair = -; multiplicar = *; dividir = /): ")
    except ValueError:
        print("⚠️ ERRO! (Por favor, digite um número.)\n")
        continue

    result = 0

    if perg == "+":
        result = somar(*the_nums)
    elif perg == "-":
        result = subtrair(*the_nums)
    elif perg == "*":
        result = multipli(*the_nums)
    elif perg == "/":
        result = dividir(*the_nums)
    else:
        print("⚠️ ERRO! (Por favor, digite o que pretende fazer com eles.)\n")
        continue

    print(result)
    try:
        cont_calcular = int(input("Continuar a usar a calculadora? (0 = Não; 1 = Sim)"))
        if cont_calcular <= 0:
            break
    except ValueError:
        print("⚠️ ERRO! (Por favor, digite um número.)\n")