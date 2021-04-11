#This module is responsible for environment where it is loaded and related settings.

import os
from wrap_py import settings

path=[settings.DATA_PATH, settings.DATA_PATH_ALT]

def add_search_path(fspath):
    fspath = os.path.abspath(fspath)
    if fspath not in path:
        path.append(fspath)

def get_sprite_types_path(base_path):
    return os.path.join(base_path, settings.SPRITES_TYPES_SUBFOLDER)

def get_backgrounds_path(base_path):
    return os.path.join(base_path, settings.BACKGROUNDS_SUBFOLDER)

def get_sounds_path(base_path):
    return os.path.join(base_path, settings.SOUNDS_SUBFOLDER)

def get_pictures_path(base_path):
    return os.path.join(base_path, settings.PICTURES_SUBFOLDER)

