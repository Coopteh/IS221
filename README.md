### Задача 1. "Случайная шутка и ее перевод"

Необходимо написать скрипты вызова случайной шутки по API и перевести ее, вызвав Google Translate

1. получаем данные в json-формате по ссылке `URL = https://official-joke-api.appspot.com/random_joke`  
2. формируют карточку с шуткой на экран
3. переводим - вызвав google translate

Выполнение:
1. В Visual Studio Code откройте папку `Документы \ marvel-api`
2. Откройте html-страницу 'index.html'
3. Измените заголовки на "1 апрельская шутка" и "День смеха"
4. Добавьте 2 кнопки
```
    <div class="row">
        <button onclick="start_joke();">Получить шутку</button>
    </div>

    <div class="row" id="character-card-box">
        <div class="d-flex justify-content-center">
            <!--<div class="spinner-border text-danger center" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>-->
        </div>
    </div>

    <div class="row">
        <button onclick="translate_joke(data);">Перевести шутку</button>
    </div>
```
5. 
