class GameStats():
    '''Отслеживание статистики для игры'''
    def __init__(self, ai_settings):
        '''Инициализирует статистику'''
        self.ai_settings = ai_settings
        self.ship_left = ai_settings.ship_limit
        # Игра запускается в неактивном состоянии
        self.game_active = False
        self.reset_stats()
        # Рекорд игры не должен сбрасываться
        self.high_score = 0


    def reset_stats(self):
        '''Инициализирует статистику меняющуюся по ходу игры'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0