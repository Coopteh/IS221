### Задание - установка MySQL WorkBench
1. Перейдите по ссылке и установите программу [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)
2. Запустите `MySQL WorkBench` и выберите построение ER-диаграмм (Диаграммы \ Add \ Add diagram)
3. Создайте таблицы
```
1. student
id int
first_name VARCHAR(45)
last_name VARCHAR(45)

2. course
id int
name VARCHAR(45)
description TEXT

3. module
id int
name VARCHAR(45)
```
4. Создайте связи между таблицами
```
1. Многие ко многим - между student и course
промежуточную таблицу назовите education

2. Один ко многим  - между course и module
```
