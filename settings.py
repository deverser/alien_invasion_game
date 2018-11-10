class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализация настроек игры'''
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 8, 50)
        self.ship_speed_factor = 1.5
        # Параметры пуль корабля
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 229, 255, 0
        self.bullets_allowed = 3
