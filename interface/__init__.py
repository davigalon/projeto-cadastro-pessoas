import tkinter as tk
from arquivo import cadastrar_pessoa

def pagina_cadastrados(data):
    alt_root = tk.Tk()

    for cadastro in data:
        x = tk.Label(alt_root, text=cadastro, font=("Times New Roman", 12))
        x.pack()

    alt_root.mainloop()


def pagina_cadastrar(caminho):
    alt_root = tk.Tk()

    label_nome = tk.Label(alt_root, text="Digite o nome do amigo", font=("Times New Roman", 12))
    label_nome.pack()
    
    entry_nome = tk.Entry(alt_root, font=("Times New Roman", 12))
    entry_nome.pack()

    label_idade = tk.Label(alt_root, text="Digite a idade do amigo", font=("Times New Roman", 12))
    label_idade.pack()
    
    entry_idade = tk.Entry(alt_root, font=("Times New Roman", 12))
    entry_idade.pack()

    button_confirmar = tk.Button(alt_root, text="Confirmar", font=("Times New Roman", 12), background="lime",
                                 command=lambda: cadastrar_pessoa(caminho, entry_nome.get(), entry_idade.get()))
    button_confirmar.pack()
    alt_root.mainloop()