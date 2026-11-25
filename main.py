from translation import *

source_text = read_txt_file("source.txt")
translation_text = read_txt_file("translation.txt")

source_lang = input("Enter source language (en/id): ").upper()
target_lang = input("Enter target language (en/id): ").upper()


if not validate_language(source_lang, target_lang):
    print("Error: Invalid language pair.")

elif source_text is not None and translation_text is not None:
    print("\nBoth files have been loaded successfully.")
    print("Language pair is valid.")
    print(f"Translating from {source_lang} to {target_lang}")
    
    deepl_result, mymemory_result, grammar_issues = analyze_translation(
        source_text,
        translation_text,
        source_lang,
        target_lang
    )
    
    display_report(deepl_result, mymemory_result, grammar_issues)
    save_report(deepl_result, mymemory_result, grammar_issues)
else:
    print("Cannot continue: one or both files could not be read.")