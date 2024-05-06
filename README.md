### Задание 1. Получить ответ от Чак Норриса

Откройте `pyCharm` и создайте новый файл `chuck.py`  
URL [https://api.chucknorris.io/](https://api.chucknorris.io/jokes/random)   
Учебное видео (1): [Автоматизация на Python для начинающих с нуля. 1 урок](https://www.youtube.com/watch?v=udREFJ7qPlA&list=PLbuh2pN46AEtSlQdsVn4krLki8Cte7x1S&index=2)  
```
Импортируйте библиотеку request
сделайте GET-запрос по указанному выше урл
получите ответ и выведите в консоль result.text и result.status_code
```

### Задание 1. Оформим через класс и сделаем проверки

Учебное видео (2): [Автоматизация на Python для начинающих с нуля. 2 урок](https://www.youtube.com/watch?v=deWtCq9Kz5g&list=PLbuh2pN46AEtSlQdsVn4krLki8Cte7x1S&index=2)  
```
Создайте класс Test_new_joke
и поместите код с предыдущего занятия в метод
def test_create_random_joke(self):

Сохраните ответ в json формате в переменную check
check = result.json()
Проверьте есть ли строка "Norris" в поле "value" указанного объекта
получить значение можно через check.get('value')
```
