from pdf_processor import PDFProcessor

class PDFTextExtractorService:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Service started. Listening for PDF files...")

    def stop(self):
        self.running = False
        print("Service stopped.")

    def process_pdf(self, pdf_file_path):
        if not self.running:
            print("Service is not running. Cannot process PDF.")
            return None

        processor = PDFProcessor()
        text = processor.extract_text(pdf_file_path)
        return text