### Задание 1. Подключиться к БД через python

Необходимо научиться работать с БД через python  
Учебное видео [Как подключиться к MySQL на Python | MySQL создание таблицы, добавление, удаление, вывод данных](https://www.youtube.com/watch?v=LS42t1VMwuM)

1. Откройте `Git Bash` и (в домашнем каталоге пользователя) вызовите команду клонирования репозитория:
```
git clone <ссылка на репозиторий>
```
ссылка на репозиторий - скопируйте с [https://github.com/pythontoday/python_mysql_connection](https://github.com/pythontoday/python_mysql_connection)  
2. Откройте `pyCharm` и откройте проект клонированного с репозитория `python_mysql_connection` (через `File \ Open`)  
3. Настройте файл config.py
```
host = "127.0.0.1"
user = "root"
password = ""
db_name = "AnketaDB-IS221"
```
4. Установите библиотеку `pymysql`
```
в GitBash - перейдите в каталог проекта
    cd python_mysql_connection
и запустите установку библиотеки pymysql через менеджер пакетов pip
pip install pymysql
```
5. Запустите на выполнение файл `main.py`
```
successfully connected...
####################
####################
```
если указанное сообщение появится - значит соединение с БД установлено успешно!
