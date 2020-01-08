with open ('day2.in') as infile:
    data = infile.read().split('\n')

triples = 0
doubles = 0

for box_id in data:
    has_3 = False
    has_2 = False
    for letter in set(box_id):
        if box_id.count(letter) == 3 and not has_3:
            triples += 1
            has_3 = True
        if box_id.count(letter) == 2 and not has_2:
            doubles += 1
            has_2 = True
        

print('there are:', triples, 'triples')
print('there are:', doubles, 'doubles')

final = doubles * triples

print('final is:', final)