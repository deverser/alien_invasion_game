class GameStats():
    '''Отслеживание статистики для игры'''
    def __init__(self, ai_settings):
        '''Инициализирует статистику'''
        self.ai_settings = ai_settings
        self.reset_stats()


    def reset_stats(self):
        '''Инициализирует статистику меняющуюся по ходу игры'''
        self.ships_left = self.ai_settings.ship_limit