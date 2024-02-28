# Ponderada semana 3

## Descrição

Este repositório contém o código relacionado à programação de um robô, juntamente com uma interface visual baseada em linha de comando (CLI), permitindo interações intuitivas com o robô.

## Funcionalidades

- **Interface de Usuário**: Uma interface de linha de comando (CLI) simples e intuitiva que permite ao usuário escolher diversas ações para o robô executar.
- **Controle do Robô**: O código oferece controle sobre o robo DOBOT Magician Lite, permitindo que ele execute várias tarefas, como retornar à posição inicial, ativar ou desativar atuadores, mover-se para diferentes posições e verificar a posição atual.

## Uso

1. **Instalação de Dependências**: Certifique-se de ter todas as dependências instaladas. Isso pode incluir bibliotecas Python específicas para o controle do robô e outras ferramentas necessárias para fazer tal coisa, basta digitar "npm install" no terminal do vscode ou da máquina (lembrando, deve-se digitar tal comando dentro da pasta "Ponderada-Sem3").
2. **Configuração da Conexão**: Ao iniciar o código, selecione no CLI a porta a qual o robo está conectado.
3. **Execução do Programa**: Execute o programa principal (Execute o mesmo através de python3/python src/main.py). Isso iniciará a interface de linha de comando (CLI) onde você poderá interagir com o robô, selecionando ações a serem executadas.
4. **Interagindo com o Robô**: Utilize as opções fornecidas na CLI para escolher ações específicas que você deseja que o robô execute. Por exemplo, você pode optar por movê-lo para uma determinada posição, ativar ou desativar um atuador, entre outras funcionalidades.

### Observacão
- Como orientado em sala, segue aqui, a função "move" do robo move o mesmo em todos os eixos de uma só vez, ou seja, caso deseje manter o mesmo y e z e apenas mudar x e r, basta colocar no em y e z os valores atuais do robo

### Vídeo demonstração

Segue no link a seguir um video de demonstração do robô, como requisitado na tarefa; https://drive.google.com/file/d/1lvChuA-N5-B2b-_QT6UehtpLPf51XCIj/view?usp=sharing

## Autor

Este código foi desenvolvido por Antonio Artimonte Vaz Guimarães.
