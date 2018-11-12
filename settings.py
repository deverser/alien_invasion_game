class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализация настроек игры'''
        # Параметры экрана
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (0, 8, 50)
        # Настройка скорости корабля
        self.ship_speed_factor = 1.5
        # Параметры пуль корабля
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 229, 255, 0
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 - движение вправо, a -1 влево
        self.fleet_direction = 1