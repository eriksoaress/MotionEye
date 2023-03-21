# MotionEye
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/EyeMotion.jpeg">
MotionEye é um programa que busca criar um vídeo interativo para o usuário através de transformações na imagem da câmera ao vivo do usuário.

## Instalação
Para utilizar o programa basta clonar esse repositório em algum local de sua máquina. Para fazer isso, clique no botão verde **"Code"** logo acima, escolha um modo de baixar o repositório, podendo ser baixando o zip e descompactando ou clonando através de https ou ssh. Após seguir essas estapas, será necessário instalar as bibliotecas necessárias. Isso pode ser feito, estando na raiz do projeto, rodando no terminal o seguinte comando:  `pip install -r requirements.txt `( se estiver rodando no sistema operacional Linux, será necessário rodar com permissões de administrador para instalar a biblioteca keyboard) , com isso, as bibliotecas necessárias serão instaladas. Com a instalação feita e na pasta raiz do projeto, basta executar o seguinte comando para rodar o programa: `python  .\main.py `( ou `python3 .\main.py`, dependendo da sua versão instalada do python). A imagens abaixo mostra os passos citados acima:
<p>Code:</p>
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/code.jpeg">
<p>Clonando ou baixando o zip</p>
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/clone.jpeg">



Após realizar todos os passos acima, a sua câmera será aberta e o vídeo começará a ser gravado, e salvo assim que você executar o comando para fechar o programa.

## Equacões aplicadas 
O programa permite a funcionalidade de rotacionar e de cisalhar. Para isso, foi utilizado as seguintes matrizes:

Criou se uma matriz de rotação R:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/rotacao.jpeg">

Uma matriz de translação T:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/translacao.jpeg">
Em T, heigth e width representam, respectivamente, a altura e largura da tela utilizada para a gravação.

Duas matrizes de cisalhamento  C e uma matriz identidade, também representada pela letra C:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/cisalhar.jpeg">


Começamos com uma matriz Xd que representa  os diversos pixels da câmera. Multiplicamos a matriz  T por Xd, para que a imagem sofresse uma translação para a origem do sitema (0,0),obtendo uma matriz M, como mostrado abaixo:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/matrizXd.jpeg">


Em seguida, multiplicamos R por M,com o fito de rotacionar a matriz M, obtendo a matriz N:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/matrizN.jpeg">


Nessa etapa, multiplicamos a matriz  C ( essa matriz pode ser de cisalhamento ou identidade) pela matriz N chegando em uma matriz L:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/matrizL.jpeg">


Para, enfim, voltarmos com a matriz L para o centro da tela. Para isso, multiplicamos a matriz inversa de T (I) pela matriz L, obtendo Q:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/matrizQ.jpeg">


Com isso, coseguimos o efeito que queremos, que é conseguir rotacionar a imagem no centro da tela e, ainda, aplicar cisalhamentos na imagem.

Por fim, nossa matriz Q, que será usada para mostrar a imagem com as rotações e cisalhamentos pode ser escrita como:
<img src= "https://github.com/eriksoaress/MotionEye/blob/main/multiplicacoes%20totais.jpeg">


## Funcionalidades 


O programa permite algumas funcionalidades para transformar a imagem, sendo elas:

- Rotacionar: inicialmente, a imagem está girando no sentido horário em determinada velocidade, mas é possível alterar a direção e a aceleração através do pressionamento da tecla **d** para aumentar a velocidade em sentido horário, e a tecla **a** em sentido anti-horário.Quando clicamos nas teclas citadas anteriormente (**a** e **d**) alteramos o valor da variável 'ang' utilizada na rotação, interferindo diretamente no sentido e na velocidade de rotação da imagem.

- Cisalhar: ao pressionar a tecla **c** é possível aplicar dois tipos de cisalhamento na imagem, isso acontece porque estamos multiplicando uma variavel 'cisalhamento', que inicia como uma matriz identidade, pela matriz N. Por ser uma matriz identidade, nada ocorre, mas quando o usuário pressiona a devida tecla, essa variável 'cisalhamento' é alterada para uma matriz transformação de cisalhamento `[[1,0,0],[-1,1,0],[0,0,1]]` aplicando um cisalhamento para a esquerda, se pressionada novamente é alterada para `[[1,0,0],[1,1,0],[0,0,1]]` aplicando um cisalhamento para a direita, e por fim, se pressionada novamente ela torna a ser uma matriz identidade e a imagem não apresenta mais cisalhamento.


Feito por: <a href= "https://github.com/fernandovs4"> Fernando Santos e <a href = "https://github.com/eriksoaress"> Erik Soares<a>


