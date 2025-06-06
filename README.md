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

### 1. Клонируйте репозиторий или скачайте последний релиз

```sh
git clone https://github.com/Bezzhanov/PDF-TEXT-EXTRACTOR-SERVICE.git
cd pdf-text-extractor-service
```

```
https://github.com/Bezzhanov/PDF-TEXT-EXTRACTOR-SERVICE/releases
```

### 2. Установите Python-зависимости (если будете использовать python скрипт)

```sh
pip install -r requirements.txt
```

### 3. Установите Tesseract OCR

- Скачайте установщик для Windows:  
  [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- Установите Tesseract, запомните путь установки (`C:\Program Files\Tesseract-OCR`).
- Добавьте путь к Tesseract в переменную среды `PATH` 
- Для русского и английского языков убедитесь, что в папке `tessdata` есть файлы `rus.traineddata` и `eng.traineddata`.

---

## Использование

### Из командной строки

```sh
python src/main.py "путь\к\вашему\файлу.pdf"
```

```powershell
.\pdf-text-extractor.exe "путь\к\вашему\файлу.pdf"
```

- После обработки текст будет выведен в консоль и сохранён в файл с тем же именем, но расширением `.txt` рядом с PDF.

---

## Структура проекта

- `src/main.py` — точка входа, обработка аргументов, запуск сервиса.
- `src/service.py` — класс службы, управляющий обработкой PDF.
- `src/pdf_processor.py` — класс для извлечения текста и OCR.
- `requirements.txt` — список зависимостей.
- `dist/pdf-text-extractor.exe` - консольное приложение

---

## Зависимости

См. файл `requirements.txt`:

````txt
pdfplumber
pytesseract
Pillow
langdetect
tqdm