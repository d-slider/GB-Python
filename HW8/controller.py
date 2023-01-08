import logger
import view
import model

import os
clear = lambda: os.system('cls')


def show_main_menu():
    while True:
        menu_num = view.start()

        if menu_num == '1':
            result = logger.view_all_employee()
            clear()
            view.print_message(result)
        elif menu_num == '2':
            clear()
            model.enter_employee_record()
        elif menu_num == '3':
            clear()
            data = view.insert_data('Поиск работника: ')
            result3 = model.search_employee_record(data)
            view.print_message(result3)
        elif menu_num == '4':
            data = view.insert_data('Поиск работника, для удаления: ')
            clear()
            model.delete_employee(data)
        elif menu_num == '5':
            clear()
            break
            
        else:
            print("Ошибка, Введите [1 до 4]\n")