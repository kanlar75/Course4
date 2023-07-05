from src.classes import HeadHunterAPI, SuperJobAPI, Vacancy, JSONSaver
from tests.conftest import test_data

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver('test_data.json')


# Тестируем метод получение списка вакансий HH
def test_hh_get_vacancies():
    assert isinstance(hh.get_vacancies('python'), list)

# Тестируем метод получения списка вакансий SJ
def test_sj_get_vacancies():
    assert isinstance(sj.get_vacancies('python'), list)


def test_instantiate_from_data(test_data):
    Vacancy.instantiate_from_data(test_data)
    assert len(Vacancy.vac_list) > 0


def test_init_vacancy(obj_vacancy1):
    assert obj_vacancy1.title == 'Старший инженер-программист'
    assert obj_vacancy1.url == 'https://hh.ru/vacancy/82963288'


def test_str(obj_vacancy1):
    assert str(obj_vacancy1) == 'Вакансия: Старший ' \
                                'инженер-программист\nСсылка на вакансию: ' \
                                'https://hh.ru/vacancy/82963288\nЗарплата ' \
                                'от: 450000 RUR\nЗарплата до: не указано ' \
                                '\nОписание: разработка ' \
                                'и улучшение приложения pSeven Enterprise\nГород: ОАЭ\nОбразование: ' \
                                'более 10 лет коммерческого опыта работы в ' \
                                'командной среде. - глубокие знания Python 3. - умение создавать чистый, ' \
                                'структурированный код с понятными...\nОпыт:' \
                                ' Более 6 лет\n'


def test_magic(obj_vacancy1, obj_vacancy2):
    assert (obj_vacancy1 > obj_vacancy2) is True
    assert (obj_vacancy1 == obj_vacancy2) is False
    assert (obj_vacancy1 >= obj_vacancy2) is True


def test_validate(obj_vacancy1, obj_vacancy3):
    assert obj_vacancy1.validate(obj_vacancy3) is False


def test_get_vacancies_town():
    js.get_vacancies_town('Новосибирск')
    assert len(Vacancy.vac_list) > 0
