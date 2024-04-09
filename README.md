### Задача 1. Игра "Посади птичку на ветку"

Создать простую игру "Посади птичку на ветку" на python, с использованием библиотеки pygame.  

1. В Проводнике создайте папку `bird-game`  
2. Создайте 2 небольшие картинки (размером 24 x 24) или спрайта для игры  
Используйте Яндекс-Брайзер и зайдите на сайт [flaticon.com](https://www.flaticon.com/)  
для выбора изображения птички - в строке поиска укажите `bird`   
- скопируйте изображения в буфер обмена (Copy PNG)
- откройте графический редактор - программу `Gimp` и вставьте изображение из буфера обмена    
- вызовите меню `Изображение \ Размер изображения` и измените размеры на `24 x 24`
- сохраните картинку под именем 'bird.png' в каталог с игрой `Документы \ bird-game`  
для выбора изображения веточки - в строке поиска укажите `branch`
- скопируйте изображения в буфер обмена (Copy PNG)
- откройте графический редактор - программу `Gimp` и вставьте изображение из буфера обмена    
- вызовите меню `Изображение \ Размер изображения` и измените размеры на `24 x 24`
- сохраните картинку под именем 'branch.png' в каталог с игрой `bird-game`  
3. Откройте в `pyCharm` папку `bird-game`
3.5 Установите библиотеку `pygame` набрав ее название и нажав на `Install package` через меню `Settings \ Python interpretator`
4. Создайте файл game.py и скопируйте в него следующее содержание  
```
import pygame
import time
 
# Инициализация Pygame
pygame.init()
 
# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
 
# Загрузка спрайтов птички и веточки
bird_img = pygame.image.load('bird.png')
branch_img = pygame.image.load('branch.png')
 
# Начальные координаты для анимации
x = 30
y = 30
speed = 5
branch_x = screen_width // 2 - 50
branch_y = screen_height - 100

# Основной цикл программы
running = True
while running:
    screen.fill((255, 255, 255))  # Очистка экрана
 
    # Отображение птички и веточки
    screen.blit(bird_img, (x, y))
    screen.blit(branch_img, (branch_x, branch_y))
 
    pygame.display.flip()  # Обновление экрана
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Управление движением птички клавишами
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
 
    time.sleep(0.1)  # Задержка между кадрами
 
# Завершение работы Pygame
pygame.quit()
```
5. Доведите птичку до веточки.
6. Сделайте выход из игры (`running = False`) при достижении веточки или выполнения условия:
```
    if branch_y-24 < y < branch_y+24 and branch_x-24 < x < branch_x+24:
        running = False
```

### Задание 2 - Посадка ракеты на луну!

Изменим спрайты, определим событие пересечения спрайтов и выведем сообщение об успешной посадке.  
1. Скачайте спрайты ракеты и луны с сайта [flaticon.com](https://www.flaticon.com/)  или [iconfinder.com](https://www.iconfinder.com/)
2. Сохраните изображение ракеты в папку `images` используя редактор `Gimp` (меню `Изображение \ Размер изображения` и измените размеры на `128 x 128`, название `rocket.png`)
3. Сохраните изображение луны в папку `images` используя редактор `Gimp` (меню `Изображение \ Размер изображения` и измените размеры на `384 x 384`, название `moon.png`)
```
# Загрузка спрайтов птички и веточки
rocket_img = pygame.image.load('images/rocket.png')
moon_img = pygame.image.load('images/moon.png')
myfont = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
text_surface = myfont.render('You win!', False,'Red')
```
