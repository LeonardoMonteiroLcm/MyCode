import cv2 # pip install opencv-python
import pytesseract # pip install pytesseract

def apply_ocr(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza (opcional, melhora OCR em alguns casos)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar suavização para reduzir ruídos (opcional)
    gray_image = cv2.medianBlur(gray_image, 3)

    # Salvar imagem processada (opcional, para análise)
    processed_image_path = "processed_image.png"
    cv2.imwrite(processed_image_path, gray_image)

    # Extrair texto da imagem usando Tesseract OCR
    text = pytesseract.image_to_string(gray_image, lang="por")  # 'lang="por"' para OCR em português

    return text

# Caminho da imagem
image_path = "caminho_para_sua_imagem.jpg"

# Certifique-se de que o Tesseract esteja instalado e configurado no PATH
# Ou configure o caminho diretamente, como mostrado abaixo:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Executar OCR
resultado = apply_ocr(image_path)

print("Texto extraído:")
print(resultado)