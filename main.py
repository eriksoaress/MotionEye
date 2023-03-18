import numpy as np
import cv2 as cv
import itertools



sentido_horario = True
def criar_indices(min_i, max_i, min_j, max_j):
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack((idx_i, idx_j))
    return idx

def run():
   def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack((idx_i, idx_j))
    return idx

def run():
    cap = cv.VideoCapture(0)
    width = 320
    height = 240
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    ang = 5
    inc = 0
      # Cria uma matriz de translação que desloca o centro da imagem para a origem
    trans1 = np.array([[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]])
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = np.array(frame).astype(float) / 255

          # Define o ângulo de rotação
    

     

        # Cria uma matriz de rotação
        rot = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])

        # Cria uma matriz de translação que desloca o centro de volta para a posição original
        trans2 = np.array([[1, 0, width/2], [0, 1, height/2], [0, 0, 1]])

        Xd = criar_indices(0, height, 0, width)
        Xd = np.vstack((Xd, np.ones(Xd.shape[1])))
        X = np.linalg.inv(trans1)@rot@trans1@Xd
        filtro = (X[0, :] < image.shape[0]-1) & (X[0, :] >= 0) & (X[1, :] < image.shape[1]-1) & (X[1, :] >= 0)
        X = X[:, filtro]
        Xd = Xd[:, filtro]
        Xd = Xd.astype(int)
        X = X.astype(int)
        image_ = np.zeros(image.shape)
        image_[Xd[0, :], Xd[1, :], :] = image[X[0, :], X[1, :], :]


        cv.imshow('Minha Imagem!', image_)
        
        if cv.waitKey(1) == ord('q'):
            break
        ang += 0.1 + inc
        

        #altera a velocidade da rotação pelas setas do teclado
        if cv.waitKey(1) == ord('d'):
            inc += 0.1
            
            print(ang)
        if cv.waitKey(1) == ord('a'):
            inc -= 0.1
        

    cap.release()
    cv.destroyAllWindows()

run()
