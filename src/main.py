import os

from src.classes import HeadHunterAPI, SuperJobAPI, Vacancy
from src.utils import user_work_with_file


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    print('Привет!\n')
    vacancies_hh = HeadHunterAPI()
    vacancies_sj = SuperJobAPI()

    # Если файл с вакансиями существует, предлагаем 2 режима работы
    if os.path.exists('data.json'):
        working_mode = input("1. Получить новые вакансии\n2. Работать с "
                             "файлом\n").strip()
    else:
        working_mode = '1'
    if working_mode == '1':

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
            print('\033[1;31mНужно выбрать цифру из предложенных '
                  'вариантов!!!\033[0m')

    # Работа с файлом
    user_work_with_file()


if __name__ == '__main__':
    main()
