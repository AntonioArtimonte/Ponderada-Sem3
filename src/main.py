# Importando bibliotecas
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin

# Classe para mover o robo com as juntas
class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def movel_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

        


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
    robo.movej_to(240, 0, 150, 0, wait=True)
    spinner.stop()

# Função para ligar o atuador do robo
def turn_actuator_on():
    print("Ligando o atuador...")
    spinner.start()
    robo.suck(True)
    robo.wait(200)
    spinner.stop()
    

# Função para desligar o atuador do robo
def turn_actuator_off():
    print("Desligando o atuador...")
    spinner.start()
    robo.suck(False)
    robo.wait(200)
    spinner.stop()

# Função para mover o robo para uma posição
def move(x, y, z, r):
    spinner.start()
    print(f"Se movendo para a posição: ({x}, {y}, {z}), rotação: {r}")
    robo.movej_to(x, y, z, r, wait=True)
    spinner.stop()
    print(f"Movimento para a posição: ({x}, {y}, {z}), rotação: {r} concluído!")

# Função para mover o robo em apenas um eixo
def move_axis(axis, value):
    pos = robo.pose()
    spinner.start()
    print(f"Se movendo no eixo {axis} para a posição: {value}")
    if axis == "X":
        print(pos[0] + value, pos[1], pos[2], pos[3])
        robo.move_to(pos[0] + value, pos[1], pos[2], pos[3], wait=True)
    elif axis == "Y":
        robo.move_to(pos[0], pos[1] + value, pos[2], pos[3], wait=True)
    elif axis == "Z":
        robo.move_to(pos[0], pos[1], pos[2] + value, pos[3], wait=True)
    elif axis == "R":
        robo.move_to(pos[0], pos[1], pos[2], pos[3] + value, wait=True)
    spinner.stop()
    print(f"Movimento no eixo {axis} para a posição: {value} concluído!")

# Função para pegar a posição atual do robo
def position():
    print("Posição atual: ...")
    current_pose = robo.pose()
    print(f"Posição atual: X: {current_pose[0]}, Y: {current_pose[1]}, Z: {current_pose[2]}, Rotação: {current_pose[3]}")
    return current_pose

# Dicíonario de funções para as ações do robo
action_functions = {
    "Home": go_home,
    "Ligar atuador": turn_actuator_on,
    "Desligar atuador": turn_actuator_off,
    "Mover": move,
    "Mover em um eixo": move_axis,
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
        inquirer.List("act", message="Escolha a ação", choices=["Home", "Ligar atuador", "Desligar atuador", "Mover", "Mover em um eixo" , "Posição atual", "Sair"])
    ])
    action_name = action["act"]
    if action_name == "Mover":
        return action_name, get_move_params()
    elif action_name == "Mover em um eixo":
        axis = inquirer.prompt([
            inquirer.List("axis", message="Escolha o eixo", choices=["X", "Y", "Z", "R"])
        ])["axis"]
        value = float(input(f"Digite o valor para o eixo {axis}: "))
        return action_name, (axis, value)
    else:
        return action_name, None

# Adquirir a porta serial escolhida
port = get_port()

robo = InteliArm(port=port, verbose=False)
robo.speed(200, 200)

# Loop para pegar as ações escolhidas
while True:
    chosen_action, action_params = get_action()
    if chosen_action in action_functions:
        if chosen_action == "Sair":
            robo.close()
            break
        elif action_params:
            action_functions[chosen_action](*action_params)
        else:
            action_functions[chosen_action]()
    else:
        print("Ação inválida")
        