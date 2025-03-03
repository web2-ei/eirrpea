from googletrans import Translator

# Create a Translator object
translator = Translator()

def translate_to_english(text):
    """
    Translates the input text to English, regardless of the input language.
    
    :param text: Text to be translated.
    :return: Translated text in English.
    """
    try:
        # Detect the language of the input text
        detected_lang = translator.detect(text).lang
        print(f"Detected language: {detected_lang}")
        
        # Translate the text to English
        translated = translator.translate(text, dest='en')
        
        # Output the translated text
        print(f"Translated text: {translated.text}")
        return translated.text

    except Exception as e:
        # Log the error and continue without crashing the program
        print(f"Error occurred during translation: {e}")
        return "Translation failed. Please try again."

# Example Usage
if __name__ == "__main__":
    while True:  # Keep the app running without crashing
        user_input_translation = input("\nEnter text to translate to English: ")
        
        if user_input_translation.lower() == 'ehoccajcanocanooevbevbuosbovwebioçae':
            print("Exiting the translator. Goodbye!")
            break
        

        result = translate_to_english(user_input_translation)
        if result:
            print(f"Translation result: {result}")
