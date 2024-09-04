import requests

def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        for entry in data:
            print(f"Word: {entry['word']}\n")
            
#            Phonetics section (commented out)
            if 'phonetics' in entry:
                print("Phonetics:")
                for phonetic in entry['phonetics']:
                    text = phonetic.get('text', 'N/A')
                    audio = phonetic.get('audio', 'N/A')
                    print(f"  - Text: {text}")
                    print(f"  - Audio: {audio}")
                print()
            
            if 'meanings' in entry:
                print("Meanings:")
                for meaning in entry['meanings']:
                    part_of_speech = meaning['partOfSpeech']
                    print(f"  - Part of Speech: {part_of_speech}\n")
                    
                    if 'definitions' in meaning:
                        print("    Definitions:")
                        for i, definition in enumerate(meaning['definitions'], start=1):
                            print(f"      {i}. {definition.get('definition', 'N/A')}")
                            
                            if 'example' in definition:
                                print(f"        Example: {definition['example']}")
                        print()

                    if 'synonyms' in meaning and meaning['synonyms']:
                        print("    Synonyms:")
                        print(f"      {', '.join(meaning['synonyms'])}\n")

                    if 'antonyms' in meaning and meaning['antonyms']:
                        print("    Antonyms:")
                        print(f"      {', '.join(meaning['antonyms'])}\n")

            if 'origin' in entry:
                print(f"Origin: {entry['origin']}\n")
                
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
word_to_search = "abstract"
get_word_info(word_to_search)
