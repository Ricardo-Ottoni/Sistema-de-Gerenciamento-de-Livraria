import tkinter as tk
from tkinter import messagebox
from ui.styles import style
from core import livros

def editarLivroUI():
    if not livros:
        messagebox.showwarning('Atenção', 'Não há arquivo para editar, cadastre um livro primeiramente.')
        return

    # janela p/ edição
    janelaEditar = tk.Toplevel()
    janelaEditar.geometry('900x700+150+150')
    janelaEditar.config(bg=style.COR_FUNDO)
    janelaEditar.resizable(False, False)

    # Título da janela
    tk.Label(janelaEditar, 
             text='Editar Livro', 
             font=style.FONTE_TITS, 
             bg=style.COR_FUNDO,
             fg=style.COR_TITULOS
    ).pack(pady=10)

    # 1) Buscar o livro pelo título
    tk.Label(janelaEditar, 
             text='Informe o título do livro que deseja editar:', 
             font=style.FONTE_PADRAO, 
             bg=style.COR_FUNDO,
             fg=style.COR_TITULOS
    ).pack(pady=5)
    entry_busca = tk.Entry(
        janelaEditar, 
        font=style.FONTE_INPUT
    )
    entry_busca.pack(
        pady=5, 
        fill='x', 
        padx=40
    )

    # Container p/ os campos de edição (só aparece após encontrar)
    frame_edicao = tk.Frame(
        janelaEditar, 
        bg=style.COR_FUNDO 
    )

    # Entradas que serão criadas qdo encontrar
    # Dicionário para armazenar as referências dos campos de entrada
    entradas = {}                   # guardará refs: {'titulo': entry, 'autor': entry, ...}
    livro_ref = {'obj': None}       # referência ao dicionário do livro na lista

    def validar_preco_str(s):
        s = s.strip()
        # aceita números decimais com ponto
        return s.replace('.', '', 1).isdigit()

    # Procura exata pelo título na lista de livros
    def buscar():
        titulo_busca = entry_busca.get().strip().upper()
        if not titulo_busca:
            messagebox.showwarning('Atenção', 'Informe o título do livro!', parent=janelaEditar)
            return

        # procura exata por título
        encontrado = None
        for lv in livros:
            if lv['titulo'].upper() == titulo_busca:
                encontrado = lv
                break

        if not encontrado:
            messagebox.showwarning('', 'Nenhum livro encontrado.', parent=janelaEditar)
            return

        # guarda referência ao dicionário do livro encontrado
        livro_ref['obj'] = encontrado

        # Exibe frame de edição
        frame_edicao.pack(
            fill='both', 
            expand=True, 
            padx=40, 
            pady=10
        )

        # limpa se já existia algo
        for w in frame_edicao.winfo_children():
            w.destroy()
        entradas.clear()

        # Cmpos pré-preenchidos 
        # Título
        tk.Label(
            frame_edicao, 
            text='Título:', 
            font=style.FONTE_PADRAO, 
            bg=style.COR_FUNDO,
            fg=style.COR_TITULOS,
        ).pack(anchor='w', pady=(0,2))
        e_titulo = tk.Entry(
            frame_edicao, 
            font=style.FONTE_INPUT
        )
        e_titulo.insert(0, encontrado['titulo'])
        e_titulo.pack(
            fill='x', 
            pady=(0,8)
        )

        # Autor
        tk.Label(frame_edicao, 
                 text='Autor:', 
                 font=style.FONTE_PADRAO, 
                 bg=style.COR_FUNDO,
                 fg=style.COR_TITULOS,
        ).pack(anchor='w', pady=(0,2))
        e_autor = tk.Entry(
            frame_edicao, 
            font=style.FONTE_INPUT
        )
        e_autor.insert(0, encontrado['autor'])
        e_autor.pack(fill='x', 
                     pady=(0,8)
        )

        # Gênero
        tk.Label(
            frame_edicao, 
            text='Gênero:', 
            font=style.FONTE_PADRAO, 
            bg=style.COR_FUNDO,
            fg=style.COR_TITULOS,
        ).pack(anchor='w', pady=(0,2))
        e_genero = tk.Entry(
            frame_edicao, 
            font=style.FONTE_INPUT
        )
        e_genero.insert(0, encontrado['genero'])
        e_genero.pack(
            fill='x', 
            pady=(0,8)
        )

        # Preço
        tk.Label(
            frame_edicao, 
            text='Preço:', 
            font=style.FONTE_PADRAO, 
            bg=style.COR_FUNDO,
            fg=style.COR_TITULOS,).pack(anchor='w', pady=(0,2))
        e_preco = tk.Entry(
            frame_edicao, 
            font=style.FONTE_INPUT
        )
        e_preco.insert(0, f"{encontrado['preco']:.2f}")
        e_preco.pack(
            fill='x', 
            pady=(0,8)
        )

        # Guardar os campos no dicionário entradas
        entradas['titulo'] = e_titulo
        entradas['autor'] = e_autor
        entradas['genero'] = e_genero
        entradas['preco']  = e_preco

        # Botões salvar/cancelar
        btns = tk.Frame(
            frame_edicao, 
            bg=style.COR_FUNDO
        )
        btns.pack(pady=10)
        tk.Button(
            btns, 
            text='Salvar', 
            command=salvar, 
            bg=style.COR_BOTOES, 
            fg=style.COR_TEXTO,
            font=style.FONTE_PADRAO, 
            width=10
        ).pack(side='left', padx=5)
        tk.Button(
            btns, 
            text='Cancelar', 
            command=janelaEditar.destroy, 
            bg=style.COR_BOTOES, 
            fg=style.COR_TEXTO,
            font=style.FONTE_PADRAO,  
            width=10
        ).pack(side='left', padx=5)
        
    # Função ao clicar em "Salvar"
    def salvar():
        if not livro_ref['obj']:
            return

        livro = livro_ref['obj']

        # Pega os novos valores digitados
        novo_titulo = entradas['titulo'].get().strip()
        novo_autor  = entradas['autor'].get().strip()
        novo_genero = entradas['genero'].get().strip()
        novo_precoS = entradas['preco'].get().strip()

        # Exigir que campos estejam preenchidos
        if not novo_titulo or not novo_autor or not novo_genero or not novo_precoS:
            messagebox.showwarning('Atenção', 'Preencha todos os campos antes de salvar.', parent=janelaEditar)
            return

        # Validar preço
        if not validar_preco_str(novo_precoS):
            messagebox.showwarning('Atenção', 'Preço inválido! Digite apenas números e ponto decimal.', parent=janelaEditar)
            return

        novo_preco = float(novo_precoS)
        if novo_preco <= 0:
            messagebox.showwarning('Atenção', 'Preço inválido! Deve ser maior que zero.', parent=janelaEditar)
            return

        # Atualizar todos os campos no backend com os valores atuais dos Entry (se o usuário não alterou, ficará igual!)
        livro['titulo'] = novo_titulo.upper()
        livro['autor']  = novo_autor
        livro['genero'] = novo_genero
        livro['preco']  = novo_preco

        messagebox.showinfo('', 'Dados do livro atualizados com sucesso!', parent=janelaEditar)
        janelaEditar.destroy()

    tk.Button(
        janelaEditar, 
        text='Buscar', 
        command=buscar, 
        bg=style.COR_BOTOES, 
        fg=style.COR_TEXTO,
        font=style.FONTE_PADRAO, 
        width=10
    ).pack(pady=10)