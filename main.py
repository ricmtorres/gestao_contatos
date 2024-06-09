from menu import menu
from adicionar import adicionar_contato
from visualizar import visualizar_contato
from atualizar import atualizar_contato
from remover import excluir_contato


def main():
    contatos = []
    while True:
        opcao = menu()

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            visualizar_contato(contatos)
        elif opcao == '3':
            atualizar_contato(contatos)
        elif opcao == '4':
            excluir_contato(contatos)
        elif opcao == '5':
            print("Saindo....")
            break
        else:
            print("Opção inválida ! Tente novamente.")

if __name__ == '__main__':
    main()
