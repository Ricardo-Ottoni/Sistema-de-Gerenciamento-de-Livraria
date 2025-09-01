import tkinter as tk
from tkinter import ttk 
from styles import style

# Janela principal
janela = tk.Tk()
janela.title('SISTEMA DE GERENCIAMENTO DE LIVRARIA')
janela.geometry('850x750')
janela.resizable(False, False)            # fixar tamanho janela
janela.config(bg=style.COR_FUNDO)

# Rótulo principal
label = tk.Label(
    janela, 
    text='MENU', 
    font=style.FONTE_TITULO, 
    bg=style.COR_FUNDO, 
    fg=style.COR_TITULOS
    )
label.pack(pady=(20, 5))  
# Posiciona o label na janela usando pack()
# 'pady' define o espaçamento vertical: 20px acima, 5px abaixo do label

# Frame (containter) botões
frameBotões = tk.Frame(
    janela, 
    bg=style.COR_FRAME, 
    )
frameBotões.pack(
    padx=100,           # espaço horizontal entre as bordas da janela e o frame
    pady=(20, 70),      # espaço vertical: 20px acima e 70px abaixo do frame
    fill="both",        # faz o frame se expandir p/ preencher tanto largura quanto altura disponível
    expand=True         # permite que o frame expanda p/ ocupar espaço extra na janela
    )

# Botões
btn1 = tk.Button(
    frameBotões, 
    text='Cadastrar Livro no Sistema', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO,
    )
btn1.pack(pady=(30, 15))

btn2 = tk.Button(
    frameBotões, 
    text='Exibir Livros Cadastrados', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn2.pack(pady=15)

btn3 = tk.Button(
    frameBotões, 
    text='Buscar um Livro Específico', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn3.pack(pady=15)

btn4 = tk.Button(
    frameBotões, 
    text='Editar Dados de um Livro', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn4.pack(pady=15)

btn5 = tk.Button(
    frameBotões, 
    text='Excluir Livro do Sistema', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn5.pack(pady=15)

btn6 = tk.Button(
    frameBotões, 
    text='Salvar Dados no Sistema', 
    width=35, 
    bg=style.COR_BOTOES, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn6.pack(pady=15)

btn7 = tk.Button(
    frameBotões, 
    text='Sair', 
    width=35, 
    bg=style.COR_BOTAO_SAIR, 
    fg=style.COR_TEXTO, 
    font=style.FONTE_PADRAO
    )
btn7.pack(pady=(15))

# Exibir a janela
janela.mainloop()