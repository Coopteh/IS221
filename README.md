### Задача 1. "Сообщения в чате"

Используйте сайт [programiz.com](https://www.programiz.com/javascript/online-compiler/)

Задача 1

Вы с другом обменивается сообщениями в чате.  
Первое сообщение отправляет Друг, второе — Вы и так далее.  
Выведите беседу в хронологическом порядке.   
```
Пример переписки:

    Вы: Привет!
    Друг: Здорово, коль не шутишь!
```
Шаги по решению задачи:
- Инициализируйте массив сообщений.
- Заполните его следующими данными:
```
        "Пойдем гулять в парк?",
        "Кажется, дождь собирается. Лучше пойдем в кино!",
        "Давай, сегодня как раз вышел новый фильм.",
        "Встречаемся через час у кинотеатра."
```
- Напишите цикл для вывода сообщений.  
(в зависимости от номера сообщения нужно подставлять в начало сообщения либо “Друг”, либо “Вы”)

### Задача 2. 

Нужно добавить функцию поиска по тексту сообщений в нашем мессенджере.

Например, пользователь ищет слово “кино”, и ему отображаются все сообщения с таким текстом.
Шаги по решению задачи:

    Инициализируйте переменную, в которой будет храниться искомый текст. Например, слово “кино”.
    Для поиска воспользуйтесь методом includes для строки.

Пример использования метода для поиска слова “зелёный” в строке “чёрный чай”:

"Чёрный чай".includes("зелёный"); // вернёт false

Метод возвращает true, если слово есть в строке, и false, если нет.

    Напечатайте списком все сообщения, в которых есть искомая строка.

Инструкция по выполнению домашнего задания

    Зарегистрируйтесь на сайте Repl.IT.
    Перейдите в раздел my repls.
    Нажмите кнопку Start coding now!, если приступаете впервые, или New Repl, если у вас уже есть работы.
    В списке языков выберите Nodejs.
    Код пишите в левой части окна.
    Посмотреть результат выполнения файла можно, нажав на кнопку Run. Результат появится в правой части окна.


```
	Уж осени конец, 
	Но верит в будущие дни 
	Зеленый мандарин. 
	Мацуо Басё 
```
- в тег абзаца `<p></p>`
- задайте переводы строк - тег `<br>`
- заключите автора (Мацуо Басё) в тег `span (<span></span>)`
- задайте таблицу стилей (css)

Для `p > span`  (родитель > потомок) задайте  
	`font-size: 120%` 	- cвойство задаёт размер шрифта   
	`font-weight: 600`	- cвойство задаёт жирность начертания.   
(Значением свойства font-weight может быть число от 100 до 900, кратное 100 (100, 200, 300, ... , 800, 900)  
	`font-style: italic`	- стиль начертания шрифта  
	`color: red` 		- цвет текста  

## Задача (2 урока)

1. Добавьте для тега `p` свойства `css`:
```
- text-transform: uppercase;		- все буквы заглавные
- text-decoration: underline;		- нижнее подчеркивание
```
2. Добавьте заголовок 2 уровня `h2` и запишите в него текст `Зеленый мандарин`:
3. Заключите все стихотворение (все теги) в блок (тег `<div></div>`)
4. Назначьте блоку класс `cats`
5. Назначьте в CSS для класса `cats` свойства
```
  height: 100vh;	- на всю высоту страницы браузера
  background-position: top center;	- фон располагать вверху и по-центру
  background-image: url("https://img.freepik.com/free-photo/close-up-on-kitten-surrounded-by-flowers_23-2150782329.jpg?size=213&ext=jpg");	- урл картинки
```
