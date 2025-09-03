from tkinter import messagebox

from core import livros
from core.database.salvar import salvarDados

def salvarDadosUI():  
    if not livros:
        messagebox.showwarning('Atenção', 'Não há arquivo para salvar, cadastre um livro primeiramente.')
        return
    
    resposta = messagebox.askyesno('Atenção', 'Houve alguma alteração nos dados? Deseja salvar?')
    if not resposta:
        messagebox.showwarning('', 'Salvamento cancelado.')
        return
    
    salvarDados()

    messagebox.showinfo('', 'Dados salvos com sucesso!')