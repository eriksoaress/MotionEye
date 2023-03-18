import numpy as np
import cv2 as cv
import itertools
import keyboard
import time
import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()
# Carrega a música a ser reproduzida
pygame.mixer.music.load("trilha.mp3")
# Inicia a reprodução da música em loop infinito
pygame.mixer.music.play(-1)


# Função para criar índices para a matriz de transformação
def criar_indices(min_i, max_i, min_j, max_j):
    # Cria uma lista com todas as combinações possíveis de índices
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    # Separa os índices das linhas em um array e os das colunas em outro array
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    # Empilha os arrays de índices em uma matriz (2xN)
    idx = np.vstack((idx_i, idx_j))
    return idx

# Função principal que roda o programa
def run():
    # Abre a câmera
    cap = cv.VideoCapture(0)
    # Define a largura e altura desejadas para o vídeo
    width = 320
    height = 240
    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Cria uma matriz de cisalhamento
    cisalhamento = np.array([[1,0,0],[0,1,0],[0,0,1]])

    # Define a variável transf_cis como 0
    transf_cis = 0
    # Define o ângulo inicial de rotação como 0
    ang = 5
    # Define o incremento inicial como 0
    inc = 0

    # Cria uma matriz de translação que desloca o centro da imagem para a origem
    trans1 = np.array([[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]])

    # Cria um objeto VideoWriter para gravar o vídeo resultante
    out = cv.VideoWriter('rotating_video.avi', cv.VideoWriter_fourcc(*'XVID'), 30, (width,height))

    # Loop principal
    while True:
        # Lê um frame da câmera
        ret, frame = cap.read()
        # Verifica se o frame foi lido corretamente
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Redimensiona o frame para a largura e altura desejadas
        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        # Converte o frame para uma matriz numpy de ponto flutuante no intervalo [0,1]
        image = np.array(frame).astype(float) / 255

        # Cria uma matriz de rotação
        rot = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
       

        Xd = criar_indices(0, height, 0, width)
        Xd = np.vstack((Xd, np.ones(Xd.shape[1])))
         # Cria uma matriz de transformação composta por translação, cisalhamento, rotação e translação inversa
        X = np.linalg.inv(trans1)@cisalhamento@rot@trans1@Xd
        # Cria um filtro para remover os pontos fora da imagem
        filtro = (X[0, :] < image.shape[0]-1) & (X[0, :] >= 0) & (X[1, :] < image.shape[1]-1) & (X[1, :] >= 0)
        # Aplica o filtro
        X = X[:, filtro]
        Xd = Xd[:, filtro]
        # Converte os pontos para inteiros
        Xd = Xd.astype(int)
        X = X.astype(int)
       # Cria uma imagem preta
        image_ = np.zeros(image.shape)
        #  Atribui os valores dos pixels da imagem original para a imagem de saída
        image_[Xd[0, :], Xd[1, :], :] = image[X[0, :], X[1, :], :]
        image_ = cv.convertScaleAbs(image_ * 255)  # converte para 8 bits
        # Grava o frame no arquivo de vídeo
        out.write(image_)  
        # Mostra a imagem 
        cv.imshow('Minha Imagem!', image_)
        # Verifica se o usuário pressionou a tecla 'q'
        if cv.waitKey(1) == ord('q'):
            break
        # Atualiza o ângulo da rotação
        ang += 0.1 + inc
        

        #altera a velocidade da rotação pelas setas do teclado
        K = cv.waitKey(1)
        if K == ord('d'):
            inc += 0.1
        if K == ord('a'):
            inc -= 0.1
         # Altera o tipo de cisalhamento ao pressionar a tecla 'c'
        if keyboard.is_pressed('c'):
            time.sleep(0.1)
            # Verifica o valor da variável transf_cis e altera a variável cisalhamento
            if transf_cis == 0:
                cisalhamento = np.array([[1,0,0],[-1,1,0],[0,0,1]])
                transf_cis = 1
            elif transf_cis == 1:
                cisalhamento = np.array([[1,0,0],[1,1,0],[0,0,1]])
                transf_cis = 2
            else:
                cisalhamento = np.array([[1,0,0],[0,1,0],[0,0,1]])
                transf_cis = 0
        
    # Libera a câmera e fecha todas as janelas
    cap.release()
    cv.destroyAllWindows()
    # Fecha o arquivo de vídeo
    out.release()


if __name__ == '__main__':
    run()
