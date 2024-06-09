import re


def adicionar_contato(contatos):
    nome = input("Digite o nome do novo contato: ")

    while True:
        tel = input("Digite o telefone do novo contato: ")
        if tel.isdigit():
            break
        else:
            print("Telefone inválido. Por favor, digite apenas números.")

    while True:
        email = input("Digite o email do novo contato: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        else:
            print("Email inválido. Por favor, digite um email válido.")

    contato = {
        "nome": nome,
        "tel": tel,
        "email": email
    }

    contatos.append(contato)

    print(f"Contato '{nome}' adicionado com sucesso !")
