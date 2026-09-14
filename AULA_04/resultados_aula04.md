## Exercício 1 — lab1_pose.py
Nesse exercício, o robô recebe comandos de velocidade linear e angular em malha aberta. Primeiro, é calculada a pose final esperada usando a integração analítica do modelo unicycle. Depois, o movimento é simulado no Pygame usando integração numérica. Assim, o programa mostra no terminal a pose teórica, a pose simulada e a diferença entre elas.
Print da execução:
<img width="903" height="622" alt="image" src="https://github.com/user-attachments/assets/3a45b7c0-ad7b-4137-aaa5-82fe0d4c7502" />

## Exercício 2 — lab2_ackermann.py
Aqui é trabalhado o modelo de direção Ackermann. As setas ↑ e ↓ controlam a velocidade do robô, enquanto ← e → controlam o ângulo de esterço, que pode chegar a ±30°. Durante a movimentação, são mostrados os valores de velocidade angular e raio de curva. A tecla G também permite comparar com um robô diferencial, que consegue girar parado no próprio eixo, algo que o Ackermann não consegue fazer.
Print da execução:
<img width="894" height="675" alt="image" src="https://github.com/user-attachments/assets/3b94da6c-460f-4eae-83c0-b1ac127e6d7a" />

## Exercício 3 — lab3_sensor_filter.py
o robô utiliza 7 sensores distribuídos em uma área de 180°. As leituras recebem um ruído gaussiano para simular um sensor real. Depois, é aplicado um filtro que elimina valores muito baixos e limita os valores que ultrapassam o alcance máximo. Assim, é possível comparar as leituras originais com as leituras filtradas.
Print da execução:
<img width="953" height="672" alt="image" src="https://github.com/user-attachments/assets/0a666302-35ec-45c6-9919-51dcd53d947b" />

## Exercício 4 — lab4_braitenberg.py
O robô possui dois sensores ligados diretamente às suas respectivas rodas. Quando ele se aproxima de um obstáculo pelo lado direito, a roda direita acelera e faz o robô virar em direção ao obstáculo. Esse comportamento mostra uma reação de atração ou agressão. Na simulação, o obstáculo também pode ser movimentado com o mouse.
Print da execução:
<img width="902" height="678" alt="image" src="https://github.com/user-attachments/assets/5413fadb-cd8b-4532-a495-834c89cb6b9c" />

## Exercício 5 — ex5_corridor.py
Por fim, o robô começa desalinhado e corrige sua trajetória automaticamente até se alinhar ao centro do corredor. Dois sensores laterais medem as distâncias até as paredes e, a partir da diferença entre essas medidas. 
Print da execução:
<img width="952" height="523" alt="image" src="https://github.com/user-attachments/assets/9d24b2b3-d465-4e8d-bcea-c58940a6a818" />



