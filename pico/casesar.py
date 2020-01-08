alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_letter(letter, shift):
    if letter == ' ':
        return ' '
    index = alphabet.index(letter)
    shifted_index = (index + shift) % 26
    return alphabet[shifted_index]

def shift_phrase(phrase, shift):
    result = ''
    for letter in phrase:
        result += shift_letter(letter, shift)
    return result

def brute_force_shift(phrase):
    for shift in range (1,26):
        print(shift_phrase(phrase, shift))

brute_force_shift('')
