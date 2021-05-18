from pygame import USEREVENT, QUIT

# SCALING AND FPS
FULL_SCREEN = 0
SCALE = 1
FPS = 30

# EVENTS
CLOSE_GAME = int(USEREVENT + 1)
LOAD_MENU = int(USEREVENT + 2)
PLAY = int(USEREVENT + 3)
PAUSE = int(USEREVENT + 4)
QUIT_TO_MENU = int(USEREVENT + 5)
RESUME = int(USEREVENT + 6)

STATE_CHANGING_EVENTS = [QUIT, CLOSE_GAME, LOAD_MENU, PLAY, PAUSE, QUIT_TO_MENU, RESUME]

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

DISPLAY_WIDTH = int(NATIVE_WIDTH * SCALE)
DISPLAY_HEIGHT = int(NATIVE_HEIGHT * SCALE)
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
