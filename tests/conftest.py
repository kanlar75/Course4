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
                  'description': 'Создание технических требований для команды разработки и '
                                 'дизайна. Сопровождение задач по реализации фичей. Проведение '
                                 'исследований в рамках сервиса.',
                  'education': 'Понимание современных методологий управления. Знание основ UX. '
                               'Будет плюсом знание <highlighttext>Python</highlighttext> на '
                               'базовом или среднем уровне. Знание игрового рынка.',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'Junior Product Manager (Москва)',
                  'town': 'Москва',
                  'url': 'https://hh.ru/vacancy/81667513'},
                 {'currency': 0,
                  'description': 'Разрабатывать и поддерживать программные продукты. Искать '
                                 'оптимальные решения по разработке. Писать тесты. Писать '
                                 'техническую документацию.',
                  'education': '...тестов, а также понимание для чего они нужны. Знание или '
                               'готовность к обучению языков программирования на базовом '
                               'уровне: <highlighttext>Python</highlighttext>, Golang.',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'PHP-разработчик (Junior)',
                  'town': 'Казань',
                  'url': 'https://hh.ru/vacancy/82898757'},
                 {'currency': 0,
                  'description': 'Проведение прикладных исследований в направлениях '
                                 '“Industrial AI”, “AI for Education”, “AI & ESG”. Участие в '
                                 'совместных проектах с внутренними клиентами и...',
                  'education': 'Хорошее знание <highlighttext>Python</highlighttext> (в том '
                               'числе опыт работы с <highlighttext>Python</highlighttext>, ML '
                               'или DL frameworks (Pandas, NumPy, SciPy, PyTorch, Tensorflow '
                               'и...',
                  'experience': 'От 1 года до 3 лет',
                  'salary_from': 0,
                  'salary_to': 0,
                  'title': 'Data scientist в центр искусственного интеллекта',
                  'town': 'Владивосток',
                  'url': 'https://hh.ru/vacancy/83001332'},
                 {'currency': 'RUR',
                  'description': 'Изучение программных продуктов 1С. Моделирование '
                                 'бизнес-процессов предприятия. Составлять запросы, '
                                 'разрабатывать отчеты и печатные формы. Написание технической '
                                 'документации.',
                  'education': 'Знание основ алгоритмизации и программирования. Владение на '
                               'базовом уровне одним из современных языков программирования '
                               '(<highlighttext>Python</highlighttext>, Ruby, Java, C++, '
                               'etc). ',
                  'experience': 'Нет опыта',
                  'salary_from': 15000,
                  'salary_to': None,
                  'title': 'Стажер-аналитик 1С',
                  'town': 'Санкт-Петербург',
                  'url': 'https://hh.ru/vacancy/80483625'},
                 {'currency': 'RUR',
                  'description': 'Создание мобильных приложений. Шахматы. Программирование '
                                 'роботов. Программирование на Java. Базовая компьютерная '
                                 'подготовка, Азы программирования, Компьютерная графика и '
                                 'другие дисциплины <highlighttext>младших</highlighttext>...',
                  'education': 'Основы 3D моделирования. Программирование на '
                               '<highlighttext>Python</highlighttext> или основы '
                               'программирования на <highlighttext>Python</highlighttext>. '
                               'Опыт работы не требуется, возможно трудоустройство в том...',
                  'experience': 'Нет опыта',
                  'salary_from': 40000,
                  'salary_to': 50000,
                  'title': 'Педагог\xa0дополнительного\xa0образования\xa0(цифровые технологии, '
                           'информатика)',
                  'town': 'Санкт-Петербург',
                  'url': 'https://hh.ru/vacancy/80098005'}]
    return test_data


@pytest.fixture
def obj_vacancy1():
    obj_vac1 = Vacancy("Старший инженер-программист",
                       "https://hh.ru/vacancy/82963288", 450000, 0, "RUR",
                       "разработка и улучшение приложения pSeven Enterprise",
                       "ОАЭ",
                       "более 10 лет коммерческого опыта работы в командной "
                       "среде. - глубокие знания Python 3. - умение "
                       "создавать чистый, структурированный код с понятными...",
                       "Более 6 лет")
    return obj_vac1


@pytest.fixture
def obj_vacancy2():
    obj_vac2 = Vacancy("Python разработчик",
                       "https://hh.ru/vacancy/82963358", 55000, 100000, "RUR",
                       "разработка и улучшение приложения",
                       "Москва",
                       "более 5 лет коммерческого опыта работы в командной "
                       "среде. - глубокие знания Python 3. - умение "
                       "создавать чистый, структурированный код с понятными...",
                       "Более 6 лет")
    return obj_vac2


@pytest.fixture
def obj_vacancy3():
    obj_vac3 = Vacancy("Senior Python engineer",
                       "https://hh.ru/vacancy/82963288", 350000, 500000, "KZT",
                       "разработка и улучшение приложения pSeven Enterprise",
                       "Астана",
                       "более 10 лет коммерческого опыта работы в командной "
                       "среде. - глубокие знания Python 3. - умение "
                       "создавать чистый, структурированный код с понятными...",
                       "Более 6 лет")
    return obj_vac3


@pytest.fixture
def list_obj(obj_vacancy1, obj_vacancy2, obj_vacancy3):
    list_obj_vac = [obj_vacancy1, obj_vacancy2, obj_vacancy3]
    return list_obj_vac
