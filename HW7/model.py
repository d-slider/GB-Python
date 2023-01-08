def search_contact(base, contact):
    base = base.split('\n')
    flag = True
    result = []
    for i in base:
        if contact in i:
            flag = True
            result.append(i)
    if not flag:
        result.append(f'Контакт {contact} не найден')
    return result