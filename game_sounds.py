import pygame


class GameSounds():
    """Создает звуки в игре"""
    def __init__(self):
        # Звук взрыва пришельца при попадании в него пули
        self.alien_sound = pygame.mixer.Sound('sounds/boom.wav')
        # Звук выстрела
        self.shot_sound = pygame.mixer.Sound('sounds/blaster.wav')
        # Звук гибели корабля
        self.death_ship = pygame.mixer.Sound('sounds/ship_dead.wav')

    def pew_sound(self):
        """Издает звук выстрела при создании пули на экране"""
        self.shot_sound.play()

    def alien_boom_sound(self):
        """Издает звук взрыва при попадании пули в пришельца"""
        self.alien_sound.play()

    def ship_death_sound(self):
        """Издает звук при гибели корабля"""
        self.death_ship.play()