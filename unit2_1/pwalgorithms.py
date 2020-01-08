 # Module pwalgorithms
import os

# get words from password dictionary file
def get_dictionary(word_file="dictionary.txt"):
  words = []
  dirname = os.path.dirname(__file__)
  dictionary_file = open(os.path.join(dirname, word_file))
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0
  for word1 in words:
    for word2 in words:
      guesses += 1
      if word1 + word2 == password:
        return True, guesses
  return False, guesses

numbers = ['0','1','2','3','4','5','6','7','8','9']

def two_word_digit(password):
  words = get_dictionary()
  guesses = 0
  for word1 in words:
    for word2 in words:
      for digit in numbers:
        guesses += 1
        if word1 + word2 + digit == password or if digit + word1 + word2 == password
          return True, guesses
  return False, guesses