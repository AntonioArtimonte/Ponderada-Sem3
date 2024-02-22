# Importando bibliotecas
from serial.tools import list_ports
import time
import inquirer
from yaspin import yaspin

# Declarando o spinner
spinner = yaspin(text="Movimentando...", color="yellow")

# Variavel para guardar as portas disponiveis
available_ports = list_ports.comports()

# Adquirir a porta serial escolhida
def get_port():
    porta_escolhida = inquirer.prompt([
        inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
    ])["porta"]
    print(f"Porta escolhida: {porta_escolhida}")
    return porta_escolhida

# Função para robo voltar para a posição inicial
def go_home():
    print("Voltando para posição inicial...")
    spinner.start()
    #robo.home()
    spinner.stop()

# Função para ligar o atuador do robo
def turn_actuator_on():
    print("Ligando o atuador...")
    spinner.start()
    #robo.suck(True)
    #robo.wait(200)
    spinner.stop()
    

# Função para desligar o atuador do robo
def turn_actuator_off():
    print("Desligando o atuador...")
    spinner.start()
    #robo.suck(False)
    #robo.wait(200)
    spinner.stop()

# Função para mover o robo para uma posição
def move(x, y, z, r):
    spinner.start()
    print(f"Se movendo para a posição: ({x}, {y}, {z}), rotação: {r}")
    #robo.move_to(x, y, z, r, wait=True)
    spinner.stop()
    print(f"Movimento para a posição: ({x}, {y}, {z}), rotação: {r} concluído!")
    time.sleep(2)  

# Função para pegar a posição atual do robo
def position():
    print("Posição atual: ...")
    spinner.start()
    #posicao = robo.pose()
    #print(f"Current Pose: X: {current_pose[0]}, Y: {current_pose[1]}, Z: {current_pose[2]}, Rotation: {current_pose[3]}")
    spinner.stop()

# Dicíonario de funções para as ações do robo
action_functions = {
    "Home": go_home,
    "Ligar atuador": turn_actuator_on,
    "Desligar atuador": turn_actuator_off,
    "Mover": move,
    "Posição atual": position,
    "Sair": exit
}

# Função para pegar os parametros de movimento do robo
def get_move_params():
    questions = [
        inquirer.Text("x", message="Enter X"),
        inquirer.Text("y", message="Enter Y"),
        inquirer.Text("z", message="Enter Z"),
        inquirer.Text("r", message="Enter R")
    ]
    answers = inquirer.prompt(questions)
    x = float(answers["x"])
    y = float(answers["y"])
    z = float(answers["z"])
    r = float(answers["r"])
    return x, y, z, r

# Função para pegar a ação escolhida
def get_action():
    action = inquirer.prompt([
        inquirer.List("act", message="Escolha a ação", choices=["Home", "Ligar atuador", "Desligar atuador", "Mover", "Posição atual", "Sair"])
    ])
    action_name = action["act"]
    if action_name == "Mover":
        return action_name, get_move_params()
    else:
        return action_name, None

# Adquirir a porta serial escolhida
port = get_port()

#robo = pydobot.Dobot(port=port, verbose=False)
#robo.speed(30, 30)

# Loop para pegar as ações escolhidas
while True:
    chosen_action, action_params = get_action()
    if chosen_action in action_functions:
        if chosen_action == "Sair":
            break
        elif action_params:
            action_functions[chosen_action](*action_params)
        else:
            action_functions[chosen_action]()
    else:
        print("Ação inválida")
