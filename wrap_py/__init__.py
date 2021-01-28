import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from wrap_py import wrap_world as world, wrap_app as app, wrap_event as event
from wrap_py import wrap_sprite as sprite
from wrap_py import wrap_sprite_text as text_sprite
from wrap_py import settings as st