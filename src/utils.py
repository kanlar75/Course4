import json
import os
import fake_useragent
from abc import ABC, abstractmethod
from pprint import pprint

import requests

from src.json_saver import OperatingJSON

pages = 1
vacancies_on_page = 20


class FindVacancies(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass


class FileHandling(ABC):

    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


def instantiate_from_data_hh():
    """ Инициализирует экземпляры класса из данных HeadHunterAPI """
    with open('tempHH.json', 'r', encoding='utf8', ) as file:

        data_all = json.load(file)

        for data_hh in data_all:

            for j in range(len(data_hh['items'])):
                title = data_hh['items'][j]['name']
                url = data_hh['items'][j]['alternate_url']
                if data_hh['items'][j]['salary'] is not None:
                    salary_from = data_hh['items'][j]['salary']['from']
                    salary_to = data_hh['items'][j]['salary']['to']
                    currency = data_hh['items'][j]['salary'][
                        'currency']
                else:
                    salary_from = 0
                    salary_to = 0
                    currency = 'не указано'
                description = data_hh['items'][j]['snippet'][
                    'responsibility']
                town = data_hh['items'][j]['area']['name']
                education = data_hh['items'][j]['snippet']['requirement']
                experience = data_hh['items'][j]['experience']['name']
                Vacancy(title=title, url=url,
                        salary_from=salary_from,
                        salary_to=salary_to,
                        currency=currency,
                        description=description,
                        town=town,
                        education=education,
                        experience=experience
                        )


class HeadHunterAPI(FindVacancies):
    headers = {'user-agent': fake_useragent.UserAgent().random}
    params = {'per_page': vacancies_on_page}
    data = {}
    vac = []

    def __init__(self):
        pass

    def get_vacancies(self, vacancy):
        self.params['text'] = vacancy

        for i in range(pages):
            self.params['page'] = i
            self.data = (requests.get('https://api.hh.ru/vacancies',
                                      params=self.params,
                                      headers=self.headers)).json()
            self.vac.append(self.data)
        self.save_vacancies_temp()
        return self.vac

    def save_vacancies_temp(self):
        with open('tempHH.json', 'w', encoding='utf-8', ) as file:
            json.dump(self.vac, file, indent=2, ensure_ascii=False)


def instantiate_from_data_sj():
    """ Инициализирует экземпляры класса из данных SuperJobAPI """

    with open('tempSJ.json', 'r', encoding='utf8', ) as file:

        data_all = json.load(file)

        for data_sj in data_all:
            for j in range(len(data_sj['objects'])):
                title = data_sj['objects'][j]['profession']
                url = data_sj['objects'][j]['link']
                salary_from = data_sj['objects'][j]['payment_from']
                salary_to = data_sj['objects'][j]['payment_to']
                currency = data_sj['objects'][j]['currency']
                description = data_sj['objects'][j]['candidat']
                town = data_sj['objects'][j]['town']['title']
                education = data_sj['objects'][j]['education']['title']
                experience = data_sj['objects'][j]['experience']['title']
                Vacancy(title=title, url=url,
                        salary_from=salary_from,
                        salary_to=salary_to,
                        currency=currency,
                        description=description,
                        town=town,
                        education=education,
                        experience=experience
                        )


class SuperJobAPI(FindVacancies):
    # API_TOKEN_SJ = os.getenv('API_TOKEN_SJ')
    API_TOKEN_SJ = 'v3.r.13773054.322adb5f53925517e4e5d74ec1b4ac2fc2fb5d21' \
                   '.643a11cd83b584cd8028edf34a0e6ef951dd8e1e'
    headers = {"X-Api-App-Id": API_TOKEN_SJ}
    params = {"count": vacancies_on_page}
    data = {}

    def __init__(self):
        self.vac = []

    def get_vacancies(self, vacancy):
        self.params['keyword'] = vacancy
        for i in range(pages):
            self.params['page'] = i
            self.data = (requests.get("https://api.superjob.ru/2.0/vacancies/",
                                      params=self.params,
                                      headers=self.headers)).json()
            self.vac.append(self.data)
        self.save_vacancies_temp()
        return self.vac

    def save_vacancies_temp(self):
        with open('tempSJ.json', 'w', encoding='utf-8', ) as file:
            json.dump(self.vac, file, indent=2, ensure_ascii=False)


class Vacancy:
    vacancy_list = []

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
        self.currency = currency if currency else 'не указано'
        self.description = description if description else 'не указано'
        self.town = town if town else 'не указано'
        self.education = education if education else 'не указано'
        self.experience = experience if experience else 'не указано'
        self.vacancy_list.append(self)

    # def __repr__(self):
    #     return (f"Vacancy(name={self.title}, salary_from={self.salary_from}, "
    #             f"salary_to={self.salary_to}, "
    #             f"salary_currency={self.currency}, town={self.town},"
    #             f"experience={self.experience}, url={self.url}")

    def __str__(self):
        return f'Вакансия: {self.title}\nСсылка на вакансию: {self.url}\n' \
               f'Зарплата от: ' \
               f'' \
               f'{self.salary_from if self.salary_from != 0 else "не указано"}' \
               f' {self.currency if self.salary_from != 0 else ""}\n' \
               f'Зарплата до: ' \
               f'{self.salary_to if self.salary_to != 0 else "не указано"}' \
               f' {self.currency if self.salary_to != 0 else ""}\n' \
               f'Описание: {self.description}\nГород: {self.town}\n' \
               f'Требования: {self.education}\nОпыт: {self.experience}\n'

    def __eq__(self, other):
        """ Возвращает True или False (равенство зарплаты) """

        if self.validate(other):
            return self.salary_from == other.salary_from

    def __gt__(self, other):
        """ Возвращает True или False, сравнение по зарплате """

        if self.validate(other):
            return self.salary_from > other.salary_from

    def __ge__(self, other):
        """ Возвращает True или False, сравнение по зарплате """

        if self.validate(other):
            return self.salary_from >= other.salary_from

    @classmethod
    def validate(cls, obj):
        """ Проверяет что зарплата int. """
        if not isinstance(obj.salary_from, int):
            return False
        else:
            return True

    @classmethod
    def vacancies_sorted(cls):
        cls.vacancy_list.sort(key=lambda lst_: lst_.salary_from, reverse=True)
        return cls.vacancy_list

    def save(self):
        with open('temp.json', 'w', encoding='utf8') as file:
            json.dump(self.vacancy_list.__dict__, file, indent=2,
                      ensure_ascii=False)


class JSONSaver(FileHandling):

    def __init__(self):
        self.data_lst = None

    def add_vacancies(self, vacancy):
        with open('vacancies.json', 'a', encoding='utf8') as file:
            json.dump(vacancy.__dict__, file, indent=2, ensure_ascii=False)

    def get_vacancies(self, vacancy_salary):
        with open('temp.json', 'r', encoding='utf8') as f:
            self.data_lst = json.load(f)
            for vacancy in self.data_lst:
                if vacancy.salary_from >= vacancy_salary:
                    return vacancy
                else:
                    return f'Подходящих вакансий не найдено'

    def delete_vacancy(self, vacancy):
        pass


vacancies_sj = SuperJobAPI()
vacancies_hh = HeadHunterAPI()

vacancies_sj.get_vacancies('python')
vacancies_hh.get_vacancies('python')
instantiate_from_data_sj()
instantiate_from_data_hh()

vacancy1 = Vacancy.vacancy_list[0]
print(vacancy1)
#
vacancy2 = Vacancy.vacancy_list[1]

# print(vacancy2)
# print(len(Vacancy.vacancy_list))
# for i in range(500):
#     print(i, Vacancy.vacancy_list[i].salary_from)
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy1)
# json_saver.add_vacancy(vacancy2)
# with open('tempHH.json', 'r', encoding='utf8', ) as file:
#     data = json.load(file)[0]
#     for i in range(100):
#         pprint(data['items'][i]['name'])
# vacancies_list = Vacancy.vacancy_list
# vacancies_list.vacancies_sorted()
# print(vacancies_list[1])
file = OperatingJSON()
file.json_exemplars(Vacancy.vacancy_list)
