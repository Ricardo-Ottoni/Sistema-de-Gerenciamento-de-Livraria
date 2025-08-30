import tkinter as tk

# Janela principal
janela = tk.Tk()
janela.title('SISTEMA DE GERENCIAMENTO DE LIVRARIA')
janela.geometry('600x400')

# Rótulo principal
label = tk.Label(janela, text='MENU')
label.pack()

# Botões
btn1 = tk.Button(janela, text='Cadastrar Livro no Sistema')
btn1.pack()

btn2 = tk.Button(janela, text='Exibir Livros Cadastrados')
btn2.pack()

btn3 = tk.Button(janela, text='Buscar um Livro Específico')
btn3.pack()

btn4 = tk.Button(janela, text='Editar Dados de um Livro ')
btn4.pack()

btn5 = tk.Button(janela, text='Excluir Livro do Sistema')
btn5.pack()

btn6 = tk.Button(janela, text='Salvar Dados no Sistema')
btn6.pack()

btn7 = tk.Button(janela, text='Sair')
btn7.pack()

# Exibir a janela
janela.mainloop()