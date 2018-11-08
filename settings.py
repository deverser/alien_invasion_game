class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализация настроек игры'''
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 8, 50)
        self.ship_speed_factor = 1.5
