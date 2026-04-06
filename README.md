## Консультация перед экзаменом по МДК 07.01 Управление и автоматизация БД

Практическое задание
```
1.	Для работы вам понадобится база данных - создайте ее запустив XAMPP и phpMyAdmin. Имя базы данных 'exam01', создайте тестовую таблицу 'test' с полями (id int, name varchar(100)) и добавьте 1 запись в таблицу (1, 'Билет 1')
2.	Запустите 'cmd' в папке 'c:/xampp/mysql/bin', в открывшейся командной строке запустите:
mysql -u root -p
3.	В интерактивном режиме создайте пользователя 'admin_user'@'localhost' в базе данных exam01 c паролем 'admin'.
CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'admin';
Назначьте ему все права на все таблицы базы данных exam01, предоставив права на любые операции с базой данных.
GRANT ALL PRIVILEGES ON exam01.* TO 'admin_user'@'localhost';
4.	Закончите сеанс под root-пользователем, запустив команду exit
5.	Выполните резервное копирование базы данных exam01 в файл backup_exam01.sql
mysqldump -u admin_user -p exam01 > backup_exam01.sql
6.	Зайдите в mysql под пользователем 'admin_user' и удалите таблицу 'test' в базе данных exam01
DROP TABLE `test`;
7.	Выполнение восстановление от пользователя 'admin_user' базы данных exam01 из резервной копии backup_exam01.sql
mysql -u admin_user -p exam01 < backup_exam01.sql
```
