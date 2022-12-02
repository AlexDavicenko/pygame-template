from typing import Tuple
from pygame import font

def Label(size: int, text: str, color: Tuple[int, int, int], x: int, y: int, f = 'freesansbold.ttf'):
    fnt = font.Font(f,size)
    l = fnt.render(text, True, color)
    lRect = l.get_rect()
    lRect.topleft = (x,y)
    
    return l, lRect
