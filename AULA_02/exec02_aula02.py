# Se for executar no VSCode, executar:
# 1. Criar e ativar o ambiente virtual
# python ou python3 -m venv venv_robotica
# source venv_robotica/bin/activate     # No Linux
# venv_robotica\Scripts\activate        # No Windows
#
# 2. Instalar as dependências leves
# pip install pygame numpy

# Se for rodar no Colab, executar o código diretamente

import pygame
import math
import numpy as np

# Constantes de Configuração
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
COR_FUNDO = (30, 30, 30)
COR_ROBO = (0, 180, 255)
COR_DIRECAO = (255, 50, 50)
COR_TRAJETORIA = (100, 200, 100)
COR_INICIO = (255, 200, 0)

# Parâmetros da máquina de estados (malha aberta, controlada por tempo)
TEMPO_RETA = 2.0        # segundos andando em linha reta por lado
TEMPO_GIRO = 1.0        # segundos girando no proprio eixo
V_RETA = 60.0            # velocidade linear durante o trecho reto (px/s)
OMEGA_GIRO = math.pi / 2.0  # velocidade angular durante o giro (rad/s) -> 90 graus em 1s
NUM_LADOS = 4            # repete 4 vezes (quadrado)


class DiffDriveRobot:
    def __init__(self, x, y, theta=0.0, wheelbase=30.0, radius=15.0):
        # Estado do robô: [x, y, theta]
        self.x = float(x)
        self.y = float(y)
        self.theta = float(theta)  # em radianos

        # Parâmetros físicos (em pixels)
        self.L = float(wheelbase)  # Distância entre rodas
        self.radius = float(radius)

        # Entradas de controle
        self.v = 0.0      # Velocidade linear (pixels/s)
        self.omega = 0.0  # Velocidade angular (rad/s)

        # Histórico de posições para plotar rastro
        self.history = []

    def set_wheel_velocities(self, v_left, v_right):
        """Converte velocidade das rodas em velocidade linear e angular."""
        self.v = (v_right + v_left) / 2.0
        self.omega = (v_right - v_left) / self.L

    def set_direct_velocity(self, v, omega):
        """Comando direto de velocidade linear e angular (padrão cmd_vel)."""
        self.v = v
        self.omega = omega

    def update(self, dt):
        """Integração numérica da cinemática diferencial (odometria discreta)."""
        # Atualização angular
        self.theta += self.omega * dt
        # Normaliza o ângulo entre [-pi, pi]
        self.theta = (self.theta + math.pi) % (2 * math.pi) - math.pi

        # Atualização de posição cartesiana
        self.x += self.v * math.cos(self.theta) * dt
        self.y += self.v * math.sin(self.theta) * dt

        # Guarda histórico para desenhar o rastro
        if len(self.history) == 0 or np.hypot(self.x - self.history[-1][0], self.y - self.history[-1][1]) > 5:
            self.history.append((self.x, self.y))
            if len(self.history) > 1000:
                self.history.pop(0)

    def draw(self, surface):
        # 1. Desenha o rastro
        if len(self.history) > 1:
            pygame.draw.lines(surface, COR_TRAJETORIA, False, self.history, 2)

        # 2. Desenha o corpo do robô
        pos_int = (int(self.x), int(self.y))
        pygame.draw.circle(surface, COR_ROBO, pos_int, int(self.radius))

        # 3. Desenha a linha indicadora da direção (orientação theta)
        linha_frente_x = self.x + (self.radius + 10) * math.cos(self.theta)
        linha_frente_y = self.y + (self.radius + 10) * math.sin(self.theta)
        pygame.draw.line(surface, COR_DIRECAO, pos_int, (int(linha_frente_x), int(linha_frente_y)), 3)


