import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse and Keyboard Control")

# Загрузка изображений
mouse_image = pygame.image.load('img/samolet_mouse.png')  # Изображение для управления мышью
keyboard_image = pygame.image.load('img/plane_keyboard.png')  # Изображение для управления клавишами
background_image = pygame.image.load('img/background.png')  # Фоновый рисунок

# Начальные координаты второго самолета
keyboard_x, keyboard_y = 100, 300  # Начальная позиция для изображения, управляемого клавишами

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка закрытия окна
            running = False

    # Получение позиции мыши
    mouse_pos = pygame.mouse.get_pos()
    mouse_image_rect = mouse_image.get_rect(center=mouse_pos)  # Центр изображения мыши

    # Обработка событий клавиатуры
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        keyboard_x -= 5  # Движение влево
    if keys_pressed[pygame.K_RIGHT]:
        keyboard_x += 5  # Движение вправо
    if keys_pressed[pygame.K_UP]:
        keyboard_y -= 5  # Движение вверх
    if keys_pressed[pygame.K_DOWN]:
        keyboard_y += 5  # Движение вниз

    keyboard_image_rect = keyboard_image.get_rect(center=(keyboard_x, keyboard_y))  # Центр изображения клавиш

    # Очистка экрана и отрисовка фона
    screen.blit(background_image, (0, 0))  # Рисуем фон

    # Отображаем изображения
    screen.blit(mouse_image, mouse_image_rect)  # Изображение, управляеое мышью
    screen.blit(keyboard_image, keyboard_image_rect)  # Изображение, управляеое клавишами

    pygame.display.flip()  # Обновление экрана

# Завершение работы Pygame
pygame.quit()