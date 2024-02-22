
# Importando as bibliotecas
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin

# Declarando o spinner do yaspin
spinner = yaspin(text="Movimentando...", color="yellow")

# Variável para guardar as portas disponíveis
available_ports = list_ports.comports()

# Função para adquirir a porta serial e retornar a escolhida
def get_port():
    porta_escolhida = inquirer.prompt([
        inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
    ])["porta"]
    print(f"Porta escolhida: {porta_escolhida}")
    return porta_escolhida

# Função para o robo voltar a home
def go_home():
    print("Voltando para a posição home...")

# Função para ligar o atuador
def turn_actuator_on():
    print("Ligando o atuador...")

# Função para desligar o atuador
def turn_actuator_off():
    print("Desligando o atuador...")

# Função para mover o robo para a respectiva posição
def move(x, y, z, r):
    # Iniciar o spinner
    spinner.start()
    print(f"Se movendo para a posição: ({x}, {y}, {z}), rotação: {r}")
    # Parar de mover o spinner quando o robo chegar ao local
    spinner.stop()

# Função para pegar a posição atual do robo
def position():
    print("Posição atual: ...")

# Dicionário para guardar as funções de cada ação
action_functions = {
    "Home": go_home,
    "Ligar atuador": turn_actuator_on,
    "Desligar atuador": turn_actuator_off,
    "Mover": move,
    "Posição atual": position
}

# Função para o input dos parametros caso a ação selecionada foi a de mover o robo
def get_move_params():
    questions = [
        inquirer.Text("x", message="Digite X"),
        inquirer.Text("y", message="Digite Y"),
        inquirer.Text("z", message="Digite Z"),
        inquirer.Text("r", message="Digite R")
    ]
    answers = inquirer.prompt(questions)
    x = float(answers["x"])
    y = float(answers["y"])
    z = float(answers["z"])
    r = float(answers["r"])
    return x, y, z, r

# Função para pegar a ação que o usuário deseja realizar
def get_action():
    # Prompt do inquirer
    action = inquirer.prompt([
        inquirer.List("act", message="Escolha a ação a ser executada", choices=["Home", "Ligar atuador", "Desligar atuador", "Mover", "Posição atual"])
    ])
    action_name = action["act"]
    if action_name == "Mover":
        return action_name, get_move_params()
    else:
        return action_name, None

# Adicionar a porta ao robo
port = get_port()
# robo = pydobot.Dobot(port=port, verbose=False)

# Se a ação não existir
chosen_action, action_params = get_action()
if chosen_action in action_functions:
    if action_params:
        action_functions[chosen_action](*action_params)
    else:
        action_functions[chosen_action]()
else:
    print("Ação inválida")

# robo.close()
