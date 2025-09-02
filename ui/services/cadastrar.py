import tkinter as tk
from tkinter import ttk 
from styles import style

# Chamando as funções do terminal:
def cadastrarLivro():
    janelaCadastrar = tk.Toplevel()
    janelaCadastrar.geometry('900x560+150+170')
    janelaCadastrar.config(bg=style.COR_FUNDO)  
    janelaCadastrar.resizable(False, False)

    tk.Label(
        janelaCadastrar, 
        text='Cadastrar Livro',
        font=style.FONTE_TITS, 
        bg=style.COR_FUNDO, 
        fg=style.COR_TITULOS,
    ).pack(pady=10)
    

    # Título
    tk.Label(
        janelaCadastrar, 
        text='Título:',
        font=style.FONTE_PADRAO,
        bg=style.COR_FUNDO,
        fg=style.COR_TITULOS,
    ).pack(pady=5)
    entry_titulo = tk.Entry(janelaCadastrar, font=style.FONTE_INPUT)
    entry_titulo.pack(pady=5, fill='x', padx=40)

    # Autor
    tk.Label(
        janelaCadastrar, 
        text='Autor:', 
        font=style.FONTE_PADRAO, 
        bg=style.COR_FUNDO,
        fg=style.COR_TITULOS,
    ).pack(pady=5)
    entry_autor = tk.Entry(janelaCadastrar, font=style.FONTE_INPUT)
    entry_autor.pack(pady=5, fill='x', padx=40)

    # Gênero
    tk.Label(
        janelaCadastrar, 
        text='Gênero:', 
        font=style.FONTE_PADRAO,
        bg=style.COR_FUNDO,
        fg=style.COR_TITULOS,
    ).pack(pady=5)
    entry_genero = tk.Entry(janelaCadastrar, font=style.FONTE_INPUT)
    entry_genero.pack(pady=5, fill='x', padx=40)

    # Preço
    tk.Label(
        janelaCadastrar, 
        text='Preço:', 
        font=style.FONTE_PADRAO,
        bg=style.COR_FUNDO,
        fg=style.COR_TITULOS,
    ).pack(pady=5)
    entry_preco = tk.Entry(janelaCadastrar, font=style.FONTE_INPUT)
    entry_preco.pack(pady=5, fill='x', padx=40)

    # Botão
    tk.Button(
        janelaCadastrar, 
        text='Cadastrar',
        font=style.FONTE_PADRAO,
        fg=style.COR_TEXTO,
        bg=style.COR_BOTOES,
        width=15
    ).pack(pady=15)