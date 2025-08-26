from database import *

# 3° Função p/ cadastrar livros por título, autor, gênero e preço
def cadastrarLivro():
    print('\n-----------------------------------------------------')
    print('               --- Cadastrar Livro ---               ')
    while True:
        titulo = input('Título: ').upper() 
        if any(livro['titulo'].upper() == titulo for livro in livros): 
            print(f'\n>>> Livro: "{titulo}" já está cadastrado no sistema!')
            return
        else:
            break
        
    autor = input('Autor: ')
    genero = input('Gênero: ')

    while True:
        preco = float(input('Preço: R$ '))
        if preco <= 0:
            print('>>> Preço inválido!')
        else:
            break
    
    # Adicionando livros a lista
    livros.append({
        'titulo':titulo,
        'autor': autor,
        'genero': genero,
        'preco': preco
    })

    print(f'\n>>> Livro: "{titulo}" cadastrado com sucesso!')    
    print('-----------------------------------------------------')

# 4° Função p/ exibir os livros cadastrados no sistema
def exibirLivros():
    print('\n-----------------------------------------------------')
    print('               --- Lista de Livros ---               ')
    
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    i = 0
    while i < len(livros):          
        livro = livros[i]
        print(f'Título: {livro['titulo']}')
        print(f'-- Autor: {livro['autor']}')
        print(f'-- Gênero: {livro['genero']}')
        print(f'-- Preço: R$ {livro['preco']:.2f}\n')
        i += 1

    print(f'>>> Total de livros cadastrados: {i}')
    print('-----------------------------------------------------')

# 5° Função p/ buscar um livro cadastrado pelo título ou autor
def buscarLivro():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('\n-----------------------------------------------------')
    print('                --- Buscar Livros ---                ')
    print('Escolha opção de busca:')
    print(':   1 -> Por Título                                 :')
    print(':   2 -> Por Autor                                  :')
    print(':   3 -> Sair da Busca                              :')

    opcao = input('\nDigite o valor escolhido: ')
    
    if opcao == '1':
        porTitulo = input('Informe o título: ').upper()
        i = 0
        encontrado = False      # uso de flag (variável booleana) p/ controlar o fluxo de execução    
        while i < len(livros):
            livro = livros[i]
            if porTitulo == livro['titulo']:
                print(f'>>> Livro encontrado com sucesso!\n')
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
                print(f'>>> Livro encontrado com sucesso!\n')
                print(f'Título: {livro['titulo']}')
                print(f'-- Autor: {livro['autor']}')
                print(f'-- Gênero: {livro['genero']}')
                print(f'-- Preço: R$ {livro['preco']:.2f}')
            i += 1
        if not encontrado:
            print('>>> Livro não encontrado.')

    elif opcao == '3':
        print('\n>>> Você saiu do buscador.')
        return
    else:
        print('\n>>> Opção inválida!! Tente novamente.')
    print('-----------------------------------------------------')

# 6° Função p/ editar livros cadastrados
def editarLivro():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('\n-----------------------------------------------------')
    print('                --- Editar Livros ---                ')
    
    livroEscolhido = input('Informe o título do livro que deseja editar:\n>  ').upper()
    # Testando 'for', mas tb pode ser por while
    for livro in livros:
        if livro['titulo'].upper() == livroEscolhido:
            print
            print(f'>>> Livro encontrado com sucesso!\n')
            print(f'Título: {livro['titulo']}')
            print(f'-- Autor: {livro['autor']}')
            print(f'-- Gênero: {livro['genero']}')
            print(f'-- Preço: R$ {livro['preco']:.2f}\n')
            
            print(f'Digite os novos dados do livro: ')
            novoTitulo = input('Novo título: ').upper()
            novoAutor = input('Novo autor: ')
            novoGenero = input('Novo gênero: ')

            while True:
                novoPreco = float(input('Novo preço: R$ '))
                if novoPreco <= 0:
                    print('>>> Preço inválido!')
                else:
                    break

            if novoTitulo:
                livro['titulo'] = novoTitulo
            if novoAutor:
                livro['autor'] = novoAutor
            if novoGenero:
                livro['genero'] = novoGenero
            if novoPreco:
                livro['preco'] = novoPreco

            print('>>> Dados do livro atualizado com sucesso!\n')
            print(f'Título: {livro['titulo']}')
            print(f'-- Autor: {livro['autor']}')
            print(f'-- Gênero: {livro['genero']}')
            print(f'-- Preço: R$ {livro['preco']:.2f}')
    
        else:
            print('\n>>> Livro não encontrado.')
    print('-----------------------------------------------------')

# 7° Função p/ excluir livros do cadastro
def excluirLivro():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('-----------------------------------------------------')
    print('                --- Excluir Livros ---               ')

    livroEscolhido = input('Informe o título do livro que deseja excluir:\n> ').upper()

    for livro in livros:
        if livro['titulo'] == livroEscolhido:
            print(f'>>> Livro encontrado com sucesso!\n')
            print(f'Título: {livro['titulo']}')
            print(f'-- Autor: {livro['autor']}')
            print(f'-- Gênero: {livro['genero']}')
            print(f'-- Preço: R$ {livro['preco']:.2f}')

            confirmacao = input('\nConfirme com "S" a exclusão: ').upper()
            if confirmacao == 'S':
                livros.remove(livro)                   # Método p/ remover o valor passado por parâmetro
                print('\n>>> Livro excluído com sucesso!')  
                break   
            else:
                print('\n>>> Opção inválida!! Tente novamente.')
                #break
    else:
        print('\n>>> Livro não encontrado.')
    print('-----------------------------------------------------')