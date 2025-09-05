import tkinter as tk
from tkinter import ttk, messagebox
from ui.styles import style
from core import livros
from collections import Counter

def exibirLivrosUI():
    if not livros:
        messagebox.showwarning('Lista de Livros', 'Não há livros cadastrados.')
        return
    
    # nova janela
    janelaExibir = tk.Toplevel()
    janelaExibir.title('Lista de Livros')
    janelaExibir.geometry('1400x800+100+100')
    janelaExibir.config(bg=style.COR_FUNDO)

    # frame principal que vai segurar aparecer a tabeloa + barra de rolagem
    frame = tk.Frame(janelaExibir, bg=style.COR_FUNDO)
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
    tree_style.theme_use("clam")
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
    for idx, livro in enumerate(livros):
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
    scroll = ttk.Scrollbar(frame, orient='vertical', command=tree.yview, style="Custom.Vertical.TScrollbar")
    tree.configure(yscrollcommand=scroll.set)

    # posicionamento na tela
    tree.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    # rodapé - qtde de livros cadastrados
    qtd_livros = len(livros)

    # frame (área separada dentro da janela) p/ colocar os elementos do rodapé, c/ total de livros e botão
    rodape = tk.Frame(janelaExibir, bg=style.COR_FUNDO)
    rodape.pack(fill="x", pady=(10, 15))

    # qtde livros cadastrados
    tk.Label(
        rodape,
        text=f"Total de livros cadastrados: {qtd_livros}",
        font=style.FONTE_PADRAO,
        bg=style.COR_FUNDO,
        fg=style.COR_TITULOS
    ).pack()

    # clicou no botão 'Gêneros'
    def mostrarGeneros():
        contagem = Counter(l['genero'] for l in livros)     # classe counter = conta qtos livros existem em cada gênero
        linhas = [f"{g}: {q}" for g, q in sorted(contagem.items())]     # sorted = p/ ordenar de A-Z
        texto = "\n".join(linhas)                                       # junta as linhas em texto único
        messagebox.showinfo("Resumo de Gêneros", texto, parent=janelaExibir)

    tk.Button(
        rodape,
        text="Gêneros",
        command=mostrarGeneros,
        bg=style.COR_BOTOES,
        fg=style.COR_TEXTO,
        font=style.FONTE_PADRAO,
        width=10
    ).pack(pady=5)