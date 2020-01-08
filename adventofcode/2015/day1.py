
infile = open('inputs/day1.txt','r')
data = infile.read()
infile.close()

floor = 0
counter = 0



#for element in iterable:
for char in data:
    if char == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    counter += 1
    if floor == -1:
        print('This is counter:',counter)
