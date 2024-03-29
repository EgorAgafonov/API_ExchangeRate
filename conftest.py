import sys
import pytest
from datetime import *
from settings import *
from colorama import Style, Back, Fore

filename = 'logs/logs.txt'


@pytest.fixture(scope='class')
def duration_of_collection(request, filename=filename):
    start_time = datetime.now()
    print(f'\n1/3 START COLLECTION:\nНачало выполнения тестовой коллекции: {start_time} сек.')
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'w') as file_object:
        file_object.write(f'1/3 START COLLECTION:\nНачало выполнения тестовой коллекции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'2/3 END COLLECTION:\nОкончание выполнения тестовой коллекции: {end_time} сек.\n')
    print(f"3/3 RESULT:\nОбщая продолжительность всех тестов в коллекции {request.cls}: {end_time - start_time} "
          f"сек.\n\n\n")
    with open(filename, 'a') as file_object:
        file_object.write(f'\n2/3 END COLLECTION:\nОкончание выполнения тестовой коллекции: {end_time} сек.\n')
        file_object.write(f"\n3/3 RESULT:\nОбщая продолжительность всех тестов в коллекции {request.cls}: "
                          f"{end_time - start_time} сек.\n\n\n")


@pytest.fixture(scope='function')
def duration_of_test(request):
    start_time = datetime.now()
    print(Fore.BLACK + Style.DIM + Back.WHITE + f'<Начало выполнения тестовой функции: {start_time} сек.>')
    yield
    end_time = datetime.now()
    print(Fore.BLACK + Style.DIM + Back.WHITE + f'>Окончание выполнения тестовой функции: {end_time} сек.<')
    print(Fore.BLACK + Style.DIM + Back.YELLOW + f"ВСЕГО продолжительность теста {request.function.__name__}: "
                                                 f"{end_time - start_time} сек.")
    print(Fore.RESET + Style.RESET_ALL + Back.RESET + f"\n")


@pytest.fixture(scope='function')
def introspection_of_test(request):
    yield
    print(f'\n- Имя теста (тестируемой функции): {request.function.__name__};')
    print(f'- Имя коллекции (тестового класса): {request.cls};')
    print(f'- Имя фикстуры: {request.fixturename};')
    print(f'- Область видимости фикстуры: {request.scope}.')
    print(f'- Относительный путь к тестовому модулю: {request.module.__name__};')
    print(f'- Абсолютный путь к тестовому модулю: {request.fspath};')
    if request.cls:
        return f"\n У теста(тестируемой функции) {request.function.__name__} есть коллекция (тестовый класс).\n"
    else:
        return f"\n У теста(тестируемой функции) {request.function.__name__} коллекция (тестовый класс) отсутствует.\n"


@pytest.fixture(scope='function', autouse=True)
def log_of_test(request, filename='logs/logs.txt'):
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'a') as file_object:
        file_object.write(f'\nНачало выполнения тестовой функции: {start_time} сек. *')
        file_object.write(f'\n- Имя теста (тестируемой функции): {request.function.__name__}.')
        file_object.write(f'\n- Имя коллекции (тестового класса): {request.cls}.')
        file_object.write(f'\n- Имя фикстуры: {request.fixturename}.')
        file_object.write(f'\n- Область видимости фикстуры: {request.scope}.')
        file_object.write(f'\n- Относительный путь к тестовому модулю: {request.module.__name__}.')
        file_object.write(f'\nОкончание выполнения тестовой функции: {end_time} сек. **')
        file_object.write(f"\nИТОГО продолжительность теста {request.function.__name__}: "
                          f"{end_time - start_time} сек.\n\n")


min_python_310_required = pytest.mark.skipif(sys.version_info > (3, 9), reason='Тест требует python версии 3.9 или '
                                                                               'ниже, выполнение теста отложено.')


def strings_generator(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def digits():
    return '1234567890'


def latin_chars():
    return 'abcdefghijklmnopqrstwxyz'
