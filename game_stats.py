import json


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
        self.high_score = self.get_high_score()

    def reset_stats(self):
        '''Инициализирует статистику меняющуюся по ходу игры'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Сохраняет рекорд игры в файл"""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)

    def get_high_score(self):
        """Извлекает значение рекордных очков игры из файла
        для дальнейшего использования в программе
        """
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return self.high_score
