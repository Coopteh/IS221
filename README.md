# Диалог двух ИИ-персонажей (агентов) через Giga Chat

Проект 
https://github.com/Scicommunity/gigachain?tab=readme-ov-file  

Установка библиотек (запускать в терминале PyCharm)  
```
pip install -U langchain-community
pip install gigachain
pip install gigachain-cli
```

Сам пример на python
```
""" Пример работы с чатом через gigachain
    Диалог двух ИИ-персонажей (агентов)

    Для получения токена доступа пройдите по ссылке и авторизуйтесь на
    https://developers.sber.ru/studio/workspaces/my-space/get/gigachat-api
    Тариф-Freemium -> Настройка API
"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
API_KEY = "MDE5OTlhMjQtZDkzMC03YTVjLTlkZmMtMTNiNDczMTQwYzA0OjkzYzg0Y2I2LTAxOTUtNDJmMi04NDY4LTc5MzIyOTVlMTJiMg=="

# Авторизация в сервисе GigaChat
giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False)

ass1_msgs = [
    SystemMessage(content='Ты являешься Винни-Пухом и опытным детективом. \
    Твоя задача расследывать кражу, свидетелем которой стал Пятачок. \
    Опроси свидетеля об обстоятельствах кражи, которая происходила \
    на его глазах. Задавай только по одному вопросу за раз. \
    Свидетель может быть растерян, задавай наводящие вопросы. \
    Возможно он тоже как-то замешан. Попробуй через вопросы выяснить это. \
    Ты уже задал первый вопрос Пятачку, что он делал рядом с местом кражи. \
    Ты всегда заканчиваешь свои реплики новым вопросом.'
    )
]
ass2_msgs = [
    SystemMessage(content='Ты являешься Пятачком. Тебе не повезло стать \
    свидетелем кражи. Тебя будет опрашивать твой друг детектив Винни-Пух. \
    Постарайся ему отвечать честно, хотя ты испытываешь стресс после случившегося.')
]
ass1_name= "Винни-Пух"
ass2_name= 'Пятачек'

# пусть Агент-01 задает первый вопрос Агенту-02
ass2_msgs.append( HumanMessage(content='Привет, Пятачок! Я расследую это преступление. \
    Расскажи, как ты тут оказался?')
)

print('Итерация - 0')
print(f'Агент-01 ({ass1_name}):', ass2_msgs[-1].content)
for i in range(5):
    # Отвечает Агент-02
    ass2_answer = giga(ass2_msgs)
    print(f'Агент-02 ({ass2_name}):', ass2_answer.content) # выводим ответ
    ass2_msgs.append(ass2_answer) # добавляем ответ как AssistantMessage
    ass1_msgs.append(HumanMessage(content=ass2_answer.content)) # это же сообщение добавляем в диалог Агент-01 в качестве HumanMessage

    print('*******\n', 'Итерация - ', i+1)
    # Отвечает Агент-01
    ass1_answer = giga(ass1_msgs)
    print(f'Агент-01 ({ass1_name}):', ass1_answer.content)
    ass1_msgs.append(ass1_answer) # добавляем ответ как AssistantMessage
    ass2_msgs.append(HumanMessage(content=ass1_answer.content))

```
