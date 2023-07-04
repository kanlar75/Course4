from src.utils import HeadHunterAPI, SuperJobAPI, Vacancy, JSONSaver


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями

    print('Привет!\n')
    vacancies_hh = HeadHunterAPI()
    vacancies_sj = SuperJobAPI()

    # Получение вакансий с разных платформ
    vacancy = input('Введите поисковый запрос:\n')
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
    input_top_number = int(input('Какое количество (не больше 500) самых '
                                 'высокооплачиваемых профессий показать?\n'))

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.save_vacancies(json_saver.json_exemplars(Vacancy.vac_list))

    # json_saver.get_vacancies("100 000-150 000 руб.")
    # json_saver.delete_vacancy(vacancy)
    #
    # # Функция для взаимодействия с пользователем
    # def user_interaction():
    #     platforms = ["HeadHunter", "SuperJob"]
    #     search_query = input("Введите поисковый запрос: ")
    #     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    #     filter_words = input(
    #         "Введите ключевые слова для фильтрации вакансий: ").split()
    #     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies,
    #                                           filter_words)
    #
    #     if not filtered_vacancies:
    #         print("Нет вакансий, соответствующих заданным критериям.")
    #         return
    #
    #     sorted_vacancies = sort_vacancies(filtered_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print_vacancies(top_vacancies)


if __name__ == '__main__':
    main()
