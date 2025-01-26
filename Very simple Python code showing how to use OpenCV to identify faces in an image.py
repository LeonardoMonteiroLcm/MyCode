import cv2 # pip install opencv-python

# Função principal
def detectar_rostos(caminho_imagem):
    # Carregar o classificador de detecção de rostos pré-treinado (Haar Cascade)
    classificador_rostos = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                                 'haarcascade_frontalface_default.xml')

    # Carregar a imagem
    imagem = cv2.imread(caminho_imagem)

    # Converter a imagem para escala de cinza (necessário para o classificador)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    rostos = classificador_rostos.detectMultiScale(imagem_cinza, scaleFactor=1.1, 
                                                   minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, largura, altura) in rostos:
        cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 0, 255), 2)

    # Mostrar a imagem com os rostos destacados
    cv2.imshow('Rostos Detectados', imagem)

    # Esperar até que uma tecla seja pressionada e fechar a janela
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho para a imagem (substitua pelo caminho da sua imagem)
caminho_imagem = 'caminho_para_a_sua_imagem.jpg'

# Chamar a função para detectar rostos
detectar_rostos(caminho_imagem)
