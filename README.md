Набор тестов на базе библиотеки requests и фреймворка Pytest для 
функционального тестирования REST API сервиса платформы 
https://www.exchangerate-api.com (ExchangeRate-API).


Cтруктура проекта представлена:
1) папкой tests c двумя модулями, содержащими коллекции позитивных и негативных тестов;
2) модулем exchange_app.py, содержащим класс с методами отправки запросов на API сервис ExchangeRate-API;
3) папкой logs, хранящей артефакты результатов тестирования.
4) папкой diagram c диаграммой негативных сценариев тестирования GET-запроса Standard ExchangeRate-API. 

В корневой папке проекта содержатся: модули settings.py и conftest.py с необходимыми тестовыми данными и 
фикстурами Pytest для запуска тестов; текстовый файл requirements.txt c указанными требованиями к проекту.  

Каждый тест и класс в модулях содержат подробную аннотацию к выполняемому коду.

Агафонов Е.А., 2023 г.
