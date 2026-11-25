import unittest
from unittest.mock import patch
from translation import validate_language, read_txt_file, display_report


#unittest runs our function automatically and compares 
#the results with our expected results.

#unittest.TestCase is a built-in Python class that we inherit 
#so that our class gets the ability to run tests.
class TestTranslation(unittest.TestCase):

    def test_valid_language_pair(self):
        result = validate_language("EN", "ID")
        self.assertTrue(result)
        
    def test_valid_language_pair2(self):
        result = validate_language("ID", "EN")
        self.assertTrue(result)

    def test_invalid_language_pair(self):
        result = validate_language("FR", "ID")
        self.assertFalse(result)

    def test_same_language_pair(self):
        result = validate_language("EN", "EN")
        self.assertFalse(result)
        
    def test_read_existing_file(self):
        result = read_txt_file("source.txt")
        self.assertIsNotNone(result)

    def test_read_missing_file(self):
        result = read_txt_file("file_not_found.txt")
        self.assertIsNone(result)




    #display_report() function's job is to print output to the terminal, 
    #not return a value. Therefore, the testing method is slightly different.
    #We can use unittest.mock.patch to capture the print() 
    #output without having to manually read the terminal.
    
    ##NOTE: grammar message test 1 : 
    # test when the grammar API is successful and 
    # does not find any errors ([]).

    def test_display_report_no_grammar_issues(self):
        
        #We don't need to actually read the output of display_report() function in the terminal.
        #The patch captures the print() call for inspection by unittest
        with patch("builtins.print") as mock_print:
            display_report(
                "Hello", #DeepL result (using mock input)
                "Halo", #MyMemory resu;t (using mock input)
                [] #LanguageTool successfully checked the text, but found no grammar issues.
            )

        #check whether print() was ever called with the message we expect
        mock_print.assert_any_call("No grammar issues found.")
        
        
    ##NOTE: grammar message test 2 : 
    # test when the grammar API is successful and 
    # find any errors.
    def test_display_report_with_grammar_issues(self):
        grammar_issues = [
            {
                "shortMessage": "Agreement error",
                "sentence": "She go to school.",
                "replacements": [
                    {"value": "goes"},
                    {"value": "went"}
                ]
            }
        ]

        with patch("builtins.print") as mock_print:
            display_report("Hello", "Halo", grammar_issues)

        mock_print.assert_any_call("Issue:", "Agreement error")
        mock_print.assert_any_call("Sentence:", "She go to school.")
        mock_print.assert_any_call("Suggestions:", "goes, went")


    ##NOTE: grammar message test 2 : 
    # Grammar API unavailable
    def test_display_report_grammar_unavailable(self):
        with patch("builtins.print") as mock_print:
            display_report("Hello", "Halo", None)

        mock_print.assert_any_call(
            "LanguageTool: Grammar checking unavailable."
        )


    #Translation API unavailable (DeepL adn MyMemory API)
    def test_display_report_translation_unavailable(self):
        with patch("builtins.print") as mock_print:
            display_report(None, None, [])

        mock_print.assert_any_call(
            "\nDeepL: Unable to retrieve translation."
        )

        mock_print.assert_any_call(
            "\nMyMemory: Unable to retrieve translation."
        )
if __name__ == "__main__":
    unittest.main()