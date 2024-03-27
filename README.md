### Задача 1. "Интеграция с API-Marvel"

Необходимо написать пару скриптов, которые:
1. получают данные в json-формате с сайта marvel.com  
ссылка `URL = https://jsfree-les-3-api.onrender.com/characters` - [перейдите посмотреть что там за API](https://jsfree-les-3-api.onrender.com/characters)  
2. формируют и добавляют на страницу карточки с названием персонажа и его картинкой

Выполнение:
1. В Visual Studio Code создайте и откройте новую папку `Документы \ marvel-api`
2. В пустой папке `marvel-api` создайте html-страницу 'index.html'
3. Через эммет `!+tab` задайте базовую структуру
4. Добавьте тaблицу стилей bootstrap в секцию `head`
```
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
          crossorigin="anonymous"
    >
```
5. Добавьте заголовок `Персонажи Marvel` в секцию `head`
6. Добавьте скрипты bootstrap в конец секции `body`
```
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
        crossorigin="anonymous"
></script>
```
7. После bootstrap-скрипта добавьте скрипты:
```
<script src="index.js"></script>
<script src="start.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", () => {
        start();
    });
</script>
```
- все используемые js функции находятся в файле `index.js`  
- управляющая функция `start()` находится в файле `start.js`

9. Создайте файл `index.js` и добавьте в него функцию `fetchData`
```
/**
 * получим информацию с API
 */
function fetchData( url ) {
    data = fetch( url ).then( res=>res.json() );
    console.log( data );
    return data;
}
```
`fetchData( url )` - запрашивает удаленный сервер по переданному `url` js-методом `fetch`  
и, когда получает успешный ответ на свой запрос, вызывается метод `.then()`
в нем производится преобразование полученных данных из строки в json-формат

Полученные данные записываются в переменную `data` и выводятся в консоль через `console.log()`

10. Создайте файл `start.js` и добавьте в него функцию `start`
```
async function start() {   
    url= "https://jsfree-les-3-api.onrender.com/characters";
    let data = await fetchData( url );
}
```
Здесь мы задаем конкретный url-адрес, ожидая получить ответ нужного формата,  
который сможем затем использовать (обработать у себя на странице)  

Чтобы увидеть результат:
- запустите `Go Live` для страницы `index.html`  
- нажмите `F12` (Панель разработчика) и откройте вкладку "Консоль"
  
Вы должны увидеть:  
```
- Promise { <state>: "fulfilled", <value>: (19) […] }
​<state>: "fulfilled"
​<value>: Array(19) [ {…}, {…}, {…}, … ]
​​0: Object { id: 1009610, name: "Человек-паук", nameor: "Spider-Man", … }
...
```
<hr>

### Задача 2. Добавление карточек с разметкой

У нас есть карточки из картинки и описания - с готовой версткой, использующей стили bootstrap!

1. Добавьте в `index.js` новую функцию
```
/**
 * Получить массив сформированных карточек персонажей
 *
 * @param jsonData
 * @returns {Array}
 */
function getCharacterCards(jsonData) {
    let arrCards=[];
    for(let i=0;  i< jsonData.length; i++) {
        let data = jsonData[i];
        let card = getCharacterCard(data);
        arrCards.push(card);
    }
    return arrCards;
}
```
`getCharacterCards(characters)`  - по переданному массиву с данными (jsonData)   
в цикле, формируется другой массив (arrCards) из сверстанных в html-разметку карточек персонажей  

2. Добавьте в `index.js` еще одну функцию
```
/**
 * Получить заполненную разметку карточки персонажа
 *
 * @param data
 * @returns {string}
 */
function getCharacterCard(data) {
    return `
        <div class="card mb-3 col-sm-12 col-md-6 col-lg-4">
            <div class="row g-0">
                <div class="col-4">
                    <img src="${data.thumbnail}"
                         style="max-width: 100%;"
                         alt="${data.name}"
                    >
                </div>
                <div class="col-8">
                    <div class="card-body">
                        <h5 class="card-title">${data.name}</h5>
                        <p>${data.description}</p>
                    </div>
                </div>
            </div>
        </div>
        `;
}
```
Это готовая разметка на bootstrap-стилях, в которую вставляются данные  
шаблонированным способом вида: `${data.name}`, здесь `$` обозначает переменную, а внутри скобок `{}` указывается ее название  
для отображения картинки используется знакомый вам тег `<img>`, для названия персонажа - тег заголовка `<h5>`

3. Добавьте в `start.js` еще пару строк
```

```
<hr>


### Задача 3. Персонажи Rick and Morty

Измените `url` на [API персонажей безумного мультсериала Rick and Morty](https://rickandmortyapi.com/api/character)
`url= "https://rickandmortyapi.com/api/character";`
