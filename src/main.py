import init
import constants as c


def main():
	display = init.get_display()
	clock = init.get_clock()
	game_states = init.get_game_states()
	controller = init.get_controller()
	controller.run_game(display, clock, game_states, c.STARTING_STATE)
	
	
if __name__ == '__main__':
	main()
