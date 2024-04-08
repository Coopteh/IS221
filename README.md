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
### Задание 3. Выведите перемешанный список ответов

1. Используя шаблонированную строку `(f"")` - выведите вопрос как заголовок 3 уровня
2. Используйте цикл `for j in range(0,len(..))`для вывода списка ответов `qa_dict['answers']`
3. Используйте функцию `random.shuffle(..)` чтобы перемешать элементы списка в случайном порядке
4. Выведите полученный результат в браузер, запустив программу  
