import os

#preload pygame with Hello disabled for future use
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.init()

#set module language
import wrap_py
from wrap_py import _transl
_transl.set_lang("ru_RU")
from wrap_py._transl import translator as _

#Say hi to user
from wrap_py import settings as st
print()
print(_("Wrap_py uses these catalogs: "))
print(st.DATA_PATH)
print(st.DATA_PATH_ALT)


#load modules for external usage
from wrap_py.ru import programma
from pygame.locals import *