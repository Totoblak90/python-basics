dictionary = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def caesar_cipher(word: str, shift_val: int, encode: bool):
    new_word = ''

    if encode is True:
        print('encoding')
        for letter in word:
            lower_lett = letter.lower()
            dictionary_letter_index = dictionary.index(lower_lett)
            positions_to_move = dictionary_letter_index + shift_val

            if positions_to_move < len(dictionary):
                new_word += dictionary[dictionary_letter_index + shift_val]
            else:
                positions_after_restart = shift_val - ( (len(dictionary) - 2) - dictionary_letter_index )
                new_word += dictionary[positions_after_restart]

        return new_word

    else:
        print('decoding')
        for letter in word:
            lower_lett = letter.lower()
            dictionary_letter_index = dictionary.index(lower_lett)
            positions_to_move = dictionary_letter_index - shift_val

            if positions_to_move >= 0:
                new_word += dictionary[dictionary_letter_index - shift_val]
            else:
                new_word += dictionary[len(dictionary) - 2 + positions_to_move]

        return new_word

# Prueba de la función
encoding = input("Type 'encode' or 'decode' to begin: ")
while encoding != 'encode' and encoding != 'decode':
    encoding = input('wrong choice. Please type again: ')

message = input('Please type your message (only letters): ').lower()
while not message.isalpha():
    message = input('Characters not accepted, please try again: ').lower()

shift_value = int(input('Please type a shift value: '))

while shift_value >= len(dictionary):
    shift_value = int(input(f"Maximum value accepted is:  {len(dictionary) - 1}. Please type again "))

print(caesar_cipher(message, shift_value, True if encoding == 'encode' else False))
