with open ('day2.in') as infile:
    data = infile.read().split('\n')

triples = 0
doubles = 0

def get_difference_count(box_id1, box_id2):
    differences = 0
    for current_index in range(len(box_id1)):
        if box_id1[current_index] != box_id2[current_index]:
            differences += 1
            
    return differences

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
        
for box_id1 in data:
    for box_id2 in data:
        if get_difference_count(box_id1, box_id2) == 1:
            result = ''
            for current_index in range(len(box_id1)):
                if box_id1[current_index] == box_id2[current_index]:
                    result += box_id1[current_index]
            print(result)