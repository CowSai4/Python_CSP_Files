
phrase = input('give me a phrase: ')
character = input('give me a character: ')

x = 0
count = 0

def count_different_characters(phrase, character):
    global count, x
    while x < len(phrase):
        if character != phrase[x]:
            count += 1
        x += 1

count_different_characters(phrase, character)
print('count of non characters is:  ', count)