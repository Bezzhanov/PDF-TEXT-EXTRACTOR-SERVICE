from pdf_processor import PDFProcessor

class PDFTextExtractorService:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def process_pdf(self, pdf_file_path):
        if not self.running:
            return None

        processor = PDFProcessor()
        text = processor.extract_text(pdf_file_path)
        return text