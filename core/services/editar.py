from core import livros

# 6° Função p/ editar livros cadastrados
def editarLivro():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('\n-----------------------------------------------------')
    print('                --- Editar Livros ---                ')
    
    livroEscolhido = input('Informe o título do livro que deseja editar:\n>  ').upper()

    encontrado = False

    # Testando 'for', mas tb pode ser por while
    for livro in livros:
        if livro['titulo'].upper() == livroEscolhido:
            encontrado = True
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
    
    if not encontrado:
        print('\n>>> Livro não encontrado.')
    print('-----------------------------------------------------')