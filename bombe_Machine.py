# Este arquivo simula a Máquina Bombe criada por Alan Turing para descriptografar as mensagens
# codificadas transmitidas pela Máquina Enigma

import socket
import base64

def descriptografar_mensagem(mensagem_codificada):

    try:
        mensagem_decodificada = base64.b64decode(mensagem_codificada).decode('utf-8')
        return mensagem_decodificada
    except Exception as e:
        return f"Erro durante a descriptografia: {str(e)}"

def main():
    servidor = "127.0.0.1"
    porta = 4040

    # fazendo conexão TCP com o enigma_Machine.py
    bombe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bombe.bind((servidor, porta))
    bombe.listen(1)

    print(f"Aguardando transmissões da Máquina Enigma....")

    while True:
        enigma, enigma_Machine = bombe.accept()
        print(f"Conexão realizada.")
        # descriptografando a mensagem recebida da máquina enigma
        mensagem_codificada = enigma.recv(1024).decode('utf-8')
        mensagem_descriptografada = descriptografar_mensagem(mensagem_codificada)

        # exibindo mensagem recebida e descriptografada pela máquina Bombe
        print(f"Mensagem Recebida: |{mensagem_codificada}|\n")

        print(f"Mensagem Descriptografada: {mensagem_descriptografada}\n")

        enigma.close()

if __name__ == "__main__":
    main()