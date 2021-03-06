import pygame
from settings import Settings
from game_sounds import GameSounds
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Инициализирует pygame, settings, game sounds и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    gs = GameSounds()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки play
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляров для ведения статистики и счёта
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, gs, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, gs, bullets)
            gf.update_aliens(ai_settings, screen, stats, gs, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
