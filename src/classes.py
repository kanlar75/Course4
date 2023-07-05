import json
import requests
import fake_useragent
from abc import ABC, abstractmethod

# количество страниц для поиска
pages = 5
# число вакансий на странице
vacancies_on_page = 100


class FindVacancies(ABC):
    """ Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, vacancy):
        """ Абстрактный метод для получения вакансий по API """

    pass


class FileHandling(ABC):
    """ Абстрактный класс для работы с файлом """

    @abstractmethod
    def save_vacancies(self, list_dict):
        """ Абстрактный метод сохранения данных в файл """
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, list_dict):
        """ Абстрактный метод получения вакансий из файла (по зарплате) """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_str):
        """
        Абстрактный метод удаления вакансий из файла по уровню зарплаты
        ниже желаемой
        """
        pass


class HeadHunterAPI(FindVacancies):
    """ Класс для работы с вакансиями с HeadHunter """

    headers = {'user-agent': fake_useragent.UserAgent().random}
    params = {'per_page': vacancies_on_page, 'archive': False}

    def __init__(self):
        # self.data = data
        pass

    def get_vacancies(self, vacancy):
        """
        Получение нужных вакансий в формате списка словарей Python -
        работа с requests и JSON
        """

        self.params['text'] = vacancy
        vac_list_hh = []

        for page in range(pages):
            data_hh = requests.get('https://api.hh.ru/vacancies',
                                   params=self.params,
                                   headers=self.headers).json()  # Запрос к API
            for i in range(vacancies_on_page):
                vac_dict_hh = {'title': data_hh['items'][i]['name'],
                               'url': data_hh['items'][i]['alternate_url']}
                if data_hh['items'][i]['salary'] is not None:
                    vac_dict_hh['salary_from'] = data_hh['items'][i]['salary'][
                        'from']
                    vac_dict_hh['salary_to'] = data_hh['items'][i]['salary'][
                        'to']
                    vac_dict_hh['currency'] = data_hh['items'][i]['salary'][
                        'currency']
                else:
                    vac_dict_hh['salary_from'] = 0
                    vac_dict_hh['salary_to'] = 0
                    vac_dict_hh['currency'] = 0
                vac_dict_hh['description'] = data_hh['items'][i]['snippet'][
                    'responsibility']
                vac_dict_hh['town'] = data_hh['items'][i]['area']['name']
                vac_dict_hh['education'] = data_hh['items'][i]['snippet'][
                    'requirement']
                vac_dict_hh['experience'] = data_hh['items'][i]['experience'][
                    'name']
                vac_list_hh.append(vac_dict_hh)
        return vac_list_hh


class SuperJobAPI(FindVacancies):
    """ Класс для работы с вакансиями SuperJob """

    API_TOKEN_SJ = 'v3.r.13773054.322adb5f53925517e4e5d74ec1b4ac2fc2fb5d21' \
                   '.643a11cd83b584cd8028edf34a0e6ef951dd8e1e'
    headers = {"X-Api-App-Id": API_TOKEN_SJ}
    params = {"count": vacancies_on_page}

    def __init__(self):
        self.vac = []
        pass

    def get_vacancies(self, vacancy):
        """
        Получение нужных вакансий в формате списка словарей Python -
        работа с requests и JSON
        """

        self.params['keyword'] = vacancy
        vac_list_sj = []
        for page in range(pages):
            data_sj = (requests.get("https://api.superjob.ru/2.0/vacancies/",
                                    params=self.params,
                                    headers=self.headers)).json()
            for i in range(vacancies_on_page):
                vac_dict_sj = {'title': data_sj['objects'][i]['profession'],
                               'url': data_sj['objects'][i]['link'],
                               'salary_from': data_sj['objects'][i][
                                   'payment_from'],
                               'salary_to': data_sj['objects'][i][
                                   'payment_to'],
                               'currency': data_sj['objects'][i]['currency'],
                               'description': data_sj['objects'][i][
                                   'candidat'],
                               'town': data_sj['objects'][i]['town']['title'],
                               'education': data_sj['objects'][i][
                                   'education']['title'],
                               'experience': data_sj['objects'][i][
                                   'experience']['title']}
                vac_list_sj.append(vac_dict_sj)
            return vac_list_sj


class Vacancy:
    """  Класс для работы с вакансиями """

    vac_list = []
    data_list = []

    def __init__(self, title, url, salary_from, salary_to, currency,
                 description, town, education, experience):
        """
        Инициализация вакансии
        :param title: наименование вакансии
        :param url: ссылка
        :param salary_from: минимальная зарплата
        :param salary_to: максимальная зарплата
        :param currency: валюта зарплаты
        :param town: город
        :param education: образование
        :param experience: требуемый опыт

        """

        self.title = title if title else 'не указано'
        self.url = url if url else 'не указано'
        self.salary_from = salary_from if salary_from else 0
        self.salary_to = salary_to if salary_to else 0
        self.currency = 'RUR' if currency in ['RUR', 'rub'] else currency
        self.description = description if description else 'не указано'
        self.town = town if town else 'не указано'
        self.education = education if education else 'не указано'
        self.experience = experience if experience else 'не указано'
        self.vac_list.append(self)

    @classmethod
    def instantiate_from_data(cls, instantiate_list):
        """
        Инициализирует экземпляры класса Vacancy из отформатированного
        списка
        """

        cls.data_list = instantiate_list
        for data in cls.data_list:
            title = data['title']
            url = data['url']
            salary_from = data['salary_from'] if ['salary_from'] else 0
            salary_to = data['salary_to'] if ['salary_to'] else 0
            currency = data['currency'] if ['currency'] else 0
            description = data['description']
            town = data['town']
            education = data['education']
            experience = data['experience']
            Vacancy(title=title, url=url,
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                    description=description,
                    town=town,
                    education=education,
                    experience=experience
                    )

    # def __repr__(self):
    # """ Для разработчика """
    # return (f"Vacancy(name={
    # self.title}, salary_from={self.salary_from}, " f"salary_to={
    # self.salary_to}, salary_currency={self.currency}, " f"town={
    # self.town}, experience={self.experience}, " f"url={self.url}")

    def __str__(self):
        """ Строковое представление для пользователя """

        return f'Вакансия: {self.title}\nСсылка на вакансию: {self.url}\n' \
               f'Зарплата от: ' \
               f'{self.salary_from if self.salary_from != 0 else "не указано"}' \
               f' {self.currency if self.salary_from != 0 else ""}\n' \
               f'Зарплата до: ' \
               f'{self.salary_to if self.salary_to != 0 else "не указано"}' \
               f' {self.currency if self.salary_to != 0 else ""}\n' \
               f'Описание: {self.description}' \
               f'\nГород: {self.town}\n' \
               f'Образование: {self.education}\n' \
               f'Опыт: {self.experience}\n'

    def __eq__(self, other):
        """ Возвращает True или False (равенство минимальной зарплаты) """

        if self.validate(other):
            return self.salary_from == other.salary_from

    def __gt__(self, other):
        """ Возвращает True или False, сравнение по минимальной зарплате """

        if self.validate(other):
            return self.salary_from > other.salary_from

    def __ge__(self, other):
        """ Возвращает True или False, сравнение по минимальной зарплате """

        if self.validate(other):
            return self.salary_from >= other.salary_from

    def validate(self, obj):
        """ Проверяет что зарплата в рублях """

        if self.currency and obj.currency in ["rub", "RUR"]:
            return True
        else:
            return False


class JSONSaver(FileHandling):
    """ Класс для работы с файлом """
    def __init__(self, file_name='data.json'):
        self.file_name = file_name

    @staticmethod
    def json_exemplars(vac_obj_list) -> list[dict]:
        """
        Метод для конвертации списка вакансий из списка экземпляров класса
        в список словарей dict

        """
        list_dicts = []
        for obj in vac_obj_list:
            list_dicts.append(obj.__dict__)
        return list_dicts

    def save_vacancies(self, list_dict):
        """ Метод сохранения списка словарей в JSON файл """

        with open(self.file_name, "w+", encoding="utf-8") as file:
            json.dump(list_dict, file, indent=2, ensure_ascii=False)

    def get_vacancies_town(self, find_str):
        """ Метод для фильтрации вакансий из файла JSON по городу """

        Vacancy.vac_list = []
        find_list = []
        try:
            with open(self.file_name, 'r', encoding='utf8') as file:
                data_lst = json.load(file)
                for data in data_lst:
                    if find_str.lower() in data['town'].lower():
                        find_list.append(data)
                    else:
                        continue
        except FileNotFoundError:
            print("File not found")
        Vacancy.instantiate_from_data(find_list)

    def get_vacancies_salary_max(self):

        Vacancy.vac_list = []
        find_list = []
        try:
            with open(self.file_name, 'r', encoding='utf8') as file:
                data_lst = json.load(file)
                for data in data_lst:
                    if data['currency'] == 'RUR':
                        find_list.append(data)
                    else:
                        continue
                find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        except FileNotFoundError:
            print("File not found")
        Vacancy.instantiate_from_data(find_list)

    def get_vacancies_by_word(self, word_list):

        find_list = []
        try:
            with open(self.file_name, 'r', encoding='utf8') as file:
                data_lst = json.load(file)
                for data in data_lst:
                    for word in word_list:
                        if word.lower() in data['description'].lower() or word in \
                                data[
                                    'education'].lower() \
                                or word in data['experience'].lower():
                            find_list.append(data)
                    else:
                        continue
                find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        except FileNotFoundError:
            print("File not found")
        return find_list

    def get_vacancies_by_salary(self, salary):
        """
        Метод для фильтрации вакансий из файла JSON по размеру зарплаты
        (минимальной - salary_from)
        """

        Vacancy.vac_list = []
        find_list = []
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data_lst = json.load(file)
                for data in data_lst:
                    if data["salary_from"] <= int(salary) or data['currency'] \
                            != 'RUR':
                        continue
                    else:
                        find_list.append(data)
                find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        except FileNotFoundError:
            print("File not found")
        Vacancy.instantiate_from_data(find_list)

    def delete_vacancy(self, salary):
        """ Метод удаления вакансий с размером зарплаты ниже желаемой """

        Vacancy.vac_list = []
        find_list = []
        try:
            with open(self.file_name, 'r', encoding='utf8') as file:
                data_lst = json.load(file)
                for data in data_lst:
                    if data['salary_from'] <= int(salary):
                        continue
                    else:
                        find_list.append(data)
                find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        except FileNotFoundError:
            print("File not found")
        Vacancy.instantiate_from_data(find_list)
