### Задание 1. Чтение списка вопросов-ответов из файла 

1. Откройте `pyCharm` и создайте новый файл `read_qa.py`
2. Создайте файл `qa.txt` в той же директории, следующего содержания
```
Сколько звезд на небе?
3
Не сосчитать
Миллион
Два миллиона
```
3. Напишите на python программу `qa.py`, которая
```
// TODO
Считать из файла (qa.txt) строки:
  1 строка - это вопрос (question)
  2 строка - число ответов (answers)
  3 и далее - сами ответы
Записать в структуру данных типа словарь, где
  - по ключу 'question' - хранится вопрос
  - по ключу 'answers' - хранится список ответов
Выдать на экран содержимое получившегося словаря

qa_dict = {}

with open('qa.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

qa_dict['question'] = lines[0].strip()
num_answers = int(lines[1])
qa_dict['answers'] = [line.strip() for line in lines[2:2+num_answers]]

print(qa_dict)
```
<hr>

### Задание 2. Добавим веб-страницу
1. Используем Flask - добавьте первой строчкой
```
from flask import Flask, request, render_template
```
2. Запуск веб-сервера
```
# create the Flask app
app = Flask(__name__)

@app.route('/')
def get_qa():
    return qa_dict['question']

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=False, port=5000)
```
<hr>

### Задание 3. Выведите перемешанный список ответов

1. Используя шаблонированную строку `(f"")` - выведите вопрос как заголовок 3 уровня
2. Сделайте присвоение `list_answers` (после `print(qa_dict)`) и сделайте копирование элементов списка ответов в новый список 
`list_answers = qa_dict['answers'].copy()`
3. Используйте функцию `random.shuffle(..)` чтобы перемешать элементы списка в случайном порядке
`random.shuffle( list_answers )`
4. Используйте цикл `for j in range(0,len(..))`для вывода списка ответов `list_answers[j]`
в виде нумерованного списка (теги `<ol></ol>`, для элементов внутри списка - теги `<li></li>`) 
5. Выведите полученный результат в браузер, запустив программу
<hr>

### Задание 4. Форма ввода правильного ответа

1. Добавьте форму ввода - строка для ввода правильного ответа
(input c name="result") и кнопки `Отправить`
```
Введите номер правильного ответа:  4
| Отправить |

<form action="/result" method="POST">..</form>
```
2. Переместите `list_answers` в начало кода (после `print`) и сделайте копирование  
`list_answers = qa_dict['answers'].copy()` 
4. Обработайте данные ответа - выдайте на экран браузера:  
`Это правильный ответ!` - в случае правильного ответа  
`Неверный ответ` - в случае неправильного ответа  
```
@app.route('/result', methods=['POST'])
def check_result():
@app.route('/result', methods=['POST'])
def check_result():
    if request.method == 'POST':
        num = int(request.form.get('result'))
        choise = list_answers[num-1]
        qa_1 = qa_dict['answers'][0]
        if (choise == qa_1):
            return "<center><h2>Это правильный ответ!</h2></center>"
        else:
            return "<center><h2>Неверный ответ..</h2></center>"
    return "Error"
```
