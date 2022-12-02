def reading():
    contacts = [0] * 5
    contacts[0] = input("Введите фамилию: ")
    contacts[1] = input("Введите имя: ")
    contacts[2] = input("Введите Отчество: ")
    contacts[3] = input("Введите Телефон: ")
    contacts[4] = input("Введите описание: ")
    contacts_str = ', '.join(map(str, contacts))
    # return contacts_str
# def newstring(contacts_str): 
    bazaopen = open("employees.csv", "a", encoding = 'utf-8')
    bazaopen.write(contacts_str + '\n')
    bazaopen.close()
    return
