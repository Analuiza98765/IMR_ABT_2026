# Resultados Aula 03

## Laboratório 1 - Raycasting e Percepção Sensorial

O código foi executado com sucesso no VS Code utilizando a biblioteca Pygame.

Foi possível observar o funcionamento de três sensores de distância (esquerda, frente e direita), que detectam obstáculos retangulares através da técnica de raycasting. As leituras dos sensores são atualizadas em tempo real conforme o robô se movimenta pelo ambiente.

### Print da execução

<img width="901" height="671" alt="Exercicio1" src="https://github.com/user-attachments/assets/68d2a8be-c7ca-4919-a180-4d24c0a7b25c" />



## Laboratório 2 — Rotação In-Place (180°)

Aqui o foco não foi a percepção, mas a cinemática angular pura. Calculamos o tempo necessário para girar 180° a partir de uma velocidade angular fixa (t = θ/ω) e fizemos o robô girar sobre o próprio eixo, sem se deslocar no espaço, até atingir esse ângulo. 
Ao final, um comando de velocidade zero é "publicado", simulando o encerramento do movimento em um sistema real de controle (como o tópico `/cmd_vel` em ROS). O resultado confirma que a posição (x, y) permanece constante enquanto apenas a orientação θ muda.

### Print da execução

<img width="896" height="680" alt="Captura de tela de 2026-08-31 20-08-27" src="https://github.com/user-attachments/assets/2653caec-6614-42d9-b5d2-4112c9d5f24a" />



## Laboratório 3 — Percepção com 5 sensores e ruído gaussiano

Evoluímos o modelo de sensores para 5 feixes (-60°, -30°, 0°, 30°, 60°), cobrindo um campo de visão mais amplo. Além disso, cada leitura recebe um ruído gaussiano (média 0, desvio-padrão 2.0), que imita a imprecisão de sensores reais como sonares e lasers. O resultado mostra que as distâncias lidas variam ligeiramente a cada quadro, mesmo com o robô parado, o que é
esperado em qualquer sensor físico.


### Print da execução

<img width="903" height="677" alt="Captura de tela de 2026-08-31 20-15-00" src="https://github.com/user-attachments/assets/2bfbf8f8-6b91-442e-8cfe-7088e6da5993" />



## Laboratório 4 — Veículo de Braitenberg (medo puro)

Este foi o primeiro exercício em que o robô se move sozinho, sem nenhum alvo definido, apenas reagindo aos sensores. A lei de desvio diferencial faz a roda esquerda acelerar quando há um obstáculo à direita, e vice-versa, o que faz o robô "fugir" naturalmente das paredes e obstáculos da sala. 

Um caso especial cuida do sensor frontal: se ele detectar algo muito perto, o robô gira rapidamente no próprio eixo em vez de tentar desviar suavemente. O comportamento observado lembra um inseto simples que se afasta de ameaças sem nunca ter um "mapa" da sala — exatamente a ideia central dos veículos de Braitenberg.


## Print da execução 

<img width="901" height="674" alt="Captura de tela de 2026-08-31 20-20-18" src="https://github.com/user-attachments/assets/0e4eba64-b9d5-42cc-88cb-48d287225880" />



## Laboratório 5 — Go-to-Goal com desvio reativo

Este laboratório combina os dois comportamentos anteriores: atração a um alvo (ponto clicado com o mouse) e repulsão a obstáculos. Quando o caminho está livre, um controlador proporcional gira o robô na direção do alvo. Se um sensor detecta um obstáculo muito próximo, esse comportamento é temporariamente sobreposto por um "torque" repulsivo calculado a partir da diferença de proximidade entre os sensores esquerdo e direito. Assim que o caminho volta a ficar livre, o robô automaticamente retoma a perseguição do alvo, parando quando chega perto o suficiente dele.


## Print da execução 

<img width="898" height="675" alt="Captura de tela de 2026-08-31 20-24-00" src="https://github.com/user-attachments/assets/afb4baa3-8482-46c3-b49b-489cf2224216" />



### 2. Exercício de maior dificuldade de compreensão

O **Laboratório 5 (Go-to-Goal com desvio)** foi o mais difícil de entender e
implementar corretamente. A dificuldade principal está em combinar dois
comportamentos que competem entre si — "ir até o alvo" e "fugir do
obstáculo" — sem que um atrapalhe o outro. Foi preciso pensar em como
alternar entre os dois modos (atração vs. repulsão) de forma suave, e como
calcular corretamente o erro angular entre a orientação atual do robô e a
direção do alvo, normalizando o ângulo para o intervalo correto
(usando `atan2` do seno e cosseno da diferença, em vez de uma subtração
direta que poderia gerar saltos incorretos perto de ±180°). Entender por que
essa normalização é necessária exigiu revisar com calma o conceito de erro
angular em coordenadas polares.

### 3. Impressões gerais sobre as dificuldades técnicas até o momento

Até este ponto, a maior dificuldade tem sido sair do raciocínio de
"programar uma sequência de comandos" e passar a pensar em termos de
**malha fechada**: o robô lê o ambiente, decide e age continuamente, quadro
a quadro, sem um roteiro fixo. Os conceitos de cinemática diferencial
(transformar `v` e `ω` em velocidades de roda `vL` e `vR`, e vice-versa)
também exigiram atenção redobrada, pois pequenos erros de sinal nas fórmulas
fazem o robô girar para o lado errado. Por fim, entender o papel do ruído
gaussiano nos sensores ajudou a perceber que, em robótica real, nenhuma
leitura é perfeita — o que reforça a importância de sistemas de controle
tolerantes a pequenas variações, tema que deve ser aprofundado nas próximas
aulas.
