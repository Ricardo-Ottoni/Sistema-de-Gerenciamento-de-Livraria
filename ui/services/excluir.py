import tkinter as tk
from tkinter import messagebox
from ui.styles import style
from core import livros

def excluirLivroUI():
    if not livros:
        messagebox.showwarning('Atenção', 'Não há arquivo para excluir, cadastre um livro primeiramente.')
        return

    # nova janela p/ exclusão
    janelaExcluir = tk.Toplevel()
    janelaExcluir.geometry('900x550+250+200')
    janelaExcluir.config(bg=style.COR_FUNDO)
    janelaExcluir.resizable(False, False)

    # Título
    tk.Label(
        janelaExcluir, 
        text='Excluir Livro', 
        font=style.FONTE_TITS, 
        bg=style.COR_FUNDO, 
        fg=style.COR_TITULOS
    ).pack(pady=10)

    # Label com campo de pesquisa
    tk.Label(
        janelaExcluir, 
        text='Informe o título do livro:', 
        font=style.FONTE_PADRAO,
        bg=style.COR_FUNDO, 
        fg=style.COR_TITULOS
    ).pack(anchor='w', pady=(0,2), padx=40)
    entry_tituloExcluir = tk.Entry(
        janelaExcluir, 
        font=style.FONTE_PADRAO,
    )
    entry_tituloExcluir.pack(
        pady=(0,8), 
        fill='x', 
        padx=40
    )

    # Pesquisar livro na base de dados
    def pesquisarLivro():
        nonlocal livro_encontrado                               # usar variável externa dentro da função
        titulo = entry_tituloExcluir.get().strip().upper()      # pega o valor do campo
        if not titulo:
            messagebox.showwarning('Atenção', 'Informe o título do livro!', parent=janelaExcluir)
            return

        # limpar labels e esconde o botão excluir
        lbl_titulo.config(text="")
        lbl_autor.config(text="")
        lbl_genero.config(text="")
        lbl_preco.config(text="")
        btn_excluir.pack_forget()

        # buscar o livro
        for livro in livros:
            if livro['titulo'].upper() == titulo:
                livro_encontrado = livro
                break
        else:
            livro_encontrado = None

        if not livro_encontrado:
            messagebox.showwarning('Atenção', f'Livro "{titulo}" não encontrado.', parent=janelaExcluir)
            return
        
        # mostrar detalhes
        lbl_titulo.config(text=f"Título: {livro_encontrado['titulo']}")
        lbl_autor.config(text=f"Autor: {livro_encontrado['autor']}")
        lbl_genero.config(text=f"Gênero: {livro_encontrado['genero']}")
        lbl_preco.config(text=f"Preço: R$ {livro_encontrado['preco']:.2f}")

        # mostrar botão excluir
        btn_excluir.pack(pady=20)

    tk.Button(
        janelaExcluir, 
        text='Pesquisar', 
        command=pesquisarLivro, 
        bg=style.COR_BOTOES,
        fg=style.COR_TEXTO,
        font=style.FONTE_PADRAO, 
        width=10
    ).pack(pady=(0,15))

    # frame para mostrar os detalhes do livro
    frame_detalhes = tk.Frame(janelaExcluir, bg=style.COR_FUNDO)
    frame_detalhes.pack(pady=20)

     # Labels para mostrar detalhes do livro encontrado
    lbl_titulo = tk.Label(frame_detalhes, text="", font=style.FONTE_PADRAO, bg=style.COR_FUNDO, fg=style.COR_TEXTO_II)
    lbl_titulo.pack(anchor="w", padx=40)

    lbl_autor = tk.Label(frame_detalhes, text="", font=style.FONTE_PADRAO, bg=style.COR_FUNDO, fg=style.COR_TEXTO_II)
    lbl_autor.pack(anchor="w", padx=40)

    lbl_genero = tk.Label(frame_detalhes, text="", font=style.FONTE_PADRAO, bg=style.COR_FUNDO, fg=style.COR_TEXTO_II)
    lbl_genero.pack(anchor="w", padx=40)

    lbl_preco = tk.Label(frame_detalhes, text="", font=style.FONTE_PADRAO, bg=style.COR_FUNDO, fg=style.COR_TEXTO_II)
    lbl_preco.pack(anchor="w", padx=40)

    # botão excluir (só aparece se encontrar o livro)
    btn_excluir = tk.Button(
        janelaExcluir, 
        text='Excluir', 
        bg=style.COR_BOTOES,
        fg=style.COR_TEXTO,
        font=style.FONTE_PADRAO, 
        width=10,
        command=lambda: confirmarExclusao(livro_encontrado)
    )
    btn_excluir.pack_forget()  # escondido por padrão

    livro_encontrado = None  # variável para guardar o livro
 
    def confirmarExclusao(livro):
        if not livro:
            return
        confirm = messagebox.askyesno('Confirmação', f'Deseja excluir o livro "{livro["titulo"]}"?', parent=janelaExcluir)
        if confirm:
            livros.remove(livro)
            messagebox.showinfo('Sucesso', f'Livro "{livro["titulo"]}" excluído com sucesso!', parent=janelaExcluir)
            janelaExcluir.destroy()         # Fechar a janela depois de excluir