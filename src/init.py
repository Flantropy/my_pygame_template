import pygame
import constants as c
from splash_screen import SplashScreen
from controller import Controller


def get_display():
	display = pygame.display.set_mode(c.DISPLAY_SIZE)
	return display


def get_clock():
	clock = pygame.time.Clock()
	return clock


def get_game_states():
	game_states = {c.SPLASH_SCREEN: SplashScreen}
	return game_states


def get_controller(display, clock, game_states, starting_state):
	controller = Controller(display, clock, game_states, starting_state)
	return controller
