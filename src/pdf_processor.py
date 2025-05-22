class PDFProcessor:
    def __init__(self):
        pass

    def extract_text(self, pdf_path, ocr_lang='rus+eng'):
        import pdfplumber
        import pytesseract
        from PIL import Image

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text and page_text.strip():
                    text += page_text + "\n"
                else:
                    # Используем сразу оба языка для OCR
                    image = page.to_image(resolution=300).original
                    ocr_text = pytesseract.image_to_string(image, lang=ocr_lang)
                    text += ocr_text + "\n"
        return text.strip()

if __name__ == "__main__":
    import os
    os.system("pip install -r requirements.txt")