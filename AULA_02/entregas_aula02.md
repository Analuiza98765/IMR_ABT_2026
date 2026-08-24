Resumo — Fundamentos de Robótica Móvel

Nessa aula vimos alguns conceitos básicos de robótica móvel, principalmente como representar a posição de um robô, como ele se movimenta e como podemos fazer ele chegar até um determinado objetivo.

Primeiro, aprendemos sobre a pose 2D, que representa o estado do robô no plano. Ela é formada por x, y e theta. O x e o y representam a posição do robô, enquanto o theta representa para qual direção ele está virado. Essas informações são importantes porque com elas conseguimos saber onde o robô está e também calcular como ele deve se movimentar.

Depois vimos a cinemática diferencial, que é o modelo usado para um robô com duas rodas independentes. A velocidade das duas rodas define tanto a velocidade que o robô anda quanto a velocidade que ele gira. Quando as rodas estão com velocidades diferentes, o robô faz uma curva, e quando estão iguais ele anda mais reto. Uma coisa importante é que ele não consegue simplesmente andar de lado, ele precisa mudar sua orientação primeiro.

Também estudamos a odometria, que é uma forma de estimar a posição do robô conforme ele vai se movimentando. A cada pequeno intervalo de tempo (dt), o sistema atualiza x, y e theta de acordo com as velocidades do robô. No código isso é feito usando integração de Euler. O problema é que pequenos erros vão se acumulando com o tempo, causando o chamado drift, então a posição calculada pode acabar ficando um pouco diferente da posição real.

No exercício do quadrado, o robô andava em linha reta por um determinado tempo e depois fazia um giro de 90 graus. Esse processo era repetido quatro vezes. Esse controle é chamado de malha aberta, porque o robô não verifica onde realmente está, ele apenas segue os comandos baseados no tempo. Por isso, na prática, ele provavelmente não consegue terminar exatamente no mesmo ponto onde começou. Pequenos erros no tempo, no giro e na integração acabam se acumulando durante o percurso.

Por fim, vimos o Go-To-Goal, que é uma forma mais inteligente de controlar o robô para chegar até um ponto escolhido. Nesse caso é usado um controlador proporcional, que calcula a distância entre o robô e o alvo e também o quanto ele precisa girar para ficar apontado na direção correta. Quanto mais longe do objetivo, maior pode ser a velocidade, e quanto mais desalinhado, maior será o giro. Quando ele chega perto o suficiente do alvo, para automaticamente.

No geral, a aula mostrou que controlar um robô não é só mandar ele andar, mas também saber onde ele está, para onde está indo e corrigir os erros durante o movimento. A diferença entre o quadrado em malha aberta e o Go-To-Goal mostra bem isso, já que o segundo consegue usar as informações do próprio robô para fazer correções durante o caminho.
