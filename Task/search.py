def Search_Entry(file):

    print(f'Введите элемент имя сотрудника для поиска в БД: ')
    name = input()
   
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if name.lower() in line.lower(): 
                    print(line)