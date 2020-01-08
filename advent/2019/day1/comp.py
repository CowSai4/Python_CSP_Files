numbers = [6,2,0,3,4,7]

squares = []

for num in numbers:
    squares.append(num**2)

print([num**2 for num in numbers])