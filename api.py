import requests
from pprint import pprint
import os #calling modules to interact with the operating system environment
from dotenv import load_dotenv #take the load_dotenv function from the dotenv library



#MyMemory : looking for alternative translations from translation memory.
#Input: source text → EN to ID
def get_mymemory_translation(text, langpair):

    url = "https://api.mymemory.translated.net/get"

    parameters = {
        "q": text,
        "langpair": langpair
    }

    #the code we want to try to run
    try:
        response = requests.get(
            url,
            params=parameters,
            timeout=15
        )

        #raises an exception if the HTTP status code indicates failure
        response.raise_for_status()

        data = response.json()
        
        return data["responseData"]["translatedText"]

    #what to do if a certain error occurs:

    #Timeout : Server takes too long to respond
    except requests.exceptions.Timeout:
        #return None here, because #Error Handling information display in display_report() is enough 
        return None
        
    #specific exception (instance of RequestException)
    except requests.exceptions.JSONDecodeError:
        return None

    #RequestException : Problem in HTTP request
    except requests.exceptions.RequestException as error:
        return None

    #build-in exception
    #KeyError: occurs if the key we are looking for is not available
    #ValueError: one of the errors that can occur when the JSON is invalid
    except (ValueError, KeyError):
        return None
        

        
        
        
#LanguageTool : Checks the grammar of translated English text.
#Currently, this feature is only used if the target text is in English.
def check_grammar(text):

    url = "https://api.languagetool.org/v2/check"

    parameters = {
        "text": text,
        "language": "en-US"
    }
    
    try:

        response = requests.post(
            url,
            data=parameters,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        return data["matches"]

    #what to do if a certain error occurs:
     
    #Timeout : Server takes too long to respond
    except requests.exceptions.Timeout:
        return None
        
    #specific exception (instance of RequestException)
    except requests.exceptions.JSONDecodeError:
        return None
        
    #RequestException : Problem in HTTP request
    except requests.exceptions.RequestException as error:
        return None
        
    #build-in exception
    #KeyError: occurs if the key we are looking for is not available
    #ValueError: one of the errors that can occur when the JSON is invalid
    except (ValueError, KeyError):
        return None
        
        

#Compare user translations with machine translations as a reference.
#Input: source text → EN to ID
def deepl_translation(text, source_lang, target_lang):
    
    url = "https://api-free.deepl.com/v2/translate"

    load_dotenv() #read the .env file and load its variables
    
    api_key = os.getenv("DEEPL_API_KEY")

    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}",
        "Content-Type": "application/json"
    }

    parameters = {
        "text": [text],
        "source_lang" : source_lang, 
        "target_lang": target_lang
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=parameters,
            timeout=15
        )
        response.raise_for_status()

        data = response.json()

        return data["translations"][0]["text"]

    #what to do if a certain error occurs:
     
    #Timeout : Server takes too long to respond
    except requests.exceptions.Timeout:
        return None
        
    #specific exception (instance of RequestException)
    except requests.exceptions.JSONDecodeError:
        return None
        
    #RequestException : Problem in HTTP request
    except requests.exceptions.RequestException as error:
        return None
        
    #build-in exception
    #KeyError: occurs if the key we are looking for is not available
    #ValueError: one of the errors that can occur when the JSON is invalid
    except (ValueError, KeyError):
        return None
        
        