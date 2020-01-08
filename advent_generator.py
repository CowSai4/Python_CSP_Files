import os, os.path

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

create_folder('advent')

for years in range(2015, 2020):
    year_path = f'advent/{years}'
    create_folder(year_path)
    for day in range(1, 26):
        day_path = f'advent/{years}/day{day}'
        create_folder(day_path)
        open(f'{day_path}/day{day}.py','a').close()
        open(f'{day_path}/day{day}.in','a').close()
        open(f'{day_path}/day{day}.test','a').close()       