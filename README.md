### Задача 1. Обработка GET запроса

1. Откройте pyCharm
2. Создайте файл `get_name.py`
3. Установите компонент `Flask` - меню `File \ Settings \ Project:<название проекта> \ Python Interpreter \ Flask -> install`
```
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query')
def query_example():
    name = request.args.get('name')
    count = request.args.get('count')
    return f"Привет, {name}!"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
```
- Заставьте скрипт запускаться и обрабатывать данные по запросу в браузере
`http://127.0.0.1:5000/query?name=Ivan&count=5`  
- В зависимости от значения параметра count - добавляйте нужное количество восклицательных знаков `!`
```
0 - нет восклицательных - Привет, Иван
1 - 1 восклицательный - Привет, Иван!
5 - 5 восклицательных - Привет, Иван!!!!!
```

<hr>
    
### Задание 2. - Создание и обработка HTML формы (POST запрос)

Вы создадите простую HTML форму на веб-странице и напишите обработчик на сервере  
для получения и дальнейшей обработки данных, введенных пользователем в форму.

1. Откройте Visual Studio, откройте папку `Документы`
2. Создайте файл feedback.html, используя эммет `!` задайте html-структуру 
3. Создайте HTML форму на веб-странице, содержащую следующие элементы:
```
   - <input type="text"> для ввода имени.
   - <input type="email"> для ввода электронной почты.
   - <textarea> для ввода сообщения.
   - <select> с несколькими опциями (`<option>`)для выбора категории (Вопрос, Отзыв, Проблема).
   - Кнопка `<button type='submit'>` для отправки формы.
```
4. Напишите простой серверный скрипт (feedback.py) на PHP для обработки данных формы.
Серверный скрипт должен получить данные, отправленные из формы и вывести их на страницу.
```
from flask import Flask, request

app = Flask(__name__)

@app.route('/feedback.py', methods = ['POST'])
def do_form:
    if request.method == 'POST':
        choices = request.form.get('choices')
    else:
        # POST Error 405 Method Not Allowed

```
6. Отправьте данные через созданную форму, чтобы убедиться, что обработчик на сервере
корректно работает и может обрабатывать введенные данные.  

Запустите `Xamp Control \ Apache start` -> в браузере вызовите `localhost/feedback.php`

<hr>
   
### Задание 3. - Переключатели

Добавьте в форму чекбокс и радио-кнопки  
[checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)  
```
_ Согласен с передачей моих персональных данных
(галочка должна быть обязательно проставлена - атрибут required)
```
[radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio)  
```
Вто вы по профессии?
_ Рабочий
_ Колхозник
_ Студент
```
Прочитайте в серверном скрипте значения полей чекбокс и радио-кнопок  
- выведите выбранные значения на экран
