Em Python, uma **função** é um bloco de código reutilizável que executa uma tarefa específica. Ela serve para organizar melhor o programa, evitar repetição de código e facilitar a manutenção.

As funções em Python são definidas usando a palavra-chave `def` (abreviação de *define*). A estrutura básica de uma função é:

```python
def nome_da_funcao(parametros):
    # bloco de código
    return resultado
```

**Explicando cada parte:**

* `def`: indica que você está criando uma função.
* `nome_da_funcao`: é o nome que você escolhe para a função.
* `parametros`: são valores que a função pode receber (opcional).
* `return`: retorna um valor como resultado da função (opcional).

**Exemplo simples:**

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

Nesse exemplo:

* Criamos uma função chamada `saudacao`.
* Ela recebe um parâmetro chamado `nome`.
* Retorna uma mensagem personalizada.

Para usar a função, basta chamá-la:

```python
print(saudacao("Maria"))
```

**Saída:**

```
Olá, Maria!
```

**Por que usar funções?**

* Reutilização de código
* Melhor organização
* Facilidade de leitura
* Manutenção mais simples

Resumindo: funções são fundamentais em Python (e na programação em geral), pois ajudam a dividir o programa em partes menores e mais gerenciáveis.
