# PDF Text Extractor Service

Сервис для извлечения текста из PDF-файлов, включая обычные и отсканированные (сканированные) PDF с помощью OCR (Tesseract). Поддерживает смешанные языки (русский и английский) на одной странице.

---

## Возможности

- Извлечение текста из обычных PDF-файлов.
- Автоматическое распознавание текста (OCR) из отсканированных PDF-файлов с помощью Tesseract.
- Поддержка одновременного распознавания русского и английского языков (`rus+eng`).
- Автоматическое определение языка содержимого.
- Сохранение результата в `.txt` файл рядом с исходным PDF.

---

## Установка

### 1. Клонируйте репозиторий

```sh
git clone https://github.com/Bezzhanov/PDF-TEXT-EXTRACTOR-SERVICE.git
cd pdf-text-extractor-service
```

### 2. Установите Python-зависимости

```sh
pip install -r requirements.txt
```

### 3. Установите Tesseract OCR

- Скачайте установщик для Windows:  
  [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- Установите Tesseract, запомните путь установки (например, `C:\Program Files\Tesseract-OCR`).
- Добавьте путь к Tesseract в переменную среды `PATH` или укажите его явно в коде:
  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
- Для русского и английского языков убедитесь, что в папке `tessdata` есть файлы `rus.traineddata` и `eng.traineddata`.

---

## Использование

### Из командной строки

```sh
python src/main.py "путь\к\вашему\файлу.pdf"
```

- После обработки текст будет выведен в консоль и сохранён в файл с тем же именем, но расширением `.txt` рядом с PDF.

---

## Структура проекта

- `src/main.py` — точка входа, обработка аргументов, запуск сервиса.
- `src/service.py` — класс службы, управляющий обработкой PDF.
- `src/pdf_processor.py` — класс для извлечения текста и OCR.
- `requirements.txt` — список зависимостей.

---

## Зависимости

См. файл `requirements.txt`:

````txt
pdfplumber
pytesseract
Pillow
langdetect
````