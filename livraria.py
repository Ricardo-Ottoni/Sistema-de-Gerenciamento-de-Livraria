# 2° Criação de uma lista vazia
livros = []

# 3° Função p/ cadastrar livros por título, autor, gênero e preço
def cadastrarLivro():
    print('\n-----------------------------------------------------')
    print('               --- Cadastrar Livro ---               ')
    while True:
        titulo = input('Título: ').upper() 
        if any(livro['titulo'].upper() == titulo for livro in livros): 
            print(f'\nLivro: "{titulo}" já é cadastrado no sistema!')
            return
        else:
            break
        
    autor = input('Autor: ')
    genero = input('Gênero: ')

    while True:
        preco = float(input('Preço: R$ '))
        if preco <= 0:
            print('Preço inválido!')
        else:
            break
    
    # Adicionando livros a lista
    livros.append({
        'titulo':titulo,
        'autor': autor,
        'genero': genero,
        'preco': preco
    })

    print(f'\nLivro: "{titulo}" cadastrado com sucesso!')    
    print('-----------------------------------------------------')

# 1° Criação do menu principal
print('-----------------------------------------------------')
print('\n  BEM-VINDO AO SISTEMA DE GERENCIAMENTO DE LIVRARIA  \n')
print('-----------------------------------------------------')
print('Verifique o menu abaixo e selecione a opção desejada.')
print('-----------------------------------------------------\n')

# função principal (menu)
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
        # elif opcao == '2':
        #     exibirLivros()
        # elif opcao == '3':
        #     buscaLivro()
        # elif opcao == '4':
        #     editarLivro()
        # elif opcao == '5':
        #     excluirLivro()
        # elif opcao == '6':
        #     dalvarDados()
        #     print('Dados salvos com sucesso!')
        # elif opcao == '7':
        #     carregarDados()
        # elif opcao == '8':
        #     print('Finalizando sistema...')
        #     break
        else:
            print('Opção inválida!! Tente novamente.')

menuPrincipal()