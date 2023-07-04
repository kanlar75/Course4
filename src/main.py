from src.utils import HeadHunterAPI, SuperJobAPI, Vacancy, JSONSaver


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями

    print('Привет!\n')
    vacancies_hh = HeadHunterAPI()
    vacancies_sj = SuperJobAPI()

    # Получение вакансий с разных платформ
    vacancy = input('Введите поисковый запрос (название вакансии):\n')
    input_platform = input(
        'Выберите платформу, с которой будем получать вакансии:\n1. '
        'SuperJob\n2. HeadHunter\n3. SuperJob и HeadHunter\n')
    if input_platform == '1':
        list_sj = vacancies_sj.get_vacancies(vacancy)
        Vacancy.instantiate_from_data(list_sj)
    elif input_platform == '2':
        list_hh = vacancies_hh.get_vacancies(vacancy)
        Vacancy.instantiate_from_data(list_hh)

    elif input_platform == '3':
        list_sj = vacancies_sj.get_vacancies(vacancy)
        list_hh = vacancies_hh.get_vacancies(vacancy)
        Vacancy.instantiate_from_data(list_sj)
        Vacancy.instantiate_from_data(list_hh)
    else:
        print('Нет такой платформы')

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.save_vacancies(json_saver.json_exemplars(Vacancy.vac_list))
    while True:
        user_chois = input(
            'Выберите что делать?:\n0. Вывести все вакансии\n1. Вывести топ '
            'вакансий по зарплате\n2. Отфильтровать вакансии по зарплате '
            'начиная с самой высокооплачиваемой\n3. Отфильтровать вакансии '
            'по городу\n4. Получить вакансии с зарплатой не ниже заданного '
            'уровня\n5. Вывести вакансии по ключевым словам\n6. Удалить '
            'вакансии у которых зарплата ниже заданного уровня\n7. '
            'Закончить\n')
        if user_chois == '0':
            for v in Vacancy.vac_list:
                print(v)
        elif user_chois == '1':
            input_top_number = int(input('Какое количество самых высокооплачиваемых '
                                 'вакансий показать?\n'))
            lst = json_saver.get_vacancies_salary_max()
            Vacancy.instantiate_from_data(lst)
            for i in range(input_top_number):
                print(Vacancy.vac_list[i])
        elif user_chois == '2':
            lst = json_saver.get_vacancies_salary_max()
            Vacancy.instantiate_from_data(lst)
            for v in Vacancy.vac_list:
                print(v)
        elif user_chois == '3':
            town = input('Введите город поиска:\n')
            lst = json_saver.get_vacancies_town(town)
            Vacancy.instantiate_from_data(lst)
            for v in Vacancy.vac_list:
                print(v)
        elif user_chois == '4':
            salary = input('Введите зарплату ниже которой вакансии не '
                           'выводить:\n')
            lst = json_saver.get_vacancies_by_salary(salary)
            Vacancy.instantiate_from_data(lst)
            for v in Vacancy.vac_list:
                print(v)
        elif user_chois == '5':
            filtered = input("Введите ключевые слова для поиска в "
                             "вакансиях (через пробел):\n ").split()
            find = ','.join(filtered)
            if not Vacancy.instantiate_from_data(
                    json_saver.get_vacancies_by_word(
                            find)):
                print("Нет вакансий, соответствующих заданным критериям.")
            else:
                for i in range(len(Vacancy.vac_list)):
                    print(Vacancy.vac_list[i])
        elif user_chois == '6':
            salary = input('Введите зарплату ниже которой вакансии '
                            'удалить:\n')
            lst = json_saver.delete_vacancy(int(salary))
            Vacancy.instantiate_from_data(lst)
            for v in Vacancy.vac_list:
                print(v)
        elif user_chois == '7':
            print("\033[1;34mУДАЧИ В ПОИСКЕ!\033[0m")
            exit()
        else:
            print('\033[1;31mНужно выбрать цифру из предложенных '
                  'вариантов!!!\033[0m')


if __name__ == '__main__':
    main()
