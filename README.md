## Проект автоматизациия сервиса itec для UI и API сервисов
***
## Установка
```
Установить python 3.11.9
```

Установить зависимости:
```
pip3 freeze > requirements.txt - сохранить зависимости
pip3 install -r requirements.txt - установить зависимости
```

Установить менеджер настроек Pydantic
```
pip install pydantic-settings - менеджер настроек pydantic
```

Установить асинхронный драйвер PostgreSQL для SqlAlchemy
```
pip install asyncpg

pip install greenlet
```

## Allure
#### Ubuntu
```
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure 
```
#### Windows
1. Скачать allure https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
2. Распаковать. bin папку добавить в переменную окружения
3. Чтобы запустить Allure, нужна среда выполнения Java — например, JRE или JDK. Проверить: java -version
4. После установки проверить allure: allure --version

Генерация отчета:
```
pytest tests.py --alluredir=allure_results 
```
Формирование отчета:
```
allure serve allure_results 
```

## Рекомендации

```
В файле .env не обрамляйте значения кавычками: код будет работать и с кавычками
, и без них, а вот при использовании Docker кавычки будут восприняты как часть
 значения, и это приведёт к ошибке.
```