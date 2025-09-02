import tkinter as tk


# Chamando as funções do terminal:
def cadastrarLivro():
    janelaCadastrar = tk.Toplevel()
    janelaCadastrar.geometry('700x450')

    tk.Label(janelaCadastrar, text='Cadastrar Livro').pack()

    # Título
    tk.Label(janelaCadastrar, text='Título:').pack()
    entry_titulo = tk.Entry(janelaCadastrar)
    entry_titulo.pack()

    # Autor
    tk.Label(janelaCadastrar, text='Autor:').pack()
    entry_autor = tk.Entry(janelaCadastrar)
    entry_autor.pack()

    # Gênero
    tk.Label(janelaCadastrar, text='Gênero:').pack()
    entry_genero = tk.Entry(janelaCadastrar)
    entry_genero.pack()

    # Preço
    tk.Label(janelaCadastrar, text='Preço:').pack()
    entry_preco = tk.Entry(janelaCadastrar)
    entry_preco.pack()

    
    tk.Button(janelaCadastrar, text='Cadastrar').pack()