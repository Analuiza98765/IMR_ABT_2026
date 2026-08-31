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

Para o nosso grupo, o Laboratório 5, que aborda a navegação Go-to-Goal com desvio de obstáculos, foi a atividade que apresentou o maior nível de dificuldade. O principal desafio foi compreender como integrar dois comportamentos diferentes no mesmo sistema; o deslocamento em direção ao objetivo e a reação de desvio quando um obstáculo é detectado. Após realizar diversos testes e analisar o comportamento do simulador, conseguimos compreender melhor como esses cálculos influenciam diretamente a tomada de decisão do robô. 

### 3. Impressões gerais sobre as dificuldades técnicas até o momento

Até o momento, a principal dificuldade do grupo tem sido compreender a lógica de funcionamento dos sistemas robóticos, que precisam analisar o ambiente e tomar decisões continuamente. Além disso, a cinemática diferencial exigiu bastante atenção, principalmente para entender a relação entre as velocidades do robô e das rodas. As simulações também mostraram a influência do ruído nos sensores, destacando a importância de desenvolver sistemas capazes de lidar com pequenas imprecisões. Esses desafios têm contribuído para ampliar nossa compreensão sobre os conceitos de robótica estudados em aula.
