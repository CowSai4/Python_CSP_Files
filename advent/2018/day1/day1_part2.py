with open('day1.in') as infile:
    data = infile.read().split('\n')

final = 0
next_line = 0

changes = [0]
duplicates = []

while len(duplicates) < 1:

    for frequency in data:

        symbol = data[next_line][0]
        number = int(data[next_line][1:])

        if symbol == '+':
            final += number
        elif symbol == '-':
            final -= number

        next_line += 1

        if final not in changes:
            changes.append(final)
        else:
            duplicates.append(final)
            
    next_line = 0

print('The duplicates are:',duplicates)