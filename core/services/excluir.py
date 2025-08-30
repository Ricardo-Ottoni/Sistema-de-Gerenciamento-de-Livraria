from core import livros

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