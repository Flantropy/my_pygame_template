# SCALING AND FPS
FULL_SCREEN = 0
SCALE = 1
FPS = 60

# DISPLAY INFORMATION
NATIVE_WIDTH = 480
NATIVE_HEIGHT = 270
NATIVE_SIZE = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_WIDTH_CENTER = NATIVE_WIDTH // 2
NATIVE_HEIGHT_CENTER = NATIVE_HEIGHT // 2
NATIVE_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT_CENTER)
NATIVE_TOP = 0
NATIVE_BOTTOM = NATIVE_HEIGHT
NATIVE_RIGHT = NATIVE_WIDTH
NATIVE_LEFT = 0
NATIVE_TOP_LEFT = (NATIVE_LEFT, NATIVE_TOP)
NATIVE_TOP_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_TOP)
NATIVE_TOP_RIGHT = (NATIVE_WIDTH, NATIVE_TOP)
NATIVE_RIGHT_CENTER = (NATIVE_WIDTH, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM_RIGHT = NATIVE_SIZE
NATIVE_BOTTOM_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT)
NATIVE_BOTTOM_LIFT = (NATIVE_LEFT, NATIVE_HEIGHT)
NATIVE_LEFT_CENTER = (NATIVE_LEFT, NATIVE_HEIGHT_CENTER)

DISPLAY_WIDTH = NATIVE_WIDTH * SCALE
DISPLAY_HEIGHT = NATIVE_HEIGHT * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_WIDTH_CENTER = DISPLAY_WIDTH // 2
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT // 2
DISPLAY_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT_CENTER)
DISPLAY_TOP = 0
DISPLAY_BOTTOM = DISPLAY_HEIGHT
DISPLAY_RIGHT = DISPLAY_WIDTH
DISPLAY_LEFT = 0
DISPLAY_TOP_LEFT = (DISPLAY_LEFT, DISPLAY_TOP)
DISPLAY_TOP_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_TOP)
DISPLAY_TOP_RIGHT = (DISPLAY_WIDTH, DISPLAY_TOP)
DISPLAY_RIGHT_CENTER = (DISPLAY_WIDTH, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM_RIGHT = DISPLAY_SIZE
DISPLAY_BOTTOM_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT)
DISPLAY_BOTTOM_LIFT = (DISPLAY_LEFT, DISPLAY_HEIGHT)
DISPLAY_LEFT_CENTER = (DISPLAY_LEFT, DISPLAY_HEIGHT_CENTER)

# GAME STATE INFORMATION
SPLASH_SCREEN = "SPLASH_SCREEN"
MAIN_MENU = "MAIN_MENU"
CHARACTER_SELECT = "CHARACTER_SELECT"
LEVEL = "LEVEL"
GAME_STATES = [SPLASH_SCREEN,
               MAIN_MENU,
               CHARACTER_SELECT,
               LEVEL
               ]
STARTING_STATE = GAME_STATES[0]

# DIRECTORY INFORMATION (work only with windows)
DIR_FONTS = "\\fonts\\"
DIR_IMAGES = "\\images\\"
DIR_MUSIC = "\\music\\"
DIR_SOUNDS = "\\sounds\\"
