from core import livros

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

