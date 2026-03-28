import tkinter as tk
from tkinter import messagebox

from util.validacao import validar_nome, validar_nota, validar_cep
from util.cep import buscar_endereco
from util.calculos import media, aprovado
from util.banco import inserir_registro


def iniciar() -> None:
    # janela
    janela = tk.Tk()
    janela.title("Cadastro de Alunos")
    janela.resizable(False,False)
    janela.configure(padx=16,pady=16)

# WIDGETS - FORMS

    tk.Label(janela,text="Nome").grid(
        row=0, 
        column=0,
        sticky="w",
        pady=4

    )

    tk.Label(janela, text="Nome").grid(row=0, column=0, sticky="w", pady=4)
    entry_nome = tk.Entry(janela, width=32)
    entry_nome.grid(row=0, column=1, pady=4)

    tk.Label(janela, text="Nota 1").grid(row=1, column=0, sticky="w", pady=4)
    entry_n1 = tk.Entry(janela, width=32)
    entry_n1.grid(row=1, column=1, pady=4)

    tk.Label(janela, text="Nota 2").grid(row=2, column=0, sticky="w", pady=4)
    entry_n2 = tk.Entry(janela, width=32)
    entry_n2.grid(row=2, column=1, pady=4)

    tk.Label(janela, text="CEP").grid(row=3, column=0, sticky="w", pady=4)
    entry_cep = tk.Entry(janela, width=32)
    entry_cep.grid(row=3, column=1, pady=4)

    # Label de feedback do endereço encontrado
    label_endereco = tk.Label(janela, text="", fg="gray", wraplength=280)
    label_endereco.grid(row=5, column=0, columnspan=2, pady=4)

    # =========================================================
    # WIDGETS — botões
    # =========================================================
    tk.Button(janela, text="Buscar CEP")
    tk.Button(janela, text="Cadastrar")

    # =========================================================
    # LOOP
    # =========================================================
    janela.mainloop()