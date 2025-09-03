import tkinter as tk
from tkinter import messagebox

import os
from core import livros
from core.database.carregar import carregarDados as backendCarregar

def carregarDados():
    backendCarregar()
    if not livros:
        messagebox.showwarning('', 'Não há arquivo para carregar.')