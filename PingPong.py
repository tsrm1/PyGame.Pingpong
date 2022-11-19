""" Игра Бандерогусак
"""
import pygame                           # импортируем библиотеку pygame
pygame.init()                           # инициализируем/вызываем библиотеку pygame
screen_size = Width, Height = 800, 600  # ширина и высота окна
main_surface = pygame.display.set_mode((screen_size), pygame.DOUBLEBUF | pygame.HWSURFACE) # создаём поверхность отрисовки
# set_mode(Width, Height) - формируем/вызываем окно (щирина, высота) в pixel
# pygame.DOUBLEBUF - двойная буферизация
# pygame.HWSURFACE - аппаратное ускорение отрисовки
# pygame.FULLSCREEN - полноэкранный режим
# pygame.OPENGL - обработка отображений с помощью библиотеки OpenGL
# pygame.RESIZABLE - окно с  изменяемыми размерами
# pygame.NOFRAME - окно без рамки и заголовка
# pygame.SCALED - разрешение, зависящее от размеров рабочего стола
pygame.display.set_caption("PingPong on PyGame")                            # устанавливаем название окна
#pygame.display.set_icon(pygame.image.load("image/pingpong.jpg"))              # устанавливаем иконку окна
clock = pygame.time.Clock()             # создаём экземпляр класса Clock
FPS = 30                                # устанавливаем частоту обработки цикла, FPS раз в секунду

RED = (255, 0, 0),              # цвет красный
GREEN = (0, 255, 0),            # цвет зелённый
BLUE = (0, 0, 255)              # цвет синий
BLACK = (0, 0, 0)               # цвет чёрный
WHITE = (255, 255, 255)         # цвет белый

ball_pos = {            # ball position. положение мяча
    "x": 0,             # начальное положение мяча, координата X
    "y": 0,             # начальное положение мяча, координата Y
}
ball_speed = [10, 10]          # ball offset. смещение мяча по координате X и по координате Y
ball = pygame.Surface((20, 20))
ball_rect = ball.get_rect()
ball_color = [RED, GREEN, BLUE, WHITE]          # перечень возможных цветов мяча
ball_color_numer = 0                            # текущий номер цвета мяча

# start game loop
game_over = False                               # флаг окончания игры
while not game_over:                            # start game loop
    for event in pygame.event.get():            # переменная event принимает значение сообщений из очереди событий pygame.event.
        if event.type == pygame.QUIT:           # проверяем ТИП события event, равно ли QUIT (закрыть окно, выход из программы)
            game_over = True                    # выход из основного цикла

    ball_rect = ball_rect.move(ball_speed)      # свдвигаем поверхность "мяч"
    if ball_rect.bottom >= Height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball_color_numer = ball_color_numer +1 if ball_color_numer < 3 else 0

        # ball_color_numer +=1 if ball_color_numer < 3 else 0
        
        # if ball_color_numer > 3:
        #     ball_color_numer = 0
    if ball_rect.right >= Width or ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]
        ball_color_numer = ball_color_numer +1 if ball_color_numer < 3 else 0

    main_surface.fill(BLACK)                    # clear screen
    ball.fill(ball_color[ball_color_numer])     # закрашиваем поверхность "мяч" в текущий цвет
    main_surface.blit(ball, ball_rect)          # накладываем поверность "мяч" на основную поверхность "фон"
    pygame.display.update()             # вывод прямоугольной области (списка областей) из буфера
    clock.tick(FPS)                     # вызывааем метод tick() класса Clock(), устанавливаем задержку для цикла, FPS
                                        # FPS раз в секунду с учётом времени на выполнение операций в самом цикле
pygame.quit()  # выход из модуля pygame
quit()
