
with open('day1.in') as infile:
    data = infile.read().split('\n')

fuel = [int(mass)//3-2 for mass in data]
final = 0

def calc_fuel():
    global final
    for fuels in fuel:
        while fuels > 0:
            final += fuels
            fuels = fuels // 3-2
    return final

calc_fuel()

print(final)