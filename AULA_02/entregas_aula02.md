Resumo dos Códigos — Robótica Móvel
Código 1 — Controle por Rodas

O primeiro código simula um robô com duas rodas independentes usando pygame.

A classe DiffDriveRobot controla:

x e y: posição do robô;
theta: direção do robô;
v: velocidade linear;
omega: velocidade angular.

As teclas controlam cada roda:

W/S: roda esquerda;
I/K: roda direita.

A função set_wheel_velocities() transforma a velocidade das rodas em velocidade linear e angular. A função update() atualiza a posição e a direção do robô usando a cinemática diferencial.

O código também desenha o robô, sua direção e o rastro do caminho.

Código 2 — Quadrado em Malha Aberta

O segundo código faz o robô percorrer um quadrado automaticamente.

Ele utiliza uma máquina de estados:

RETA: anda para frente por 2 segundos;
GIRO: gira 90° por 1 segundo;
FIM: encerra o movimento.

O processo é repetido 4 vezes.

Esse controle é de malha aberta, pois o robô não verifica sua posição para corrigir possíveis erros. Por isso, pequenas diferenças na velocidade, no tempo ou na integração podem causar um erro no final do quadrado.

O programa calcula o erro de fechamento, que é a distância entre o ponto inicial e o ponto final.

Código 3 — Go-To-Goal

O terceiro código usa um controlador proporcional (P-Controller) para levar o robô até um ponto escolhido com o mouse.

O controlador calcula:

rho: distância até o alvo;
alpha: erro entre a direção atual e a direção do alvo.

Depois calcula as velocidades:

v = KP_LINEAR * rho
omega = KP_ANGULAR * alpha


Quanto mais longe o robô estiver, mais rápido ele anda. Quanto maior o erro de direção, mais ele gira.

Quando chega próximo do alvo, o robô para automaticamente.

Diferente do código 2, esse sistema utiliza malha fechada, pois verifica constantemente a posição do robô e corrige seu movimento.

Conclusão

Os três códigos mostram uma evolução do controle:

Código 1 → controle manual das rodas
Código 2 → movimento automático em malha aberta
Código 3 → navegação automática em malha fechada
