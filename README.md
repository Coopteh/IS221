### Задание 1 - Подключение Bootstrap

Bootstrap — свободный набор инструментов для создания сайтов и веб-приложений.  
Включает в себя HTML- и CSS-шаблоны оформления для типографики, веб-форм, кнопок, меток,  
блоков навигации и прочих компонентов веб-интерфейса, включая JavaScript-расширения.

Задание - подключить стили и js-библиотеку Bootstap   
и добавить пример формы из документации, чтобы проверить работу шаблона

Шаги выполнения:
1. Создайте в Проводнике в папке `Документы` новую папку `cafe`
2. Откройте в Visual Studio Code папку `Документы\cafe`
3. Создайте файл `index.html` и через `!<tab>` задайте структуру html-страницы
4. Откройте в браузере ссылку [https://getbootstrap.com/](https://getbootstrap.com/)
5. Найдите в меню `Docs \ Download \ Source files \ Download sources` - скачайте архив
6. Найдите в нем папку `dist` и скопируйте файлы:
```
bootstrap.bundle.min.js  -  в новую папку js (создайте папку внутри `Документы\cafe`)
bootstrap.min.css  -  в новую папку css (создайте папку внутри `Документы\cafe`)
```
5. Подключите таблицу стилей `bootstrap.min.css` в конце секции `head` (тег `<link rel="stylesheet" href="...">`)
6. Подключите js-скрипты `bootstrap.bundle.min.js` в конце секции `body` (тег `<script src="..."></script>`)
7. Добавьте блок
```
<div class="container">
	<div class="row">

	</div>
</div>
```
8. Внутрь блока добавьте html-код формы из документации [https://getbootstrap.com/](https://getbootstrap.com/) (`Docs \ Forms \ Form controls \ Example`)
11. Откройте в браузере через `Go Live` - форма должна отображаться в стилях Bootstrap!
<hr>

### Задание 2 - Добавление карусели изображений

1. Откройте в Visual Studio Code папку `Документы\cafe`
2. На сайте Bootstrap  [https://getbootstrap.com/](https://getbootstrap.com/) зайдите в раздел `Docs \ Components \ Carousel \ Basic examples`
3. Скопируйте код карусели и вставьте над формой
4. Найдите 3 картинки пиццы и сохраните их в папку `img` (создайте папку внутри `Документы\cafe`)
5. Исправьте в html-коде карусели атрибуты `src` тегов `img`, чтобы они указывали на нужные картинки (пример <img src="./img/image1.png">)
6. Проверьте работу карусели изображений - в браузере через `Go Live`
<hr>

### Задание 3 - Добавление навигационной панели

1. Откройте в Visual Studio Code папку `Документы\cafe`
2. На сайте Bootstrap  [https://getbootstrap.com/](https://getbootstrap.com/) зайдите в раздел `Docs \ Components \ Navbar`
3. Скопируйте код навигационной панели без кнопок и форм
```
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled" aria-disabled="true">Disabled</a>
      </div>
    </div>
  </div>
</nav>
```
6. Создайте меню с пунктами "Главная", "Каталог", "Сделать заказ", "Для персонала" (disabled)
7. Измените ссылку `Каталог` c `#` на `./products.html`
8. Измените название бренда (<a class="navbar-brand") - вместо `Navbar` на `ПИЦЦА ИС-221`
<hr>

### Задание 4 - Каталог продукции

1. Откройте в Visual Studio Code папку `Документы\cafe`
2. Создайте новый файл `products.html`, через `!<tab>` задайте структуру html-страницы
3. Добавьте на страницу Bootstrap css (тег link) из файла `index.html`
4. В секцию body добавьте блок `<div class="container">`
5. Добавьте на страницу навигационную панель с меню сайта (блок nav) из файла `index.html` в блок `<div class="row">`
6. Добавьте после навигационной панели заголовок страницы
```
    <div class="row mb-5">
        <h1>Каталог продукции</h1>
    </div>
```
7. Создайте 3 новых блока `<div class="row">` в каждый из которых добавьте 2 блока `<div class="col-6">`
```
- в левом блоке должна быть картинка
- в правом блоке - название, описание, вес и цена
Описание можете взять с https://silver-food.ru/kemerovo/burgery
```
8. Блоки должны содержать описания трех товаров: Гамбургер, Чизбургер, Чикен Бургер
9. Проверьте работу на сайте `localhost/products.html`
