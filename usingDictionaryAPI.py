import requests

def get_meanings_from_free_dictionary(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Free Dictionary API: {e}")
        return None

def get_meanings_from_words_api(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Words API: {e}")
        return None

def get_meanings_from_urban_dictionary(word):
    url = f'https://api.urbandictionary.com/v0/define?term={word}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Urban Dictionary: {e}")
        return None

def display_meanings(word):
    print(f"\n{'='*40}\nMeanings for '{word}':\n{'='*40}\n")

    # Free Dictionary API
    meanings = get_meanings_from_free_dictionary(word)
    print("Free Dictionary API:")
    if meanings:
        for meaning in meanings:
            print(f"Word: {meaning['word']}")
            for definition in meaning['meanings']:
                for defn in definition['definitions']:
                    print(f" - Definition: {defn['definition']}")
                    if 'example' in defn:
                        print(f"   Example: {defn['example']}")
        print("\n" + "-"*40)  # Separator
    else:
        print("No results from Free Dictionary API.")
        print("-" * 40)

    # Words API
    meanings = get_meanings_from_words_api(word)
    print("Words API:")
    if meanings and 'definitions' in meanings:
        for definition in meanings['definitions']:
            print(f" - Definition: {definition['definition']}")
            if 'example' in definition:
                print(f"   Example: {definition['example']}")
        print("\n" + "-"*40)  # Separator
    else:
        print("No results from Words API.")
        print("-" * 40)

    # Urban Dictionary API
    meanings = get_meanings_from_urban_dictionary(word)
    print("Urban Dictionary:")
    if meanings and 'list' in meanings and meanings['list']:
        for entry in meanings['list']:
            print(f" - Definition: {entry['definition']}")
            if 'example' in entry:
                print(f"   Example: {entry['example']}")
        print("\n" + "-"*40)  # Separator
    else:
        print("No results from Urban Dictionary.")
        print("-" * 40)

def main():
    word = input("Enter a word: ")
    display_meanings(word)

if __name__ == "__main__":
    main()
