# Translation Quality Assistant

## 1. Project Description

Translation Quality Assistant is a Python-based application designed to support translation and localization students in reviewing their translations.

The application compares the source text with translation references from DeepL and MyMemory, and checks English grammar using LanguageTool.

It supports two language directions:
- English to Indonesian (EN → ID)
- Indonesian to English (ID → EN)

## 2. Features

- Reads source and translated texts from `.txt` files.
- Retrieves translation references from DeepL and MyMemory.
- Checks English grammar using LanguageTool.
- Displays a translation quality report in the terminal.
- Exports the report to a CSV file.
- Handles API errors and unavailable responses.

## 3. APIs and Libraries

| API / Library | Purpose |
|---|---|
| DeepL API | Provides machine translation references |
| MyMemory API | Provides translation memory references |
| LanguageTool API | Checks English grammar |
| Requests | Sends HTTP requests |
| python-dotenv | Loads API credentials from `.env` |

## 4. Project Setup

### Requirements

- Python 3
- A DeepL API Free key

### Installation

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### API Configuration

Create a `.env` file in the project directory and add your DeepL API key:

```text
DEEPL_API_KEY=your_deepl_api_key_here
```

Do not share your actual API key.

## 5. Input Files

The application requires two text files:

- `source.txt`: Contains the original text.
- `translation.txt`: Contains the translated text.

Both files should be placed in the project directory.

## 6. Running the Application

Run the following command:

```bash
python main.py
```

Enter the source and target language when prompted:

- `EN` for English
- `ID` for Indonesian

The application displays the translation references and grammar-checking results in the terminal and saves the report as `report.csv`.

## 7. Running Unit Tests

Run:

```bash
python -m unittest test_translation.py
```

The tests cover language-pair validation, file reading, and report display under different conditions.

## 8. Limitations

- DeepL and MyMemory provide translation references, not definitive assessments of translation accuracy.
- LanguageTool checks English grammar only. It does not evaluate Indonesian grammar or semantic translation accuracy.
- API availability and usage limits may affect the results.