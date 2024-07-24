# Tet to Morse Code Converter
import json

with open('morse_dictionary.json', 'r') as file:
    morse_dict = json.load(file)


def text_to_morse(word: str) -> str:
    morse_code = ""
    for letter in word:
        morse_code += morse_dict.get(letter.upper(), '') + ' '
    return morse_code.strip()


if __name__ == "__main__":
    print("Welcome to the text to Morse converter")
    while True:
        text = input('Enter a word or click enter to exit:\n')
        if text:
            print(text_to_morse(text))
        else:
            break
