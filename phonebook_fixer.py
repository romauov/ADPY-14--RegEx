import re
import csv

def phonebook_fixer(raw_data, fixed_data):
    with open(raw_data, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

        names_pattern = r"^([\w]+)(\s)?([\w]+)?(\s)?([\w]+)?,([\w]+)?(\s)?([\w]+)?,([\w]+)?"
        names_regex = re.compile(names_pattern)

        phones_pattern = r"((\+7)|8)\s?\(?([\d]{3}?)(\)|\s|-)?\s?([\d]{3}?)(\s|-)?([\d]{2}?)(\s|-)?([\d]{2}?)(\s\(?(доб\.)?\s?([\d]*)\)?)?"
        phones_regex = re.compile(phones_pattern)

        contacts_list_fixed = []

        for contact in contacts_list:
            contact = ','.join(contact)

            contact = names_regex.sub(r"\1,\3\6,\5\8\9", contact)
            # исправили имена
            contact = phones_regex.sub(r"+7(\3)\5-\7-\9 \11\12", contact)
            # исправили телефоны
            contact = contact.split(',')

            contacts_list_fixed.append(contact)

    contacts = []
    for contact in contacts_list_fixed:
        entry = (contact[0], contact[1])
        contacts.append(entry)
    contacts = set(contacts)

    # итерируемся по сету
    # записываем повторяющиеся строки
    # складываем повторяющиеся строки
    # тут надеюсь есть более простое решение
    phone_book_fixed = []

    for entry in contacts:
        new_entry = ['', '', '', '', '', '', '']

        for contact in contacts_list_fixed:

            if entry[0] and entry[1] in contact:
                i = -1
                for field in contact:
                    i += 1
                    if new_entry[i] != contact[i]:
                        new_entry[i] += contact[i]

        phone_book_fixed.append(new_entry)
    phone_book_fixed.sort()

    with open(fixed_data, "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phone_book_fixed)
    return print(f'исходный файл {raw_data} исправлен и записан в {fixed_data}')