### Задача "Разработка сайта"

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
