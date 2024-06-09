def atualizar_contato(contatos):
    if not contatos:
        print("Nenhum contato adicionado.")
        return

    nome = input("Digite o nome do contato que deseja atualizar: ")
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Atualizando contato '{contato['nome']}'")
            new_tel = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
            new_email = input("Digite o novo email (ou pressione Enter para manter o atual): ")

            if new_tel:
                contato['tel'] = new_tel
            if new_email:
                contato['email'] = new_email

            print(f"Contato '{contato['nome']}' atualizado com sucesso!")

            return

    print(f"Contato '{nome}' não encontrado.")