class SquareStateMachine:
    """
    Máquina de estados simples, controlada por tempo (dt), que comanda o robô
    a percorrer um quadrado em malha aberta (open-loop), ou seja, sem realimentação
    da pose real do robô -- apenas alternando comandos fixos de v/omega por
    intervalos de tempo pré-definidos.

    Estados:
        RETA -> anda em linha reta por TEMPO_RETA segundos
        GIRO -> gira no proprio eixo por TEMPO_GIRO segundos
    Repete o par (RETA, GIRO) NUM_LADOS vezes e então finaliza.
    """

    RETA = "RETA"
    GIRO = "GIRO"
    FIM = "FIM"

    def __init__(self):
        self.estado = self.RETA
        self.temporizador = 0.0
        self.lado_atual = 1  # conta quantos lados já foram concluídos (1..NUM_LADOS)

    def update(self, robot, dt):
        """Atualiza a máquina de estados e aplica o comando de velocidade correspondente."""
        if self.estado == self.FIM:
            robot.set_direct_velocity(0.0, 0.0)
            return

        self.temporizador += dt

        if self.estado == self.RETA:
            robot.set_direct_velocity(V_RETA, 0.0)
            if self.temporizador >= TEMPO_RETA:
                self.estado = self.GIRO
                self.temporizador = 0.0

        elif self.estado == self.GIRO:
            robot.set_direct_velocity(0.0, OMEGA_GIRO)
            if self.temporizador >= TEMPO_GIRO:
                # Um lado do quadrado (reta + giro de 90 graus) foi concluído
                if self.lado_atual >= NUM_LADOS:
                    self.estado = self.FIM
                    robot.set_direct_velocity(0.0, 0.0)
                else:
                    self.lado_atual += 1
                    self.estado = self.RETA
                self.temporizador = 0.0

    def status_txt(self):
        if self.estado == self.FIM:
            return "Concluido (quadrado finalizado)"
        return f"{self.estado} | lado {self.lado_atual}/{NUM_LADOS} | t = {self.temporizador:.2f}s"


def main():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Aula 02 - Exercicio 2: Quadrado em Malha Aberta (Open-Loop)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 14)

    robot = DiffDriveRobot(x=LARGURA_TELA // 2, y=ALTURA_TELA // 2 + 100, theta=0.0)
    pos_inicial = (robot.x, robot.y)

    fsm = SquareStateMachine()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time em segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reinicia a demonstração (posição, rastro e máquina de estados)
                    robot = DiffDriveRobot(x=LARGURA_TELA // 2, y=ALTURA_TELA // 2 + 100, theta=0.0)
                    pos_inicial = (robot.x, robot.y)
                    fsm = SquareStateMachine()

        # A máquina de estados decide o comando de velocidade (sem intervenção manual)
        fsm.update(robot, dt)
        robot.update(dt)

        # Renderização
        screen.fill(COR_FUNDO)

        # Marca a posição/ponto inicial para comparação visual com a posição final
        pygame.draw.circle(screen, COR_INICIO, (int(pos_inicial[0]), int(pos_inicial[1])), 6, 1)

        robot.draw(screen)

        # Erro de fechamento do ciclo (distância entre pose final e pose inicial)
        erro_fechamento = math.hypot(robot.x - pos_inicial[0], robot.y - pos_inicial[1])

        info_txt = [
            f"Pose X: {robot.x:.1f} px | Y: {robot.y:.1f} px | Theta: {math.degrees(robot.theta):.1f} deg",
            f"Comandos: v = {robot.v:.1f} px/s | omega = {robot.omega:.2f} rad/s",
            f"Estado (FSM): {fsm.status_txt()}",
            f"Erro de fechamento (dist. ao ponto inicial): {erro_fechamento:.2f} px",
            "R = reiniciar demonstracao | Movimento 100% em malha aberta (sem correcao)",
        ]
        for i, txt in enumerate(info_txt):
            rendered = font.render(txt, True, (220, 220, 220))
            screen.blit(rendered, (15, 15 + i * 20))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
