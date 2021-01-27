import os

DATA_CATALOG_NAME = "wrap_py_catalog"

DATA_PATH = os.path.abspath( os.path.join(os.path.expanduser("~"), DATA_CATALOG_NAME) )
DATA_PATH_ALT = os.path.abspath(DATA_CATALOG_NAME)

SPRITES_TYPES_SUBFOLDER="sprite_types"
BACKGROUNDS_SUBFOLDER="backgrounds"
PICTURES_SUBFOLDER="images"
SOUNDS_SUBFOLDER="sounds"


SPRITE_TYPES_PATH = os.path.join(DATA_PATH, SPRITES_TYPES_SUBFOLDER)
BACKGROUNDS_PATH = os.path.join(DATA_PATH, BACKGROUNDS_SUBFOLDER)
PICTURES_PATH = os.path.join(DATA_PATH, PICTURES_SUBFOLDER)
SOUNDS_PATH = os.path.join(DATA_PATH, SOUNDS_SUBFOLDER)

SPRITE_TYPES_PATH_ALT = os.path.join(DATA_PATH_ALT, SPRITES_TYPES_SUBFOLDER)
BACKGROUNDS_PATH_ALT = os.path.join(DATA_PATH_ALT, BACKGROUNDS_SUBFOLDER)
PICTURES_PATH_ALT = os.path.join(DATA_PATH_ALT, PICTURES_SUBFOLDER)
SOUNDS_PATH_ALT = os.path.join(DATA_PATH_ALT, SOUNDS_SUBFOLDER)


print(_("Wrap_py uses this catalogs: "))

print(DATA_PATH)
print(DATA_PATH_ALT)