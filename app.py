import cv2
import numpy as np

def nothing(x):
    # Função de callback exigida pelo trackbar, mas não precisamos fazer nada nela.
    pass

# 1. Inicializa a captura da webcam
cap = cv2.VideoCapture(0)

# 2. Cria uma janela para exibir os resultados e o trackbar
cv2.namedWindow("Ajuste de Threshold")

# 3. Cria o trackbar (barra deslizante)
# Nome, Janela, Valor Inicial, Valor Máximo, Função de Callback
cv2.createTrackbar("Limite", "Ajuste de Threshold", 127, 255, nothing)

print("Pressione 'q' para sair.")

while True:
    # Captura frame por frame
    ret, frame = cap.read()
    if not ret:
        break

    # Passo A: Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Passo B: Pegar o valor atual do trackbar
    threshold_val = cv2.getTrackbarPos("Limite", "Ajuste de Threshold")

    # Passo C: Aplicar o Threshold Binário
    # Se o pixel > threshold_val, vira 255 (branco). Caso contrário, 0 (preto).
    _, threshold_img = cv2.threshold(gray, threshold_val, 255, cv2.THRESH_BINARY)

    # Para exibir simultaneamente, vamos redimensionar e concatenar as imagens
    # (Opcional: você pode apenas usar 3 cv2.imshow diferentes)
    
    # Como 'frame' tem 3 canais (BGR) e as outras têm 1 (cinza), 
    # precisamos converter as cinzas de volta para BGR apenas para visualização lado a lado.
    gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    thresh_3ch = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2BGR)

    # Empilha as imagens horizontalmente: Original | Cinza | Threshold
    resultado = np.hstack((frame, gray_3ch, thresh_3ch))

    # Exibe a janela única com as três visualizações
    cv2.imshow("Ajuste de Threshold", resultado)

    # Interrompe o loop ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
