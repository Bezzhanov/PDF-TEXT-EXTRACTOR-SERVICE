import os
import time
import sys
from service import PDFTextExtractorService
from pdf_processor import PDFProcessor
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0  # Для стабильности результатов

def main():
    service = PDFTextExtractorService()
    service.start()

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        if os.path.isfile(pdf_path):
            extracted_text = service.process_pdf(pdf_path)
            try:
                language = detect(extracted_text)
            except LangDetectException:
                language = None

            if not extracted_text.strip() or not language:
                processor = PDFProcessor()
                text = processor.extract_text(pdf_path)  # lang='rus+eng' по умолчанию
                try:
                    language = detect(text)
                except LangDetectException:
                    language = None

            txt_path = os.path.splitext(pdf_path)[0] + ".txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(extracted_text)
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