import my_utilities

my_utilities.say_hello()

filename = 'words.txt'

word_list = my_utilities.read_list_from_file(filename)

word = input('enter in a word, or quit to stop: ')

while word != 'quit':
    word_list.append(word)
    word = input('enter in a word, or quit to stop: ')
if word == 'quit':
    word_list.append('ended session')

my_utilities.write_list_to_file(filename, word_list)

