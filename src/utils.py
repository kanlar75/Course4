from abc import ABC, abstractmethod
import requests

class FindVacancies(ABC):

    @abstractmethod
    def get_vacancies(self, name):
        pass


class FileHandling(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, request):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class HeadHunterAPI(FindVacancies):

    url_ip = 'https://api.hh.ru/'
    headers = 'User-Agent: MyApp/1.0 (my-app-feedback@example.com)'

    def __init__(self, vacancy):
        self.vacancy = vacancy

    def get_vacancies(self, vacancy):
        base_url = 'https://hh.ru/search/vacancy?area=1&search_period=3&text=python&page=0'
        session = requests.Session()  # иммулирует действия одного пользователя, а не разные запросы
        request = session.get(base_url, headers=self.headers)



class SuperJobAPI(FindVacancies):

    def __init__(self, vacancy):
        self.vacancy = vacancy

    def get_vacancies(self, vacancy):
        pass


class Vacancy:

    vacancy_list = []

    def __init__(self, title, url, salary_from, salary_to, description,
                 requirements):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.requirements = requirements


class JSONSaver(FileHandling):

    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        pass

    def get_vacancies(self, request):
        pass

    def delete_vacancy(self, vacancy):
        pass
