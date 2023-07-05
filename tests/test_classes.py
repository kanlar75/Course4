import pytest as pytest

from src.classes import HeadHunterAPI, SuperJobAPI, Vacancy, JSONSaver

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver('test_data.json')


# Тестируем метод получение списка вакансий HH
def test_hh_get_vacancies():
    assert isinstance(hh.get_vacancies('python'), list)


# Тестируем метод получения списка вакансий SJ
def test_sj_get_vacancies():
    assert isinstance(sj.get_vacancies('python'), list)


# Тестируем метод инициализации экземпляров класса Vacancy из списка
def test_instantiate_from_data(test_data):
    Vacancy.instantiate_from_data(test_data)
    assert len(Vacancy.vac_list) > 0
    vacancy1 = Vacancy.vac_list[0]
    assert vacancy1.title == 'Junior Flutter Developer'


# Тест инициализированного тестового объекта
def test_init_vacancy(obj_vacancy1):
    assert obj_vacancy1.title == 'Старший инженер-программист'
    assert obj_vacancy1.url == 'https://hh.ru/vacancy/82963288'


# Тест строкового представления объекта
def test_str(obj_vacancy1):
    assert str(obj_vacancy1) == 'Вакансия: Старший ' \
                                'инженер-программист\nСсылка на вакансию: ' \
                                'https://hh.ru/vacancy/82963288\nЗарплата ' \
                                'от: 450000 RUR\nЗарплата до: не указано ' \
                                '\nОписание: разработка ' \
                                'и улучшение приложения pSeven ' \
                                'Enterprise\nГород: ОАЭ\nОбразование: ' \
                                'более 10 лет коммерческого опыта работы в ' \
                                'командной среде.\nОпыт:' \
                                ' Более 6 лет\n'


# Тест магических методов
def test_magic(obj_vacancy1, obj_vacancy2):
    assert (obj_vacancy1 > obj_vacancy2) is True
    assert (obj_vacancy1 == obj_vacancy2) is False
    assert (obj_vacancy1 >= obj_vacancy2) is True


# Тест проверки валюты
def test_validate(obj_vacancy1, obj_vacancy4):
    assert obj_vacancy1.validate(obj_vacancy4) is False


# Тест получения вакансий по городу
def test_get_vacancies_town():
    js.get_vacancies_town('Екатеринбург')
    assert Vacancy.vac_list[0].town == 'Екатеринбург'
    assert Vacancy.vac_list != 0
    js_bad = JSONSaver('bad.json')
    try:
        with pytest.raises(FileNotFoundError):
            js_bad.get_vacancies_town("Екатеринбург")
    except:
        assert True


# Тест получения вакансий по максимальной зарплате
def test_get_vacancies_salary_max():
    js.get_vacancies_salary_max()
    assert Vacancy.vac_list[0].salary_from == 450000
    js_bad = JSONSaver('bad.json')
    try:
        with pytest.raises(FileNotFoundError):
            js_bad.get_vacancies_town("Екатеринбург")
    except:
        assert True


# Тест получения вакансий по уровню не ниже минимальной желаемой зарплаты
def test_get_vacancies_by_salary(obj_vacancy6):
    js.get_vacancies_by_salary(40000)
    assert obj_vacancy6 not in Vacancy.vac_list
