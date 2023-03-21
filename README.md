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

## Funcionalidades / Teoria
O programa permite algumas funcionalidades para transformar a imagem, sendo elas:

- Rotacionar: inicialmente, a imagem está girando no sentido horário em determinada velocidade, mas é possível alterar a direção e a aceleração através do pressionamento da tecla **d** para aumentar a velocidade em sentido horário, e a tecla **a** em sentido anti-horário.
Tal funcionalidade foi implementada através de manipulações matriciais, sendo que começamos com uma matriz que representava os diversos pixels da câmera. Pré multiplicamos uma matriz transformação `[[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]]` (sendo heigth e width variáveis que representam o tamanho da tela utilizada) pela matriz incial (pixels da câmera) para que a imagem sofresse uma transladação para a origem do sitema (0,0), em seguida pré multipiclamos a matriz rotação `[[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]]` para girar a imagem, e por fim mandamos a imagem novamente para o centro da tela através da pré multiplicação da matriz inversa de `[[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]]`, tudo isso com o objetivo de rotacionar a imagem em relação ao seu centro. Quando clicamos nas teclas citadas anteriormente (**a** e **d**) alteramos o valor da variável 'ang' utilizada na rotação, interferindo diretamente no sentido e na velocidade de rotação da imagem, haja vista que tal variável está presente na matriz de rotação.

- Cisalhar: ao pressionar a tecla **c** é possível aplicar dois tipos de cisalhamento na imagem, isso acontece porque estamos pré multiplicando uma variavel 'cisalhamento', que inicia como uma matriz identidade, pela nossa matriz da imagem. Por ser uma matriz identidade, nada ocorre, mas quando o usuário pressiona a devida tecla, essa variável 'cisalhamento' é alterada para uma matriz transformação de cisalhamento ´[[1,0,0],[-1,1,0],[0,0,1]]` aplicando um cisalhamento para a esquerda, se pressionada novamente é alterada para `[[1,0,0],[1,1,0],[0,0,1]]´ aplicando um cisalhamento para a direita, e por fim, se pressionada novamente ela torna a ser uma matriz identidade e a imagem não apresenta mais cisalhamento.



Feito por: <a href= "https://github.com/fernandovs4"> Fernando Santos e <a href = "https://github.com/eriksoaress"> Erik Soares<a>


