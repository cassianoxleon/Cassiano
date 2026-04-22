## Variáveis
# Básicas - Elas pode receber valores de diferentes tipos e até receber funções
tipo_basica = None
n1 = 1

# Constantes - Elas recebem valores fixos que não devem ser 
# alterados no decorrer do código
CONSTATE = "Valor Fixo"
OUTRA_CONSTANTE = "Outro Valor"

## Tipos
# int - Numeros inteiros, ou seja, numeros sem ponto.
inteiro = 998989    # type(int)

# float - Numeros decimais ou numeros de ponto flutuante.
ponto_flutuante = 999.999   # type(float)

# str - Caracteriza texto, uma string. Sempre dentro de aspas simples ou duplas.
texto = "Isso é um str" # type(str)

# bool - Booleano, ou seja, verdadeiro ou falso. (True or False)
booleano = True or False

# list - Uma lista, deve ser aberta com colchetes "[ ]", os valores de uma lista
# podem ser alterados a qualquer momento
tupla_teste = (1, 2)

lista = []
lista_preenchida = [1, 2]
tupla_convertida = list(tupla_teste)

# tuple - Uma tupla, deve ser aberto com parenteses "( )", os valores não podem
# ser alterados
tupla = ()
tupla_preenchida = (1, 2)
tupla_reconvertida = tuple(tupla_convertida)

# dict - Dicionario, trabalha chave e valor, {"Chave": "Valor",}, Pode ser alterado
# a qualquer momento.
dicionario = {}
dicionario = {
    "Nome": "Matheus",
    "Idade": 26
} 


### Listas

lista_vazia = []
# print(lista_vazia)

## lista_vazia.append() - Isso permite que eu adicione algo a lista
pessoa_1 = "Matheus"
idade_pessoa_1 = 26
tupla_pessoa = ("Matheus", 1)
tupla_pessoa_2 = ("Richard", 2)
tupla_pessoa_3 = ("Richard", 3)
tupla_pessoa_4 = ("Richard", 4)
tupla_pessoa_5 = ("Richard", 5)
tupla_pessoa_6 = ("Richard", 6)
tupla_pessoa_7 = ("Richard", 7)


# lista_vazia.append(pessoa_1)
# lista_vazia.append(idade_pessoa_1)
lista_vazia.append(tupla_pessoa)
lista_vazia.append(tupla_pessoa_2)
lista_vazia.append(tupla_pessoa_3)
lista_vazia.append(tupla_pessoa_4)
lista_vazia.append(tupla_pessoa_5)
lista_vazia.append(tupla_pessoa_6)
lista_vazia.append(tupla_pessoa_7)

# print(lista_vazia)

# lista.remove() - Remove pela compatibilida, ou seja, se forem valores iguais.
# lista.pop() - Remove pelo indice, você fornece a posição e o codigo apaga
# lista_vazia.remove(tupla_pessoa)

# print(lista_vazia)

item = ("Richard", 5)
for posicao in lista_vazia:
    if posicao == item:
        indice = lista_vazia.index(posicao)
        # print(indice)
        lista_vazia.pop(indice)

lista_vazia.extend(lista_preenchida)

# print(lista_vazia)

# Dicionario

dicionario_vazio = {}

dicionario_vazio['Nome'] = "Richard"


print(dicionario_vazio["Nome"], dicionario_vazio.get("Nome", "Não possui nome"))

##############################

# range(9)
# print(range(5))

# while True:

lista = []
for i in range(3):
    dic = {}
    pessoa = input("Nome: ")
    idade = input("Idade: ")

    dic["Nome"] = pessoa
    dic["Idade"] = idade

    lista.append(dic)

    if pessoa == "Richard":
        break

venda = False

# while not venda:
#     preco = input("Preço: ")
#     quantidade = input("Quantidade: ")

#     if preco != "" and quantidade != "":
#         venda = True

# print(preco, quantidade)



print(lista)
