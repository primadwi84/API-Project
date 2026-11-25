from api import*
import csv

#reading file
def read_txt_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    #if one of the execption condition rise,
    #function read_txt_file() finish without running its return statement
    #if no return was executed, Python automatically return None
    #that's why we need to make if source_text is not None after executing 
    #read_txt_file() function

    #file not found
    except FileNotFoundError:
        print("Error: File not found.")

    #No permission to read the file
    except PermissionError:
        print("Error: You do not have permission to read this file.")

    #Other file system operation errors
    except OSError as error:
        print("File error:", error)
        

#Execute the API and return results
def analyze_translation(source_text, translation_text, source_lang, target_lang):

    # Get translation reference from MyMemory
    mymemory_result = get_mymemory_translation(
        source_text,
        f"{source_lang}|{target_lang.lower()}"
    )

    # Get translation reference from DeepL
    deepl_result = deepl_translation(
        source_text,
        source_lang,
        target_lang
    )

    # Grammar checking
    #If the source language is English (EN), check the source_text
    if source_lang == "EN":
        grammar_text = source_text

    #If the target language is English (EN), check translation_text
    elif target_lang == "EN":
        grammar_text = translation_text

    #If both are not English, there is no need to run LanguageTool
    else:
        grammar_text = None


    if grammar_text is not None:
        grammar_issues = check_grammar(grammar_text)
    else:
        grammar_issues = None
        

    return deepl_result, mymemory_result, grammar_issues


#Check results and display reports
def display_report(deepl_result, mymemory_result, grammar_issues):

    print("\n--- Translation Quality Report ---")

    #Error Handling (if DeepL API failed to give apropriate API response)
    if deepl_result is None:
        print("\nDeepL: Unable to retrieve translation.")
    else:
        print("\nDeepL Reference:")
        print(deepl_result)

    #Error Handling (if MyMemory API failed to give apropriate API response)
    if mymemory_result is None:
        print("\nMyMemory: Unable to retrieve translation.")
    else:
        print("\nMyMemory Reference:")
        print(mymemory_result)

    print("\nGrammar Check:")

    if grammar_issues is None:
        print("LanguageTool: Grammar checking unavailable.")
    elif grammar_issues:
        for issue in grammar_issues:
            print("Issue:", issue["shortMessage"])
            print("Sentence:", issue["sentence"])

            suggestions = [
                replacement["value"]
                for replacement in issue["replacements"]
            ]

            print("Suggestions:", ", ".join(suggestions))
    else:
        print("No grammar issues found.")
        
    
def save_report(deepl_result, mymemory_result, grammar_issues):
    with open("report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Section", "Result"])

        writer.writerow(["DeepL Reference", deepl_result])
        writer.writerow(["MyMemory Reference", mymemory_result])

        writer.writerow(["Grammar Check", ""])

        if grammar_issues is None:
            writer.writerow(["Status", "Grammar checking unavailable."])

        elif grammar_issues:
            for issue in grammar_issues:
                suggestions = [
                    replacement["value"]
                    for replacement in issue["replacements"]
                ]

                writer.writerow(["Issue", issue["shortMessage"]])
                writer.writerow(["Sentence", issue["sentence"]])
                writer.writerow(["Suggestions", ", ".join(suggestions)])

        else:
            writer.writerow(["Status", "No grammar issues found."])

    print("Report saved successfully as report.csv.")
    

def validate_language(source_lang, target_lang):
    if source_lang not in ["EN", "ID"] or target_lang not in ["EN", "ID"]:
        return False

    elif source_lang == target_lang:
        return False

    else:
        return True