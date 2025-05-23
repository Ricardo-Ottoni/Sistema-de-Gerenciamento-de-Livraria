# Criação do menu principal
print('-----------------------------------------------------')
print('\n  BEM-VINDO AO SISTEMA DE GERENCIAMENTO DE LIVRARIA  \n')
print('-----------------------------------------------------')
print('Verifique o menu abaixo e selecione a opção desejada.')
print('-----------------------------------------------------\n')


def menuPrincipal():
    while True:
        print('\n-----------------------------------------------------')
        print('                    --- MENU ---                     ')
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
        
        # if opcao == '1':
        #     CadastrarLivro()
        # elif opcao == '2':
        #     ExibirLivros()
        # elif opcao == '3':
        #     BuscaLivro()
        # elif opcao == '4':
        #     EditarLivro()
        # elif opcao == '5':
        #     ExcluirLivro()
        # elif opcao == '6':
        #     SalvarDados()
        #     print('Dados salvos com sucesso!')
        # elif opcao == '7':
        #     CarregarDados()
        # elif opcao == '8':
        #     print('Finalizando sistema...')
        #     break
        # else:
        #     print('Opção inválida!! Tente novamente.')

menuPrincipal()