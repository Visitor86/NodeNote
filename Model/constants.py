from PyQt5.QtWidgets import QGraphicsItem
from Components import attribute


__all__ = ["DEBUG_DRAW_PIPE", "DEBUG_EFFECT_SNOW", "DEBUG_VIEW_CHANGE_SCALE", "DEBUG_TUPLE_NODE_SCALE",
           "Z_VAL_PORT", "Z_VAL_NODE", "Z_VAL_PIPE", "Z_VAL_NODE_WIDGET",
           "NODE_HEIGHT", "NODE_WIDTH", "NODE_LAYOUT_MARGINS", "NODE_SEL_BORDER_COLOR", "NODE_SEL_COLOR",
           "NODE_ICON_SIZE",
           "ITEM_CACHE_MODE",
           "INPUT_NODE_TYPE", "OUTPUT_NODE_TYPE",
           "MODE_PIPE_DRAG", "MODE_NOOP", "MODE_PIPE_CUT", "PIPE_DRAG_START_THRESHOLD",
           "SCALE_WIDGET"]


# === DEBUG ===
DEBUG_EFFECT_SNOW = False
DEBUG_TUPLE_NODE_SCALE = False
DEBUG_VIEW_CHANGE_SCALE = False
DEBUG_DRAW_PIPE = False
DEBUG_TEXT_CHANGED = False
DEBUG_PYTHON_SYNTAXHIGHTLIGHTER = False
DEBUG_RICHTEXT = False

# === DRAW STACK ORDER ===
Z_VAL_PIPE = 1
Z_VAL_NODE = 2
Z_VAL_PORT = 3
Z_VAL_NODE_WIDGET = 4


# === NODE ===
NODE_WIDTH = 150
NODE_HEIGHT = 70
NODE_LAYOUT_MARGINS = 5
NODE_ICON_SIZE = 24
NODE_SEL_COLOR = (255, 255, 255, 30)
NODE_SEL_BORDER_COLOR = (254, 207, 42, 255)

# === ITEM CACHE MODE ===
ITEM_CACHE_MODE = QGraphicsItem.DeviceCoordinateCache

# === NODE TYPE ===
INPUT_NODE_TYPE = 0
OUTPUT_NODE_TYPE = 1

# === DRAW LINE ===
MODE_NOOP = 1
MODE_PIPE_DRAG = 2
MODE_PIPE_CUT = 3
PIPE_DRAG_START_THRESHOLD = 10

# === WIDGET ===
SCALE_WIDGET = (attribute.LogicWidget,)
