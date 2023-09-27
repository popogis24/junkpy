import tkinter as tk
from tkinter import ttk
import os
import shutil

def copy_files():
    # Obtém o caminho da pasta raiz
    root_directory = root_directory_entry.get()

    # Cria uma nova pasta para armazenar as cópias dos arquivos zip
    new_directory = destination_directory_entry.get()
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    # Obtém o nome do arquivo alvo
    alvo = alvo_entry.get()

    # Procura todos os arquivos zip com o nome alvo nas pastas e subpastas
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for file_name in filenames:
            if file_name.endswith('.zip') and alvo in file_name:
                # Cria o caminho completo do arquivo
                file_path = os.path.join(dirpath, file_name)

                # Cria o novo nome do arquivo usando um prefixo com base no caminho da pasta
                prefix = os.path.basename(os.path.dirname(file_path))
                new_file_name = f"{prefix}_{file_name}"

                # Faz uma cópia do arquivo na nova pasta com o novo nome
                shutil.copy(file_path, os.path.join(new_directory, new_file_name))

                print(f"Arquivo copiado: {file_name}")

    print("Fim do processo.")

# Cria a janela principal
root = tk.Tk()
root.title("Copiar arquivos")
root.geometry("500x250")
root.resizable(False, False)

# Cria um estilo para personalizar a aparência dos widgets
style = ttk.Style(root)
style.configure('TLabel', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=10)
style.configure('TButton', font=('Arial', 12), padding=10)

# Cria o campo de entrada para o caminho da pasta raiz
root_directory_label = ttk.Label(root, text="Insira o caminho da pasta raiz:")
root_directory_label.pack()
root_directory_entry = ttk.Entry(root)
root_directory_entry.pack()

# Cria o campo de entrada para o nome do arquivo alvo
alvo_label = ttk.Label(root, text="Insira o nome do arquivo zip que você quer extrair:")
alvo_label.pack()
alvo_entry = ttk.Entry(root)
alvo_entry.pack()

# Cria o campo de entrada para o caminho da pasta de destino
destination_directory_label = ttk.Label(root, text="Insira o caminho da pasta de destino:")
destination_directory_label.pack()
destination_directory_entry = ttk.Entry(root)
destination_directory_entry.pack()

# Cria o botão para executar o script
copy_files_button = ttk.Button(root, text="Copiar arquivos", command=copy_files, style='AccentButton')
copy_files_button.pack(pady=10)

# Define o estilo para o botão
style.map('AccentButton', background=[('active', 'orange')])

# Inicia o loop principal do Tkinter
root.mainloop()
