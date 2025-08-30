from core.services.cadastrar import cadastrarLivro
from core.services.exibir import exibirLivros
from core.services.buscar import buscarLivro
from core.services.editar import editarLivro
from core.services.excluir import excluirLivro

from core.database.salvar import salvarDados
from core.database.carregar import carregarDados

# 1° Criação do menu principal
print('-----------------------------------------------------')
print('\n  BEM-VINDO AO SISTEMA DE GERENCIAMENTO DE LIVRARIA  \n')
print('-----------------------------------------------------')
print('Verifique o menu abaixo e selecione a opção desejada.')
print('-----------------------------------------------------\n')

# Função principal (menu)
def menuPrincipal():
    while True:
        print('\n-----------------------------------------------------')
        print('                  ----- MENU -----                   ')
        print('-----------------------------------------------------')
        print(':   1 -> Cadastrar Livro no Sistema                 :')
        print(':   2 -> Exibir Livros Cadastrados                  :')
        print(':   3 -> Buscar um Livro Específico                 :')
        print(':   4 -> Editar Dados de um Livro                   :')
        print(':   5 -> Excluir Livro do Sistema                   :')
        print(':   6 -> Salvar Dados no Sistema                    :')
        print(':   7 -> Carregar Dados Salvos                      :')
        print(':   8 -> Sair do Sistema                            :')
        print('-----------------------------------------------------\n')
        
        opcao = input('Digite o valor escolhido: ')
        
        if opcao == '1':
            cadastrarLivro()
        elif opcao == '2':
            exibirLivros()
        elif opcao == '3':
            buscarLivro()
        elif opcao == '4':
            editarLivro()
        elif opcao == '5':
            excluirLivro()
        elif opcao == '6':
            salvarDados()
        elif opcao == '7':
            carregarDados()
        elif opcao == '8':
            print('\n>>> SISTEMA FINALIZADO <<<')
            print('-----------------------------------------------------')
            break
        else:
            print('\n>>> Opção inválida!! Tente novamente.')

# 11° Chamar a função p/ carregar dados logo qdo o programa inicia.
carregarDados()

menuPrincipal()