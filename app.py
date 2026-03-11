import cv2
import numpy as np

def nada(x):
    pass

# 1. Inicializa a captura da webcam
cap = cv2.VideoCapture(0)

# 2. Cria a janela e o Trackbar para o Limiar (Threshold)
cv2.namedWindow("Parametros")
cv2.createTrackbar("Limiar", "Parametros", 127, 255, nada)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Converte para Escala de Cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. Obtém o valor atual do Trackbar
    valor_limiar = cv2.getTrackbarPos("Limiar", "Parametros")

    # 5. Aplica o Threshold Binário
    # Se o pixel > valor_limiar vira 255 (branco), senão 0 (preto)
    _, threshold = cv2.threshold(cinza, valor_limiar, 255, cv2.THRESH_BINARY)

    # --- LÓGICA DO HISTOGRAMA (Igual à imagem enviada) ---
    # Calcula o histograma da imagem em cinza
    hist = cv2.calcHist([cinza], [0], None, [256], [0, 256])
    
    # Cria uma imagem preta para desenhar o histograma (300px altura, 256px largura)
    hist_img = np.zeros((300, 256, 3), dtype=np.uint8)
    
    # Normaliza o histograma para caber na altura da imagem
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    
    # Desenha as linhas brancas do histograma
    for i in range(1, 256):
        # Adicionamos o [0] para pegar o valor numérico puro do array
        ponto_anterior = int(hist[i-1][0])
        ponto_atual = int(hist[i][0])
        
        cv2.line(hist_img, (i-1, 300 - ponto_anterior), (i, 300 - ponto_atual), (255, 255, 255), 1)
    
    # Desenha a LINHA VERMELHA (ajustada para não dar erro)
    cv2.line(hist_img, (valor_limiar, 0), (valor_limiar, 300), (0, 0, 255), 2)
    # -----------------------------------------------------

    # Redimensiona para caber tudo na tela (opcional)
    frame_res = cv2.resize(frame, (400, 300))
    cinza_res = cv2.cvtColor(cv2.resize(cinza, (400, 300)), cv2.COLOR_GRAY2BGR)
    thresh_res = cv2.cvtColor(cv2.resize(threshold, (400, 300)), cv2.COLOR_GRAY2BGR)

    # Organiza a exibição (Original | Cinza | Threshold)
    # O Histograma será exibido em uma janela separada para destaque
    layout_superior = np.hstack((frame_res, cinza_res, thresh_res))

    cv2.imshow("Aplicacao Threshold - Original | Cinza | Binario", layout_superior)
    cv2.imshow("Histograma e Limiar", hist_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
