def say_hello():
    print('Hello')

def write_list_to_file(filename, word_list):
    outfile = open(filename, 'w')
    for word in word_list:
        outfile.write(word + '\n')
    outfile.close()

def read_list_from_file(filename):
    try:
        words = []
        infile = open(filename, 'r')
        for line in infile:
            words.append(line.strip())
        infile.close()
        return words
    except:
        return[]