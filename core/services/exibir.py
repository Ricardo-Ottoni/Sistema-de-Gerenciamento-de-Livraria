from core import livros

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
        print(f'Título: {livro["titulo"]}')
        print(f'-- Autor: {livro["autor"]}')
        print(f'-- Gênero: {livro["genero"]}')
        print(f'-- Preço: R$ {livro["preco"]:.2f}\n')
        i += 1

    print(f'>>> Total de livros cadastrados: {i}')
    print('-----------------------------------------------------')