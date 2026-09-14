## Exercício 1 — lab1_pose.py
Aplica a sequência de comandos (v, ω) em malha aberta, calcula a Pose final
teórica por integração analítica do modelo unicycle e simula o movimento
no Pygame (integração numérica). Ao final imprime no terminal a Pose
teórica, a Pose simulada e o erro entre elas.
Print da execução:
<img width="903" height="622" alt="image" src="https://github.com/user-attachments/assets/3a45b7c0-ad7b-4137-aaa5-82fe0d4c7502" />

## Exercício 2 — lab2_ackermann.py
Setas ↑/↓ controlam v, ←/→ controlam o ângulo de esterço φ (limitado a
±30°). Mostra ω = (v/L)·tan(φ) e R = L/tan(φ) em tempo real, comparando
com um robô diferencial (tecla `G` demonstra giro no próprio eixo, R = 0,
algo impossível para o Ackermann).
Print da execução:
<img width="894" height="675" alt="image" src="https://github.com/user-attachments/assets/3b94da6c-460f-4eae-83c0-b1ac127e6d7a" />

## Exercício 3 — lab3_sensor_filter.py
Varredura de 7 feixes em 180° com ruído gaussiano N(0, 5.0). Mostra lado
a lado, para cada feixe, a leitura bruta e a leitura após o filtro de
limiar (descarta < 10 px, crava em 200 px acima do alcance máximo).
Print da execução:
<img width="953" height="672" alt="image" src="https://github.com/user-attachments/assets/0a666302-35ec-45c6-9919-51dcd53d947b" />

## Exercício 4 — lab4_braitenberg.py
Conexões diretas (sensor esquerdo→roda esquerda, sensor direito→roda
direita). Ao aproximar-se de um obstáculo à direita, a roda direita
acelera e o robô vira PARA o obstáculo (atração/agressão). Arraste o
obstáculo com o botão esquerdo do mouse.
Print da execução:
<img width="902" height="678" alt="image" src="https://github.com/user-attachments/assets/5413fadb-cd8b-4532-a495-834c89cb6b9c" />

## Exercício 5 — ex5_corridor.py
Corredor com duas paredes paralelas e dois feixes laterais fixos a ±90°.
Controle proporcional ω = Kp·e, com e = d_esq − d_dir e Kp = 0.01,
mantendo v = 40 px/s constante. O robô inicia desalinhado e se
autocorrige até o centro do corredor.
Print da execução:
<img width="952" height="523" alt="image" src="https://github.com/user-attachments/assets/9d24b2b3-d465-4e8d-bcea-c58940a6a818" />



