from statemachine import State, StateMachine


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
    
    @staticmethod
    def on_enter_loadscreen():
        print("loading started")
    
    @staticmethod
    def on_enter_main_menu():
        print("welcome to main menu")
    
    @staticmethod
    def on_load():
        print("loading finished")
    
    @staticmethod
    def on_close():
        print("back to loadscreen")
