import os
import time
import sys
from service import PDFTextExtractorService
from pdf_processor import PDFProcessor
from langdetect import detect_langs, DetectorFactory, LangDetectException
import warnings
import logging
import pdfplumber

warnings.filterwarnings("ignore")
logging.getLogger("pdfminer").setLevel(logging.ERROR)

DetectorFactory.seed = 0  # Для стабильности результатов

def main():
    service = PDFTextExtractorService()
    service.start()

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        if os.path.isfile(pdf_path):
            print(f"Начато распознавание файла: {pdf_path}")
            try:
                # Получаем количество страниц заранее
                import pdfplumber
                with pdfplumber.open(pdf_path) as pdf:
                    num_pages = len(pdf.pages)

                extracted_text = service.process_pdf(pdf_path)
                try:
                    langs = detect_langs(extracted_text)
                    main_lang = langs[0].lang if langs else None
                    if langs and langs[0].prob > 0.95:
                        ocr_lang = main_lang
                        if ocr_lang == 'ru':
                            ocr_lang = 'rus'
                        elif ocr_lang == 'en':
                            ocr_lang = 'eng'
                    else:
                        ocr_lang = 'rus+eng'
                except LangDetectException:
                    ocr_lang = 'rus+eng'

                # Если текст пустой или язык не определён, делаем OCR с выбранным языком и меньшим разрешением
                if not extracted_text.strip():
                    processor = PDFProcessor()
                    extracted_text = processor.extract_text(pdf_path, ocr_lang=ocr_lang, resolution=100)

                txt_path = os.path.splitext(pdf_path)[0] + ".txt"
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(extracted_text)

                # Выводим статистику
                num_chars = len(extracted_text)
                print(f"Распознавание завершено. Страниц: {num_pages}, символов: {num_chars}")
            except Exception as e:
                print(f"Ошибка при распознавании PDF: {e}")
            service.stop()
            return
        else:
            service.stop()
            return

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        service.stop()

if __name__ == "__main__":
    main()