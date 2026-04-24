## 🎯 1. Objetivo do jogo

* O jogador precisa adivinhar uma palavra secreta
* Ele pode tentar letras
* Tem um número limitado de erros antes de perder

---

## 🧠 2. Escolher a palavra secreta

* Pode ser uma palavra fixa (ex: “python”)
* Ou uma lista de palavras para escolher aleatoriamente

---

## 🔤 3. Criar a estrutura da palavra escondida

* Mostrar a palavra com traços ou underscores

  * Ex: `_ _ _ _ _ _`
* Cada traço representa uma letra não descoberta

---

## 🔁 4. Criar o sistema de tentativas

* Definir quantas chances o jogador tem (ex: 6 erros)
* Criar um contador de erros

---

## ⌨️ 5. Pedir uma letra ao jogador

* O jogador digita uma letra por vez
* Validar:

  * Se digitou apenas 1 letra
  * Se não repetiu uma letra já usada

---

## ✅ 6. Verificar se a letra está na palavra

* Se estiver:

  * Revelar a letra nas posições corretas
* Se não estiver:

  * Aumentar o número de erros

---

## 📊 7. Mostrar o progresso

* Exibir:

  * Palavra atual (com letras descobertas)
  * Letras já usadas
  * Quantos erros ainda restam

---

## 🏁 8. Criar condição de vitória

* O jogador vence quando descobre todas as letras

---

## 💀 9. Criar condição de derrota

* O jogador perde quando atinge o limite de erros

---

## 🔄 10. Encerrar ou reiniciar

* Mostrar mensagem final:

  * “Você ganhou!” ou “Você perdeu!”
* Perguntar se quer jogar novamente

