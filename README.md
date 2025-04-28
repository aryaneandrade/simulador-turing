# 🛡️ Simulação da Máquina Enigma e Bombe em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![TCP](https://img.shields.io/badge/Protocol-TCP-005f73)
![Project](https://img.shields.io/badge/Project-Simulation-orange)

---

## 📜 Descrição
Este repositório apresenta uma simulação da Máquina Enigma e do dispositivo Bombe, ambos utilizados durante a Segunda Guerra Mundial para cifrar e decifrar mensagens secretas. Desenvolvido em Python, o projeto é uma homenagem à história da criptografia e à contribuição vital de Alan Turing e sua equipe na quebra do código Enigma.

---

## 📋 Requisitos

| Item         | Versão     | Observação            |
|--------------|------------|------------------------|
| Python       | 3.10 ou superior | Bibliotecas padrão (socket, threading) |

> Nenhuma instalação de biblioteca externa é necessária.

---

## ⚙️ Funcionalidades Principais
- **Comunicação via Protocolo TCP:** 
  - `bombe_Machine.py` (servidor)
  - `enigma_Machine.py` (cliente)

Esses arquivos estabelecem uma conexão TCP para envio e recepção de mensagens cifradas e decifradas.

---

## 🚀 Execução do Programa

1. **Execute o servidor** (`bombe_Machine.py`) primeiro. Ele ficará aguardando a conexão do cliente.
   
   <p align="center">
     <img src="https://github.com/arybytes/Simulador_Turing/assets/165725554/aa39e895-5bf6-4ef0-972e-3f93781d926f" width="500" alt="Execução Bombe">
   </p>

2. **Execute o cliente** (`enigma_Machine.py`) em seguida. Ele abrirá uma interface para digitar uma mensagem que será criptografada e enviada ao servidor.

   > O exemplo de mensagem cifrada abaixo poderia representar um mandato crucial emitido para a Operação Barbarossa (invasão da União Soviética).

   <p align="center">
     <img src="https://github.com/arybytes/Simulador_Turing/assets/165725554/f94286dd-6219-472d-8a9e-eaa3db9a768b" width="500" alt="Interface Enigma">
   </p>

3. **Máquina Enigma (Cliente):**  
O arquivo `enigma_Machine.py` simula a funcionalidade da Máquina Enigma, criptografando a mensagem antes de enviá-la ao servidor.

   <p align="center">
     <img src="https://github.com/arybytes/Simulador_Turing/assets/165725554/3b03f6ba-6840-48f8-8fd3-df28b88d99fd" width="500" alt="Execução Enigma">
   </p>

4. **Máquina Bombe (Servidor):**  
O arquivo `bombe_Machine.py` recebe as mensagens cifradas e realiza o processo de descriptografia, exibindo o conteúdo original no terminal.

   <p align="center">
     <img src="https://github.com/arybytes/Simulador_Turing/assets/165725554/929975e8-4443-4fd1-ac9c-434508094c57" width="500" alt="Terminal Bombe">
   </p>

---

## 🧠 Importância Histórica
Esta simulação, ainda que simplificada, busca ilustrar as complexas operações de criptoanálise da Máquina Enigma. A genialidade de Alan Turing e sua equipe foi decisiva para a vitória dos Aliados e impulsionou o desenvolvimento da computação moderna e da criptografia.

<p align="center">
  <img src="https://github.com/arybytes/Simulador_Turing/assets/165725554/24e51687-8328-4a9f-8589-ccaa3a6c9b8e" width="500" alt="Alan Turing">
</p>
