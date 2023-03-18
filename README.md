# MotionEye
MotionEye é um programa que busca criar um vídeo interativo para o usuário através de transformações na imagem da câmera ao vivo do usuário.

Para utilizar o programa basta clonar esse repositório em algum local de sua máquina, acessá-lo e executar no terminal o seguinte comando: python .\main.py

Após isso, a sua câmera será aberta e o vídeo começará a ser gravado, e salvo assim que você executar o comando para fechar o programa.

O programa permite algumas funcionalidades para transformar a imagem, sendo elas:
- Rotacionar: inicialmente, a imagem está girando no sentido horário em determinada velocidade, mas é possível alterar a direção e a aceleração através do pressionamento da tecla D para aumentar a velocidade em sentido horário, e a tecla A em sentido anti-horário.
- Tal funcionalidade foi implementada através de manipulações matriciais, sendo que começamos com uma matriz que representava os diversos pixels da câmera. Multiplicamos uma matriz transformação [[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]] pela matriz incial para que a imagem sofresse uma transladação para a origem, em seguida multipiclamos a matriz rotação [[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]], e por fim mandamos a imagem novamente para o centro da tela, tudo isso com o objetivo de rotacionar a imagem em relação ao seu centro.

- Cisalhar: ao pressionar a tecla C é possível aplicar dois tipos de cisalhamento na imagem, isso acontece porque estamos multiplicando uma variavel 'cisalhamento', que inicia como uma matriz identidade, e é alterada para uma matriz transformação de cisalhamento quando o usuário pressionar a devida tecla pela nossa matriz da imagem.

-Alteração de cores: também é possível alterar as cores da imagem através 