import pytest as pytest

from src.classes import Vacancy


@pytest.fixture
def test_data():
    test_data = [{'currency': 'KZT',
                  'description': 'Разработка кросс-платформенных мобильных '
                                 'приложений на'
                                 'Flutter. Поддержка уже существующих '
                                 'приложений на Flutter.',
                  'education': 'Опыт разработки мобильных приложений на '
                               'Flutter от 1 года.'
                               'Знание систем контроля версий (git). Опыт '
                               'работы в команде'
                               '(Scrum, Kanban...',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 200000,
                  'salary_to': 300000,
                  'title': 'Junior Flutter Developer',
                  'town': 'Алматы',
                  'url': 'https://hh.ru/vacancy/81933558'},
                 {'currency': 'RUR',
                  'description': 'Создание чат-ботов. На курсе ученики '
                                 'создают собственных'
                                 'чат-ботов для Telegram и соцсетей с '
                                 'помощью no-code'
                                 'платформ. ',
                  'education': 'Языки программирования: '
                               '<highlighttext>Python</highlighttext>'
                               '(понимание ООП будет плюсом), С++, С#, JS и '
                               'другие. Имеете'
                               'опыт преподавания детям или готовы '
                               'развиваться в...',
                  'experience': 'Нет опыта',
                  'salary_from': None,
                  'salary_to': 130000,
                  'title': 'Преподаватель IT-дисциплин (младшая школа)',
                  'town': 'Москва',
                  'url': 'https://hh.ru/vacancy/81049446'},
                 {'currency': 0,
                  'description': 'Создание технических требований для '
                                 'команды разработки и'
                                 'дизайна. Сопровождение задач по реализации '
                                 'фичей. Проведение'
                                 'исследований в рамках сервиса.',
                  'education': 'Понимание современных методологий '
                               'управления. Знание основ UX.'
                               'Будет плюсом знание '
                               '<highlighttext>Python</highlighttext> на'
                               'базовом или среднем уровне. Знание игрового '
                               'рынка.',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'Junior Product Manager (Москва)',
                  'town': 'Москва',
                  'url': 'https://hh.ru/vacancy/81667513'},
                 {'currency': 0,
                  'description': 'Разрабатывать и поддерживать программные '
                                 'продукты. Искать'
                                 'оптимальные решения по разработке. Писать '
                                 'тесты. Писать'
                                 'техническую документацию.',
                  'education': '...тестов, а также понимание для чего они '
                               'нужны. Знание или'
                               'готовность к обучению языков '
                               'программирования на базовом'
                               'уровне: <highlighttext>Python</highlighttext'
                               '>, Golang.',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'PHP-разработчик (Junior)',
                  'town': 'Казань',
                  'url': 'https://hh.ru/vacancy/82898757'},
                 {'currency': 0,
                  'description': 'Проведение прикладных исследований в '
                                 'направлениях'
                                 '“Industrial AI”, “AI for Education”, “AI & '
                                 'ESG”. Участие в'
                                 'совместных проектах с внутренними '
                                 'клиентами и...',
                  'education': 'Хорошее знание '
                               '<highlighttext>Python</highlighttext> (в том'
                               'числе опыт работы с '
                               '<highlighttext>Python</highlighttext>, ML'
                               'или DL frameworks (Pandas, NumPy, SciPy, '
                               'PyTorch, Tensorflow'
                               'и...',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'Data scientist в центр искусственного интеллекта',
                  'town': 'Владивосток',
                  'url': 'https://hh.ru/vacancy/83001332'},
                 {'currency': 'RUR',
                  'description': 'Изучение программных продуктов 1С. '
                                 'Моделирование'
                                 'бизнес-процессов предприятия. Составлять '
                                 'запросы,'
                                 'разрабатывать отчеты и печатные формы. '
                                 'Написание технической'
                                 'документации.',
                  'education': 'Знание основ алгоритмизации и '
                               'программирования. Владение на'
                               'базовом уровне одним из современных языков '
                               'программирования'
                               '(<highlighttext>Python</highlighttext>, '
                               'Ruby, Java, C++,'
                               'etc). ',
                  'experience': 'Нет опыта',
                  'salary_from': 15000,
                  'salary_to': None,
                  'title': 'Стажер-аналитик 1С',
                  'town': 'Санкт-Петербург',
                  'url': 'https://hh.ru/vacancy/80483625'},
                 {'currency': 'RUR',
                  'description': 'Создание мобильных приложений. Шахматы. '
                                 'Программирование'
                                 'роботов. Программирование на Java. Базовая '
                                 'компьютерная'
                                 'подготовка, Азы программирования, '
                                 'Компьютерная графика и'
                                 'другие дисциплины '
                                 '<highlighttext>младших</highlighttext>...',
                  'education': 'Основы 3D моделирования. Программирование на '
                               '<highlighttext>Python</highlighttext> или '
                               'основы'
                               'программирования на '
                               '<highlighttext>Python</highlighttext>.'
                               'Опыт работы не требуется, возможно '
                               'трудоустройство в том...',
                  'experience': 'Нет опыта',
                  'salary_from': 40000,
                  'salary_to': 50000,
                  'title': 'Педагог\xa0дополнительного\xa0образования\xa0('
                           'цифровые технологии,'
                           'информатика)',
                  'town': 'Санкт-Петербург',
                  'url': 'https://hh.ru/vacancy/80098005'}]
    return test_data


