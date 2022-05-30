from time import sleep
from plot import Color
from plot import LineStyle

_i_color = 0

class YAxisProperty():
    name = ''
    is_enabled = True
    label  = ''
    lw     = 3
    color  = 'Black'
    style  = 'solid'

    def __init__(self, label, is_enabled=True) -> None:
        self.name = label
        self.label = label
        self.is_enabled = is_enabled

        global _i_color
        self.color = Color[_i_color]
        _i_color = (_i_color + 1) % len(Color)

    def setEnable(self, bool):
        self.is_enabled = bool
    
    def setLabel(self, label):
        self.label = label
    
    def setLineWidth(self, lw):
        self.lw = lw

    def setColor(self, color):
        self.color = color

    def setStyle(self, style):
        self.style = style