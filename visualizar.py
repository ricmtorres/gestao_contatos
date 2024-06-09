def visualizar_contato(contatos):
    if not contatos:
        print("Nenhum contato adicionado.")
        return

    for idx, contato in enumerate(contatos):
        print("\n Contato {}:".format(idx + 1))
        print(f"Nome: {contato['nome']}, Telefone: {contato['tel']}, Email: {contato['email']}")