# obj_vac1 - obj_vac6 тестовые объекты класса Vacancy
@pytest.fixture
def obj_vacancy1():
    obj_vac1 = Vacancy("Старший инженер-программист",
                       "https://hh.ru/vacancy/82963288", 450000, 0, "RUR",
                       "разработка и улучшение приложения pSeven Enterprise",
                       "ОАЭ",
                       "более 10 лет коммерческого опыта работы в командной "
                       "среде.",
                       "Более 6 лет")
    return obj_vac1


@pytest.fixture
def obj_vacancy2():
    obj_vac2 = Vacancy("Junior Программист/Разработчик Python",
                       "https://hh.ru/vacancy/82392679", 60000, 0, "RUR",
                       "Разработка, тестирование, отладка и поддержка "
                       "кросс-платформенных (x86/ARM) приложений",
                       "Новосибирск",
                       "Знание английского языка достаточное для чтения "
                       "технической документации.",
                       "От 1 года до 3 лет")
    return obj_vac2


@pytest.fixture
def obj_vacancy3():
    obj_vac3 = Vacancy("Программист Python Junior (BigData)",
                       "https://hh.ru/vacancy/82524858", 45000, 100000, "RUR",
                       "Обеспечивать работоспособность и доступность "
                       "бизнес-систем компании.",
                       "Екатеринбург",
                       "Высшее образование (можно неоконченное/неполное) "
                       "технического ВУЗа.",
                       "Нет опыта")
    return obj_vac3


@pytest.fixture
def obj_vacancy4():
    obj_vac4 = Vacancy("Разработчик Python",
                       "https://hh.ru/vacancy/82822848", 450000, 590000, "KZT",
                       "Внедрение автоматизации и цифровизации.",
                       "Алматы",
                       "Высшее образование (можно неоконченное/неполное)",
                       "Опыт программирования на Python. Знания СУБД "
                       "PostgreSQL.")
    return obj_vac4


@pytest.fixture()
def obj_vacancy5():
    obj_vac5 = Vacancy("Junior Python - Developer",
                       "https://hh.ru/vacancy/82585620", 61000, 70000, "RUR",
                       "Поддержка текущего кода генератора.",
                       "Москва",
                       "Понимание того, что такое Ffmpeg. Умение писать "
                       "Bash-команды.",
                       "От 1 года до 3 лет")
    return obj_vac5


@pytest.fixture()
def obj_vacancy6():
    obj_vac6 = Vacancy("Начинающий программист (стажер)",
                       "https://hh.ru/vacancy/82868479", 30000, 0, "RUR",
                       "Участие в работе с обработкой потоковых данных.",
                       "Новосибирск",
                       "Python. Postgres, ClickHouse.",
                       "Нет опыта")
    return obj_vac6


# Список экземпляров класса Vacancy
@pytest.fixture
def list_obj(obj_vacancy1, obj_vacancy2, obj_vacancy3, obj_vacancy4):
    list_obj_vac = [obj_vacancy1, obj_vacancy2, obj_vacancy3]
    return list_obj_vac

