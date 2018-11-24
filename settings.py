class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализация статических настроек игры'''
        # Параметры экрана
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (0, 8, 50)
        # Настройка скорости корабля
        self.ship_limit = 2
        # Параметры пуль корабля
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 229, 255, 0
        self.bullets_allowed = 3
        # Настройки пришельцев

        self.fleet_drop_speed = 10
        # Темп ускорения игры
        self.speedup_scale = 1.2
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Инициализирует настройки меняющиеся по ходу игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction = 1 - движение вправо, a -1 влево
        self.fleet_direction = 1
        # Подсчёт очков
        self.alien_points = 50


    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)