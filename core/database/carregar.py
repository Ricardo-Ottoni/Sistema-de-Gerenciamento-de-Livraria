from core import livros

# 9° Importar biblioteca p/ verificar existência de dados
import os

# 10° Função p/ carregar dados salvos de um arquivo txt 
def carregarDados():
    # Verificando se existe o arquivo txt
    # 'r' é o modo leitura
    if not os.path.exists('data/livraria.txt'):
        print('\n>>> Não há arquivo para carregar.')
        return
    
    # Abre e fecha o arquivo automaticamente
    with open('data/livraria.txt', 'r', encoding='utf-8') as arquivo:
       
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

    print('\n>>> Dados carregados com sucesso!')
    print('-----------------------------------------------------') 