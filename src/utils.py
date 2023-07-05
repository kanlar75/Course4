from src.classes import Vacancy, JSONSaver


def print_info():
    """ Выводит информацию о подготовленных вакансиях """

    for v in Vacancy.vac_list:
        print(v)


def user_work_with_file():
    """ Функция взаимодействия с пользователем (работа с файлом) """

    json_saver = JSONSaver()
    json_saver.save_vacancies(json_saver.json_exemplars(Vacancy.vac_list))
    while True:
        user_choice = input(
            'Выберите что делать?:\n0. Вывести все вакансии\n1. Вывести топ '
            'вакансий по зарплате\n2. Отфильтровать вакансии по зарплате '
            'начиная с самой высокооплачиваемой\n3. Отфильтровать вакансии '
            'по городу\n4. Получить вакансии с зарплатой не ниже заданного '
            'уровня\n5. Вывести вакансии по ключевым словам\n6. Удалить '
            'вакансии у которых зарплата ниже заданного уровня\n7. '
            'Закончить\n').strip()
        if user_choice == '7':
            print("\033[1;34mУДАЧИ В ПОИСКЕ!\033[0m")
            exit()
        elif user_choice == '0':
            print_info()
        elif user_choice == '1':
            input_top_number = int(input('Какое количество самых '
                                         'высокооплачиваемых'
                                         'вакансий показать?\n').strip())
            json_saver.get_vacancies_salary_max()
            for i in range(input_top_number):
                print(Vacancy.vac_list[i])
        elif user_choice == '2':
            json_saver.get_vacancies_salary_max()
            print_info()
        elif user_choice == '3':
            town = input('Введите город поиска:\n').strip().lower()
            json_saver.get_vacancies_town(town)
            print_info()
            user_answer = input('Сохранить результат в новый файл?\n1. ДА\n2. '
                                'НЕТ\n').strip()
            if user_answer == '1':
                new_file = JSONSaver('data_town.json')
                new_file.save_vacancies(
                    new_file.json_exemplars(Vacancy.vac_list))
        elif user_choice == '4':
            salary = int(input('Введите зарплату ниже которой вакансии не '
                               'выводить:\n').strip())
            json_saver.get_vacancies_by_salary(salary)
            print_info()
        elif user_choice == '5':
            filtered = list(
                map(str, input("Введите ключевые слова для поиска в "
                               "вакансиях (через пробел)\n").split()))
            words = tuple(filtered)
            Vacancy.instantiate_from_data(json_saver.get_vacancies_by_word(
                words))
            if not json_saver.get_vacancies_by_word(words):
                print("\033[1;31mНет вакансий, соответствующих заданным "
                      "критериям.\033[0m")
            else:
                print_info()
                user_answer = input('Заменить результаты в файле?\n1. ДА\n2. '
                                    'НЕТ\n').strip()
                if user_answer == '1':
                    json_saver.save_vacancies(
                        json_saver.json_exemplars(Vacancy.vac_list))
        elif user_choice == '6':
            salary = int(input('Введите зарплату ниже которой вакансии '
                               'удалить:\n').strip())
            json_saver.delete_vacancy(salary)
            print_info()
            user_answer = input('Сохранить результат в новый файл?\n1. ДА\n2. '
                                'НЕТ\n').strip()
            if user_answer == '1':
                new_file = JSONSaver('data_higher_salary.json')
                new_file.save_vacancies(
                    new_file.json_exemplars(Vacancy.vac_list))
        else:
            print('\033[1;31mНужно выбрать цифру из предложенных '
                  'вариантов!!!\033[0m')
