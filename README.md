**Título:** Simulação da Máquina Enigma e Bombe em Python 





**Descrição:** 

Bem-vindo ao repositório que apresenta uma simulação da icônica Máquina Enigma e do dispositivo Bombe, ambos utilizados durante a Segunda Guerra Mundial para cifrar e decifrar mensagens secretas. Este programa em Python é uma homenagem à história da criptografia e à contribuição vital de Alan Turing e sua equipe na quebra do código Enigma. 

 

**Funcionalidades Principais:** 

- **Comunicação via Protocolo TCP:** O programa consiste em dois arquivos: `bombe_Machine.py` (servidor) e `enigma_Machine.py` (cliente), que estabelecem uma conexão TCP para enviar mensagens cifradas e decifradas entre si. 

  

- **Execução do Programa:**  

    1. Primeiro, o arquivo do servidor (`bombe_Machine.py`) deve ser executado. Ele aguardará a conexão do cliente. 
    ![Execucao_Bombe](https://github.com/arybytes/Simulador_Turing/assets/165725554/aa39e895-5bf6-4ef0-972e-3f93781d926f)

 

    2. Em seguida, execute o arquivo cliente (`enigma_Machine.py`). Ele estabelecerá a conexão com o servidor e abrirá uma interface para o usuário digitar uma mensagem que será criptografada e enviada para o servidor. 

O exemplo da mensagem abaixo cifrada pela Máquina Enigma pode representar um mandato crucial emitido pelos líderes do Eixo para dar início à Operação Barbarossa, o ataque à União Soviética. 
![Interface_Enigma](https://github.com/arybytes/Simulador_Turing/assets/165725554/6e9a62f1-e2c0-4aba-90bc-7f85d66ad0ee)


- **Máquina Enigma (Cliente):** O arquivo `enigma_Machine.py` simula a funcionalidade da Máquina Enigma, utilizada pelos alemães para criptografar mensagens durante a guerra. Ao reaizar o comando anterior o arquivo `enigma_Machine.py`  gera a mensagem cifradas e envia para o servidor. 
![Execucao_Enigma](https://github.com/arybytes/Simulador_Turing/assets/165725554/3b03f6ba-6840-48f8-8fd3-df28b88d99fd)

  

- **Máquina Bombe (Servidor):** O arquivo `bombe_Machine.py` atua como servidor, recebendo mensagens criptografadas do cliente e aplicando o processo de descriptografia. O resultado é exibido no terminal, revelando o conteúdo original da mensagem. 

  ![Terminal_Bombe](https://github.com/arybytes/Simulador_Turing/assets/165725554/929975e8-4443-4fd1-ac9c-434508094c57)


 

**Importância Histórica:** 

Esta simulação não apenas demonstra as habilidades técnicas necessárias para implementar uma versão virtual das máquinas Enigma e Bombe, mas também serve como um tributo à genialidade de Alan Turing e sua equipe. Seu trabalho na decifração do código Enigma foi fundamental para a vitória dos Aliados na Segunda Guerra Mundial e teve um impacto significativo no desenvolvimento subsequente da computação e da criptografia. 

  

Este repositório é uma oportunidade para os entusiastas da história e da programação explorarem e compreenderem melhor o papel dessas tecnologias pioneiras no contexto histórico da Segunda Guerra Mundial. 
                              ![Alan Turing](https://github.com/arybytes/Simulador_Turing/assets/165725554/24e51687-8328-4a9f-8589-ccaa3a6c9b8e)

