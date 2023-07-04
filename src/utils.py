import json
import requests
import os
import fake_useragent
from abc import ABC, abstractmethod
from pprint import pprint

pages = 5
vacancies_on_page = 100


class FindVacancies(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass


class FileHandling(ABC):

    @abstractmethod
    def save_vacancies(self, list_dict):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, list_dict):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_str):
        pass


class HeadHunterAPI(FindVacancies):
    headers = {'user-agent': fake_useragent.UserAgent().random}
    params = {'per_page': vacancies_on_page, 'archive': False}

    def __init__(self):
        # self.data = data
        pass

    def get_vacancies(self, vacancy):
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
    API_TOKEN_SJ = 'v3.r.13773054.322adb5f53925517e4e5d74ec1b4ac2fc2fb5d21' \
                   '.643a11cd83b584cd8028edf34a0e6ef951dd8e1e'
    headers = {"X-Api-App-Id": API_TOKEN_SJ}
    params = {"count": vacancies_on_page}

    def __init__(self):
        self.vac = []

    def get_vacancies(self, vacancy):
        self.params['keyword'] = vacancy
        vac_list_sj = []
        for page in range(pages):
            data_sj = (requests.get("https://api.superjob.ru/2.0/vacancies/",
                                    params=self.params,
                                    headers=self.headers)).json()  # Запрос к API

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
        """ Инициализирует экземпляры класса Vacancy из отформатированного
        списка """

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

    # def __repr__(self): return (f"Vacancy(name={self.title}, salary_from={
    # self.salary_from}, " f"salary_to={self.salary_to},
    # " f"salary_currency={self.currency}, town={self.town}," f"experience={
    # self.experience}, url={self.url}")

    def __str__(self):
        return f'Вакансия: {self.title}\nСсылка на вакансию: {self.url}\n' \
               f'Зарплата от: ' \
               f'' \
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
        """ Возвращает True или False, сравнение по зарплате """

        if self.validate(other):
            return self.salary_from >= other.salary_from

    def validate(self, obj):
        """ Проверяет что зарплата в рублях """

        if self.currency and obj.currency in ["rub", "RUR"]:
            return True
        else:
            return False


class JSONSaver(FileHandling):

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

    @staticmethod
    def save_vacancies(list_dict, file_name='data.json'):
        """ Метод для загрузки списка словарей в JSON файл """

        with open(file_name, "w+", encoding="utf-8") as file:
            json.dump(list_dict, file, indent=2, ensure_ascii=False)

    def get_vacancies_town(self, find_str):
        Vacancy.vac_list = []
        find_list = []
        with open(self.file_name, 'r', encoding='utf8') as file:
            data_lst = json.load(file)
            for data in data_lst:
                if find_str in data.values():
                    find_list.append(data)
                else:
                    continue

        return find_list

    def get_vacancies_salary_max(self):
        Vacancy.vac_list = []
        find_list = []
        with open(self.file_name, 'r', encoding='utf8') as file:
            data_lst = json.load(file)
            for data in data_lst:
                if data['currency'] == 'RUR':
                    find_list.append(data)
                else:
                    continue
            find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        return find_list

    def get_vacancies_by_word(self, *args):
        Vacancy.vac_list = []
        find_list = []
        with open(self.file_name, 'r', encoding='utf8') as file:
            data_lst = json.load(file)
            for data in data_lst:
                for arg in args:
                    if arg in data['description']:
                        find_list.append(data)
                    else:
                        continue
            find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        return find_list

    def get_vacancies_by_salary(self, salary):
        """
        Метод для фильтрации вакансий из файла JSON по размеру зарплаты
        (минимальной)
        """
        Vacancy.vac_list = []
        find_list = []
        with open(self.file_name, "r", encoding="utf-8") as file:
            data_lst = json.load(file)
            find_list = []
            for data in data_lst:
                if data["salary_from"] <= int(salary) or data['currency'] \
                        != 'RUR':
                    continue
                else:
                    find_list.append(data)
            find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        return find_list

    def delete_vacancy(self, salary):
        find_list = []
        with open(self.file_name, 'r', encoding='utf8') as file:
            data_lst = json.load(file)
            for data in data_lst:
                if data['salary_from'] <= int(salary):
                    continue
                else:
                    find_list.append(data)
            find_list.sort(key=lambda lst_: lst_['salary_from'], reverse=True)
        return find_list



# vacancies_sj = SuperJobAPI()
# vacancies_hh = HeadHunterAPI()
# list_sj = vacancies_sj.get_vacancies('python')
# list_hh = vacancies_hh.get_vacancies('python')
# Vacancy.instantiate_from_data(list_hh)
# Vacancy.instantiate_from_data(list_sj)
# f = JSONSaver()
# f.save_vacancies(f.json_exemplars(Vacancy.vac_list))
# Vacancy.instantiate_from_data(f.delete_vacancy(45000))
# f.save_vacancies(f.json_exemplars(Vacancy.vac_list))
# for v in Vacancy.vac_list:
#     print(v)
