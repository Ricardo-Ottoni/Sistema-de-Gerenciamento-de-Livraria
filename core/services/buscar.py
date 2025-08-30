from core import livros

# 5° Função p/ buscar um livro cadastrado pelo título, autor ou palavra qualquer
def buscarLivro():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('\n-----------------------------------------------------')
    print('                --- Buscar Livro ---                 ')
    print('Escolha uma opção de busca:')
    print(':   1 -> Por Título                                 :')
    print(':   2 -> Por Autor                                  :')
    print(':   3 -> Por Palavra                                :')
    print(':   4 -> Sair da Busca                              :')

    opcao = input('\nDigite o valor escolhido: ')
    
    if opcao == '1':
        porTitulo = input('Informe o título: ').upper()
        i = 0
        encontrado = False      # uso de flag (variável booleana) p/ controlar o fluxo de execução    
        while i < len(livros):
            livro = livros[i]
            if porTitulo == livro['titulo']:
                print(f'>>> Livro(s) encontrado(s) com sucesso!\n')
                print(f'Título: {livro['titulo']}')
                print(f'-- Autor: {livro['autor']}')
                print(f'-- Gênero: {livro['genero']}')
                print(f'-- Preço: R$ {livro['preco']:.2f}')
                encontrado = True
            i += 1
        if not encontrado:
            print('>>> Livro não encontrado.')
            

    elif opcao == '2':
        porAutor = input('Informe o autor: ').upper()
        i = 0
        encontrado = False
        while i < len(livros):
            livro = livros[i]
            if porAutor in livro['autor'].upper():
                print(f'>>> Livro(s) encontrado(s) com sucesso!\n')
                print(f'Título: {livro['titulo']}')
                print(f'-- Autor: {livro['autor']}')
                print(f'-- Gênero: {livro['genero']}')
                print(f'-- Preço: R$ {livro['preco']:.2f}')
                encontrado = True
            i += 1
        if not encontrado:
            print('>>> Livro não encontrado.')

    elif opcao == '3':
        porPalavra = input('Informe uma palavra: ').upper()
        i = 0
        encontrado = False
        while i < len(livros):
            livro = livros[i]
            if (porPalavra in livro['titulo'].upper()) or (porPalavra in livro['autor'].upper()):
                print(f'>>> Livro(s) encontrado(s) com sucesso!\n')
                print(f'Título: {livro['titulo']}')
                print(f'-- Autor: {livro['autor']}')
                print(f'-- Gênero: {livro['genero']}')
                print(f'-- Preço: R$ {livro['preco']:.2f}')
                encontrado = True
            i += 1
        if not encontrado:
            print('>>> Livro não encontrado.')

    elif opcao == '4':
        print('\n>>> Você saiu do buscador.')
        return
    else:
        print('\n>>> Opção inválida!! Tente novamente.')
    print('-----------------------------------------------------')
