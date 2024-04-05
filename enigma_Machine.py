# Este arquivo simula a Máquina Enigma utilizada pelos nazistas
# durante a Segunda Guerra Mundial para emitir mensagens em códigos cifrados.

import socket
import base64
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def encriptografar_mensagem(mensagem):
    mensagem_codificada = base64.b64encode(mensagem.encode("utf-8")).decode("utf-8")
    return mensagem_codificada

def enviar_mensagem():
    mensagem = texto_entry.get()
    mensagem_criptografada = encriptografar_mensagem(mensagem)
    enigma.send(mensagem_criptografada.encode("utf-8"))
    janela.destroy()  # Fecha a janela após enviar a mensagem

# Criar a janela
janela = tk.Tk()
janela.title("Máquina Enigma")
janela.geometry("500x333")  # Definindo o tamanho da janela

# Adicionar imagem de fundo
background_image = Image.open("bombe (1).jpg")
background_image = background_image.resize((500, 333))
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(janela, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adicionar caixa de texto
texto_entry = tk.Entry(janela, font=('Arial', 11), justify='center',width=45, border=0.5, relief='solid')
texto_entry.place(relx=0.5, rely=0.2, anchor='center')

# Criando o estilo para o botão personalizado
janela.style = ttk.Style()
janela.style.configure('W.TButton', background="black", foreground="black", font=("Arial", 10), borderwidth=2, relief="solid")

# Adicionar botão diretamente à janela
enviar_button = ttk.Button(janela, text="enviar mensagem", command=enviar_mensagem, style='W.TButton')
enviar_button.place(relx=0.5, rely=0.3, anchor='center')

# Definindo a cor de fundo da janela para corresponder à cor de fundo do botão
janela.configure(bg="black")

# Configurar socket
servidor = "127.0.0.1"
porta = 4040
enigma = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enigma.connect((servidor, porta))

# Loop principal da interface
print(f"Clique no Terminal bombe_Machine para visualizar a execução...")
janela.mainloop()
