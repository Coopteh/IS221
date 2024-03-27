### Задача "Интеграция с API-Marvel"

Необходимо написать пару скриптом, которые:
1. получают данные в json-формате с сайта marvel.com  
ссылка `URL = https://jsfree-les-3-api.onrender.com/characters`
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
7. После скрипта добавьте скрипты:
```
<script src="index.js"></script>
<script src="start.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", () => {
        start();
    });
</script>
```
все используемые js функции находятся в файле `index.js`  
управляющая функция `start()` находится в файле `start.js`  
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
- запустите `Go Live`
- нажмите `F12` (Панель разработчика) и откройте вкладку "Консоль"






Используйте сайт [replit.com](https://replit.com/@vmilevskiy/jsfree-les-3-start-template#index.html)

На занятии мы научились получать данные с [API](https://jsfree-les-3-api.onrender.com/characters)  
и используя полученные данные оживили статичную верстку.  
Вам нужно повторить аналогичные операции.

```
Вся работа будет происходить в файле index.js

Внутри function fetchCharacters() {} реализуйте получение данных с API, используя Fetch
  function fetchCharacters() {
      let url= "https://jsfree-les-3-api.onrender.com/characters";
      return fetch(url).then( res => res.json() );
  }

Внутри function getCharacterCards(characters) {} реализуйте формирование массива карточек персонажей
  function getCharacterCards(characters) {
      let arr= [];
      for(let i=0; i < characters.length; i++) {
        let character = characters[i];
        let card = getCharacterCard(character);
        arr.push( card );
      }
      return arr;
  }
```
