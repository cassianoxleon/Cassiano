# string = teste
# int = números inteiros (1,2,3,4)
# float = números de ponto flutuante
# list = lista
# dict =  tipo de dicionário
# tupla
# sets = conjuntos
# datetime = data e hora
# bool = true ou false (boolean)
"""
type() - validar tipos, assim verificando se o tipo corresponde ao pedido do código
"""

# texto = 'sim'
# número = '67'
# print("está é a variável texto: ", texto)
# print("essa variável é do tipo: ", type(texto))

# print(type(type(texto) == type(número)))

ponto_flutuante = 6.7
inteiro = 6
complexo = 6 + 7j
# f-string = é um texto que recebe variáveis em chaves
# print(f"a soma de {inteiro} mais {ponto_flutuante} é: {inteiro + ponto_flutuante}")
# while True:
#     recebido = input("digite um numero: ")
#     try:
#         recebido = int(recebido)
#     except ValueError:
#         try:    
#             recebido = float(recebido)
#         except ValueError:
#             pass

#     print(bool(recebido))
# if type(recebido) == int:
#     print("esse número é inteiro.")
# else:
#     print("esse número não é inteiro")
dicionario = {
    "chave": 1, 
    "chave2": "sicoseveim"
}
lista = [1,2,3,4]

chave = dicionario["chave"]
chave2 = dicionario["chave2"]
# print(f"o valor da chave1 é {chave}")
# print(f"o valor da chave2 é {chave2}")
# print(dicionario.keys())
# print(dicionario.values())
print(dicionario)
dicionario["chave2"] = "Cassi"
print(dicionario)