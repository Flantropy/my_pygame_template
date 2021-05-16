from statemachine import State, StateMachine

from game_states import (
    LoadScreen,
    MainMenu,
    Game,
    Pause
)


class FSM(StateMachine):
    loadscreen = State("Loadscreen", initial=True)
    main_menu = State("MainMenu")
    game = State("Game")
    on_hold = State("OnHold")
    
    load = loadscreen.to(main_menu)
    play = main_menu.to(game)
    pause = game.to(on_hold)
    resume = on_hold.to(game)
    quit = on_hold.to(main_menu)
    close = main_menu.to(loadscreen)
    
    def on_load(self):
        self.model.current_scene = MainMenu()
        
    def on_play(self):
        self.model.current_scene = Game()
        
    def on_pause(self):
        self.model.current_scene = Pause()
        
    def on_resume(self):
        self.model.current_scene = Game()
        
    def on_quit(self):
        self.model.current_scene = MainMenu()
    
    def on_close(self):
        self.model.current_scene = LoadScreen()
    
    @staticmethod
    def on_enter_loadscreen():
        print("loading started")
    
    @staticmethod
    def on_enter_main_menu():
        print("welcome to main menu")
        
    @staticmethod
    def on_enter_game():
        print("game started")
        
    @staticmethod
    def on_enter_on_hold():
        print("pause")
