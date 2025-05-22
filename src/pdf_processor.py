from tqdm import tqdm

class PDFProcessor:
    def __init__(self):
        pass

    def extract_text(self, pdf_path, ocr_lang='rus+eng', resolution=200):
        import pdfplumber
        import pytesseract
        from PIL import Image

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            pages_text = []
            for page in tqdm(pdf.pages, desc="OCR страниц"):
                page_text = page.extract_text()
                if page_text and page_text.strip():
                    pages_text.append(page_text)
                else:
                    image = page.to_image(resolution=resolution).original
                    if hasattr(page, "rotation") and page.rotation:
                        image = image.rotate(-page.rotation, expand=True)
                    ocr_text = pytesseract.image_to_string(image, lang=ocr_lang)
                    pages_text.append(ocr_text)
        return "\n".join(pages_text).strip()

if __name__ == "__main__":
    import os
    os.system("pip install -r requirements.txt")