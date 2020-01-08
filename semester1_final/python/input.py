
numbers = []

amount = int((input('give me an amount of numbers you want to put in: ')))

for num_in in range(amount):
    nums = int(input('give me a number: '))
    numbers.append(nums)

print('minimum is:  ', min(numbers))
print('maximum is:  ', max(numbers))
print('sum is:  ', sum(numbers))