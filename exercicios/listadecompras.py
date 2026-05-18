lista_compras = []

def verif_lista() -> bool:
    if len(lista_compras) == 0:
        print("\n ⚠️ Não tem nenhum item para remover!\n")
        return True
    return False

def remover_item(nome: str) -> str:
    if nome in lista_compras:
        lista_compras.remove(nome)
        return "\n Item removido com sucesso!\n"
    else:
        return "\n ⚠️ Item não encontrado.\n"
    
def adicionar_item(nome: str) -> str:
    lista_compras.append(nome)
    return "\n Item adicionado com sucesso!\n"
    
print("\n//------------------ 🛒 Shopee..? ------------------//")

while True:
    pergun = input("O que pretende fazer?\n(''ADD'' = adicionar; ''REMOVE'' = remover; ''END'' = terminar.) ").upper()
    if pergun == "REMOVE":
        verif = verif_lista()
        if verif:
            continue
        else:
            rmv_item = input("Qual item remover? ")
            print(remover_item(rmv_item))
        
    elif pergun == "ADD":
        add_item = input("Que item você quer adicionar? ")
        print(adicionar_item(add_item))
    elif pergun == "END":
        break
    else:
        print("\n ⚠️ Por favor, escolha o que você pretende fazer.\n")

    if len(lista_compras) == 0:
        print("👜 Lista de Compras: Não adicionou nenhum item.\n")
    else:
        print("👜 Lista de Compras: ", lista_compras, "\n")

if len(lista_compras) == 0:
    print("👜 Lista de Compras: Não adicionou nenhum item.\n")
else:
    print("👜 Lista de Compras: ", lista_compras, "\n")
print("Removendo todos os itens da sua Lista de Compras.")
print("Removendo todos os itens da sua Lista de Compras..")
print("Removendo todos os itens da sua Lista de Compras...")

print("\n 🎉 Parabéns, você acabou de desperdiçar seu tempo.")