# Revisão de Assunto - LPPI

## 1) Tipos de dados em Python

### `str` (texto)
- Representa palavras, frases e caracteres.
- Exemplo: `nome = "Ana"`

### `int` (número inteiro)
- Representa números sem casa decimal.
- Exemplo: `idade = 18`

### `float` (número decimal)
- Representa números com casa decimal.
- Exemplo: `altura = 1.70`

### `bool` (verdadeiro ou falso)
- Só possui dois valores: `True` e `False`.
- Exemplo: `maior_de_idade = True`

### `list` (lista)
- Coleção mutável (pode mudar) e ordenada.
- Exemplo: `notas = [7.5, 8.0, 9.2]`

### `tuple` (tupla)
- Coleção imutável (não muda depois de criada) e ordenada.
- Exemplo: `coordenada = (10, 20)`

### `dict` (dicionário)
- Armazena dados em pares `chave: valor`.
- Exemplo: `usuario = {"nome": "Carlos", "idade": 20}`

## 2) Funções e estruturas usadas nas aulas

### `input()`
- Lê dados digitados pelo usuário.
- Sempre retorna texto (`str`).

### `print()`
- Exibe informações na tela.

### `type()`
- Mostra o tipo de uma variável.

### `if`, `elif`, `else`
- Estruturas de decisão para validar condições.

### `while`
- Estrutura de repetição que executa enquanto a condição for verdadeira.

## 3) Conversão de tipos

Como o `input()` retorna `str`, muitas vezes é preciso converter:

- `int(valor)` para inteiro
- `float(valor)` para decimal
- `str(valor)` para texto
- `bool(valor)` para booleano

Exemplo:

```python
valor = input("Digite um numero: ")
inteiro = int(valor)
decimal = float(valor)

print("Valor inteiro:", inteiro)
print("Valor decimal:", decimal)
print("Tipo de inteiro:", type(inteiro))
print("Tipo de decimal:", type(decimal))
```