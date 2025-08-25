# 9° Importar biblioteca p/ verificar existência de dados
import os

# 2° Criação de uma lista vazia
livros = []


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
    with open('livraria.txt', 'w', encoding='utf-8') as arquivo:
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

# 10° Função p/ carregar dados salvos de um arquivo txt 
def carregarDados():
    # Verificando se existe o arquivo txt
    # 'r' é o modo leitura
    if not os.path.exists('livraria.txt'):
        print('\n>>> Não há arquivo para carregar.')
        return
    else:
        print('\n>>> Dados carregados com sucesso!')

    # Abre e fecha o arquivo automaticamente
    with open('livraria.txt', 'r', encoding='utf-8') as arquivo:

        # Pode ser por 'while' tb.
        for dadosLivro in arquivo:
            dados = dadosLivro.split(' | ')          # split é p/ dividir em partes com base em um separador
            if len(dados) == 4:
                livros.append({
                    'titulo': dados[0],
                    'autor': dados[1],
                    'genero': dados[2],
                    'preco': float(dados[3])
                })