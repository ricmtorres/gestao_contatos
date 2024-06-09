def excluir_contato(contatos):
    if not contatos:
        print("Nenhum contato adicionado.")
        return

    try:
        indice = int(input("Digite o número do contato que você deseja excluir: ")) - 1
        if 0 <= indice < len(contatos):
            contato_excluir = contatos.pop(indice)
            print(f"Contato '{contato_excluir['nome']}' excluído com sucesso !")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