# # Временный файл json для тестов, возможно не пригодится
# @pytest.fixture(scope='module')
# def temp_file_json(tmpdir_factory):
#     """
#     Записываем тестовые данные в файл 'test_data.json' во временной
#     директории.
#     """
#     temp_data = [
#         {
#             "title": "Программист Python Junior (BigData)",
#             "url": "https://hh.ru/vacancy/82524858",
#             "salary_from": 45000,
#             "salary_to": 100000,
#             "currency": "RUR",
#             "description": "Обеспечивать работоспособность и доступность "
#                            "бизнес-систем компании. Управлять конфигурациями "
#                            "и микросервисами. Находить не тривиальные "
#                            "решения. Быть \"белыми хакерами\" всегда "
#                            "решать...",
#             "town": "Екатеринбург",
#             "education": "Высшее образование (можно неоконченное/неполное) "
#                          "технического ВУЗа (с курсов по "
#                          "<highlighttext>Python</highlighttext> не "
#                          "принимаем). Логичный и структурированный подход к "
#                          "решению задач...",
#             "experience": "Нет опыта"
#         },
#         {
#             "title": "Junior Программист/Разработчик Python",
#             "url": "https://hh.ru/vacancy/82392679",
#             "salary_from": 60000,
#             "salary_to": 0,
#             "currency": "RUR",
#             "description": "Разработка, тестирование, отладка и поддержка "
#                            "кросс-платформенных (x86/ARM) приложений на "
#                            "<highlighttext>Python</highlighttext>.",
#             "town": "Новосибирск",
#             "education": "Знание английского языка достаточное для чтения "
#                          "технической документации. Опыт разработки "
#                          "приложений на "
#                          "<highlighttext>Python</highlighttext>/Qt/C++/C#. "
#                          "Желателен опыт работы с.",
#             "experience": "От 1 года до 3 лет"
#         },
#         {
#             "title": "Разработчик Python",
#             "url": "https://hh.ru/vacancy/82822848",
#             "salary_from": 450000,
#             "salary_to": 590000,
#             "currency": "KZT",
#             "description": "Внедрение автоматизации и цифровизации. "
#                            "Разработка ERP системы на платформе Odoo. Анализ "
#                            "потребностей, разработка и внедрение новых "
#                            "процессов.",
#             "town": "Алматы",
#             "education": "Опыт программирования на "
#                          "<highlighttext>Python</highlighttext>. Знания СУБД "
#                          "PostgreSQL. Опыт работы с django или другим "
#                          "<highlighttext>python</highlighttext> web "
#                          "framework. Знание основ HTML, CSS. ",
#             "experience": "От 1 года до 3 лет"
#         },
#         {
#             "title": "Junior Python - Developer",
#             "url": "https://hh.ru/vacancy/82585620",
#             "salary_from": 61000,
#             "salary_to": 70000,
#             "currency": "RUR",
#             "description": "Поддержка текущего кода генератора. Создание "
#                            "новых креативов по инструкции (Т/З).",
#             "town": "Москва",
#             "education": "Понимание того, что такое Ffmpeg. Умение писать "
#                          "Bash-команды. Представление того, что такое s3 и "
#                          "как туда загружать файл.",
#             "experience": "От 1 года до 3 лет"
#         },
#         {
#             "title": "Начинающий программист (стажер)",
#             "url": "https://hh.ru/vacancy/82868479",
#             "salary_from": 30000,
#             "salary_to": 0,
#             "currency": "RUR",
#             "description": "Участие в работе с обработкой потоковых данных. "
#                            "Разработка end point. Парсинг данных. Сбор "
#                            "данных по API.",
#             "town": "Новосибирск",
#             "education": "<highlighttext>Python</highlighttext>. Postgres, "
#                          "ClickHouse. Возможность работать с распределений "
#                          "командой. Знания ООП. Высшее / неоконченное высшее "
#                          "(последний курс) техническое образование. Желание "
#                          "развиваться в...",
#             "experience": "Нет опыта"
#         }
#     ]
#     file = tmpdir_factory.mktemp('data').join('test_data.json')
#
#     with file.open('w') as f:
#         json.dump(temp_data, f)
#     return file
