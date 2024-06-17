## Проект автоматизациия сервиса itec для UI и API сервисов
***
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
Зависимости:
```
pip3 freeze > requirements.txt - сохранить зависимости
pip3 install -r requirements.txt - установить зависимости

pip install pydantic-settings
```