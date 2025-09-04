import tkinter as tk
from tkinter import ttk, messagebox

from ui.styles import style

from core import livros

def buscarLivroUI():
    if not livros:
        messagebox.showwarning('Atenção', 'Não há arquivo para buscar, cadastre um livro primeiramente.')
        return
    
    # Funções de busca individuais
    def buscarPorTitulo():
        titulo = entryTitulo.get().upper()
        if not titulo:
            messagebox.showwarning('Atenção', 'Informe o título do livro!', parent=janelaBuscar) 
            entryTitulo.delete(0, tk.END)           # limpa o campo   
            return
        resultados = [livro for livro in livros if livro['titulo'].upper() == titulo]
        mostrarResultados(resultados)
        entryTitulo.delete(0, tk.END) 

    def buscarPorAutor():
        autor = entryAutor.get().upper()
        if not autor:
            messagebox.showwarning('Atenção', 'Informe o autor do livro!', parent=janelaBuscar)
            entryAutor.delete(0, tk.END)    
            return
        resultados = [livro for livro in livros if autor in livro['autor'].upper()]
        mostrarResultados(resultados)
        entryAutor.delete(0, tk.END)

    def buscarPorPalavra():
        palavra = entryPalavra.get().upper()
        if not palavra:
            messagebox.showwarning('Atenção', 'Informe uma palavra!', parent=janelaBuscar) 
            entryPalavra.delete(0, tk.END)  
            return
        resultados = [livro for livro in livros if (palavra in livro['titulo'].upper()) or (palavra in livro['autor'].upper())]
        mostrarResultados(resultados)
        entryPalavra.delete(0, tk.END)

    # Mostrar resultados em nova janela
    def mostrarResultados(resultados):
        if not resultados:
            messagebox.showinfo('Atenção', 'Nenhum livro encontrado.', parent=janelaBuscar)
            return

        janelaResultados = tk.Toplevel(janelaBuscar)
        janelaResultados.title("Resultados da Busca")
        janelaResultados.geometry('1400x300+200+200')
        janelaResultados.config(bg=style.COR_FUNDO)

        # frame principal
        frame = tk.Frame(janelaResultados, bg=style.COR_FUNDO)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # criar tabela
        colunas = ('Título', 'Autor', 'Gênero', 'Preço')
        tree = ttk.Treeview(frame, columns=colunas, show='headings', height=15)
        
        # cabeçalho da tabela
        tree.heading('Título', text='Título')
        tree.heading('Autor', text='Autor')
        tree.heading('Gênero', text='Gênero')
        tree.heading('Preço', text='Preço')

        # largura e alinhamento das colunas
        tree.column('Título', width=550, anchor='w')   
        tree.column('Autor', width=220, anchor='w')
        tree.column('Gênero', width=200, anchor='w')
        tree.column('Preço', width=50, anchor='w')  

        # estilo da tabela - cores, fontes
        tree_style = ttk.Style()
        tree_style.theme_use("clam")             #default       clam
        tree_style.configure("Treeview.Heading",
                        background=style.COR_CABECALHO,         # cor de fundo do cabeçalho
                        foreground=style.COR_TEXTO,             # cor do texto do cabeçalho 
                        font=style.FONTE_TABELA                 # fonte do cabeçalho
        )
        tree_style.configure("Treeview",
                        font=style.FONTE_LINHAS,                # fonte das linhas
                        rowheight=35,                           # altura das linhas
                        background=style.COR_FUNDO,             # cor de fundo padrão
                        fieldbackground=style.COR_FUNDO,        # fundo das células
                        foreground=style.COR_TEXTO_II           # cor do texto das linhas
        )  
        # cor da linha qdo for selecionada
        tree_style.map('Treeview', background=[('selected', style.COR_TITULOS)]) 
        
        # cores alternadas da linhas
        tree.tag_configure('par', background=style.COR_PAR)
        tree.tag_configure('impar', background=style.COR_IMPAR)

        # inserir livros na tabela
        for idx, livro in enumerate(resultados):
            tag = 'par' if idx % 2 == 0 else 'impar'            # alterna entre par e ímpar
            tree.insert('', tk.END, values=(
                livro['titulo'],
                livro['autor'],
                livro['genero'],
                f"R$ {livro['preco']:.2f}"
            ), tags=(tag,))

        # barra de rolagem
        scroll_style = ttk.Style()
        scroll_style.configure("Custom.Vertical.TScrollbar",
                            background=style.COR_CABECALHO,     # mesma cor do cabeçalho
                            troughcolor=style.COR_FUNDO,        # cor do trilho
                            bordercolor=style.COR_TEXTO_II,    
                            arrowcolor=style.COR_TEXTO)         # cor da setinha
        
        # estilo na scrollbar
        scroll = ttk.Scrollbar(frame, orient='vertical', command=tree.yview, style='Custom.Vertical.TScrollbar')
        tree.configure(yscrollcommand=scroll.set)

        # posicionamento na tela
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")        

    # Janela de busca 
    janelaBuscar = tk.Toplevel()
    janelaBuscar.geometry('900x490+90+110')
    janelaBuscar.config(bg=style.COR_FUNDO)
    janelaBuscar.resizable(False, False)

    tk.Label(
        janelaBuscar, 
        text='Buscar Livro', 
        font=style.FONTE_TITS, 
        bg=style.COR_FUNDO, 
        fg=style.COR_TITULOS
    ).pack(pady=10)

    tk.Label(
        janelaBuscar, 
        text='Escolha uma opção de busca:', 
        font=style.FONTE_PADRAO,  
        fg=style.COR_TITULOS, 
        bg=style.COR_FUNDO
    ).pack(pady=5)

    # Buscar por título
    entryTitulo = tk.Entry(janelaBuscar, font=style.FONTE_INPUT)
    entryTitulo.pack(pady=5, fill='x', padx=40)
    tk.Button(
        janelaBuscar, 
        text='Buscar por Título', 
        command=buscarPorTitulo, 
        font=style.FONTE_PADRAO,
        fg=style.COR_TEXTO, 
        bg=style.COR_BOTOES, 
        width=20
    ).pack(pady=5)

    # Buscar por autor
    entryAutor = tk.Entry(janelaBuscar, font=style.FONTE_INPUT)
    entryAutor.pack(pady=5, fill='x', padx=40)
    tk.Button(
        janelaBuscar, 
        text='Buscar por Autor', 
        command=buscarPorAutor, 
        font=style.FONTE_PADRAO,
        fg=style.COR_TEXTO, 
        bg=style.COR_BOTOES, 
        width=20
    ).pack(pady=5)

    # Buscar por palavra
    entryPalavra = tk.Entry(janelaBuscar, font=style.FONTE_INPUT)
    entryPalavra.pack(pady=5, fill='x', padx=40)
    tk.Button(
        janelaBuscar, 
        text='Buscar por Palavra', 
        command=buscarPorPalavra, 
        font=style.FONTE_PADRAO,
        fg=style.COR_TEXTO, 
        bg=style.COR_BOTOES, 
        width=20
    ).pack(pady=5)