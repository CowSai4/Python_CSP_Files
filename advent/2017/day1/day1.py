with open('day1.in') as infile:
    num = infile.read()

total = 0

for index in range(-1,len(num) -1):
    if num[index] == num[index + 1]:
        total += int(num[index])



print(total)

