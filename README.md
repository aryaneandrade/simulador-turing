**Título:** Simulação da Máquina Enigma e Bombe em Python 

 ![Imagem](enigma (1).jpg)


**Descrição:** 

Bem-vindo ao repositório que apresenta uma simulação da icônica Máquina Enigma e do dispositivo Bombe, ambos utilizados durante a Segunda Guerra Mundial para cifrar e decifrar mensagens secretas. Este programa em Python é uma homenagem à história da criptografia e à contribuição vital de Alan Turing e sua equipe na quebra do código Enigma. 

 

**Funcionalidades Principais:** 

- **Comunicação via Protocolo TCP:** O programa consiste em dois arquivos: `bombe_Machine.py` (servidor) e `enigma_Machine.py` (cliente), que estabelecem uma conexão TCP para enviar mensagens cifradas e decifradas entre si. 

  

- **Execução do Programa:**  

    1. Primeiro, o arquivo do servidor (`bombe_Machine.py`) deve ser executado. Ele aguardará a conexão do cliente. 

 

    2. Em seguida, execute o arquivo cliente (`enigma_Machine.py`). Ele estabelecerá a conexão com o servidor e abrirá uma interface para o usuário digitar uma mensagem que será criptografada e enviada para o servidor. 

O exemplo da mensagem abaixo cifrada pela Máquina Enigma pode representar um mandato crucial emitido pelos líderes do Eixo para dar início à Operação Barbarossa, o ataque à União Soviética. 

 

  

- **Máquina Enigma (Cliente):** O arquivo `enigma_Machine.py` simula a funcionalidade da Máquina Enigma, utilizada pelos alemães para criptografar mensagens durante a guerra. Ao reaizar o comando anterior o arquivo `enigma_Machine.py`  gera a mensagem cifradas e envia para o servidor. 

 

  

- **Máquina Bombe (Servidor):** O arquivo `bombe_Machine.py` atua como servidor, recebendo mensagens criptografadas do cliente e aplicando o processo de descriptografia. O resultado é exibido no terminal, revelando o conteúdo original da mensagem. 

  

 

**Importância Histórica:** 

Esta simulação não apenas demonstra as habilidades técnicas necessárias para implementar uma versão virtual das máquinas Enigma e Bombe, mas também serve como um tributo à genialidade de Alan Turing e sua equipe. Seu trabalho na decifração do código Enigma foi fundamental para a vitória dos Aliados na Segunda Guerra Mundial e teve um impacto significativo no desenvolvimento subsequente da computação e da criptografia. 

  

Este repositório é uma oportunidade para os entusiastas da história e da programação explorarem e compreenderem melhor o papel dessas tecnologias pioneiras no contexto histórico da Segunda Guerra Mundial. 

 
