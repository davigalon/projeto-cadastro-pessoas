import tkinter as tk
from arquivo import *
from interface import *

root = tk.Tk()
root.title("Menu de Cadastro")


label_title = tk.Label(root, text="Gerenciador de Registros v0.1", font=("Times New Roman", 20, "bold"))
label_title.pack()

label1 = tk.Button(root, text="Ver pessoas cadastradas", font=("Times New Roman", 12), command=lambda: pagina_cadastrados(ler_arquivo("pessoas.txt")))
label1.pack()

label2 = tk.Button(root, text="Cadastrar nova pessoa", font=("Times New Roman", 12), command=lambda: pagina_cadastrar("pessoas.txt"))
label2.pack()

label3 = tk.Button(root, text="Sair", font=("Times New Roman", 12), background="red", command=lambda:exit())
label3.pack()

root.mainloop()