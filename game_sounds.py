import pygame


class GameSounds():
    """Создает звуки в игре"""
    def __init__(self):
        # Звук взрыва пришельца при попадании в него пули
        try:
            self.alien_sound = pygame.mixer.Sound('sounds/boom.wav')
        except pygame.error:
            pass
        # Звук выстрела
        try:
            self.shot_sound = pygame.mixer.Sound('sounds/blaster.wav')
        except pygame.error:
            pass
        # Звук гибели корабля
        try:
            self.death_ship = pygame.mixer.Sound('sounds/ship_dead.wav')
        except pygame.error:
            pass

    def pew_sound(self):
        """Издает звук выстрела при создании пули на экране"""
        try:
            self.shot_sound.play()
        except AttributeError:
            pass

    def alien_boom_sound(self):
        """Издает звук взрыва при попадании пули в пришельца"""
        try:
            self.alien_sound.play()
        except AttributeError:
            pass

    def ship_death_sound(self):
        """Издает звук при гибели корабля"""
        try:
            self.death_ship.play()
        except AttributeError:
            pass
