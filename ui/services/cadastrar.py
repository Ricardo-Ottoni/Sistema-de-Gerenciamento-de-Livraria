import tkinter as tk
from tkinter import messagebox
from ui.styles import style
from core import livros

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

    # Função p/ enviar os dados ao backend
    def enviar():
        titulo = entry_titulo.get().strip().upper()
        autor = entry_autor.get().strip()
        genero = entry_genero.get().strip()
        precoSTR = entry_preco.get().strip()

        # verificar se há algum campo vazio
        if not titulo or not autor or not genero or not precoSTR:
            messagebox.showwarning('Atenção', 'Não pode haver campos vazios.', parent=janelaCadastrar)
            return
        
        # Verificar se preço é válido
        if not precoSTR.replace('.', '', 1).isdigit():
            messagebox.showwarning('Atenção', 'Preço inválido! Digite apenas números.', parent=janelaCadastrar)
            return

        preco = float(precoSTR)
        if preco <= 0:
            messagebox.showwarning('Atenção', 'Preço inválido! Deve ser maior que zero.', parent=janelaCadastrar)
            return

        # verificar se já existe o livro com mesmo autor
        if any(livro['titulo'] == titulo and livro['autor'] == autor for livro in livros):
            messagebox.showwarning('Atenção', f'O livro "{titulo}" do autor "{autor}" já está cadastrado.', parent=janelaCadastrar)
            return

        # Adiciona via backend
        livros.append({
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'preco': preco
        })

        messagebox.showinfo('', f'Livro "{titulo}" do autor "{autor}" foi cadastrado com sucesso!', parent=janelaCadastrar)
        janelaCadastrar.destroy()

    # Botão
    tk.Button(
        janelaCadastrar, 
        text='Cadastrar',
        command=enviar,
        font=style.FONTE_PADRAO,
        fg=style.COR_TEXTO,
        bg=style.COR_BOTOES,
        width=15
    ).pack(pady=15)