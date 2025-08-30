from core import livros

import os

# 8° Função p/ salvar os dados do sistema em arquivo txt 
def salvarDados():
    if not livros:
        print('\n>>> Não há livros cadastrados.')
        return
    
    print('-----------------------------------------------------')
    print('                --- Salvar Dados ---                 ')

    # with faz parte da biblioteca do Python, age garatindo q o arquivo será fechado automaticamente
    # open vai abrir ou criar um arquivo de texto, no caso chamdo de livros.txt
    # 'w' é o modo de escrita e 'utf-8' padrão p/ suportar acentos que nem no html
    with open('data/livraria.txt', 'w', encoding='utf-8') as arquivo:
        i = 0
        
        # Pode ser por 'for' tb.
        while i < len(livros):
            livro = livros[i]

            # Cria os dados de cada livro
            dadosLivro = f"{livro['titulo']} | {livro['autor']} | {livro['genero']} | {livro['preco']:.2f}\n"

            # Escreve os dados no arquivo
            arquivo.write(dadosLivro)

            i += 1

        print('\n>>> Dados salvos com sucesso!')
    print('-----------------------------------------------------')