from plot import Color
from plot import LineStyle

class YAxisProperty():

    is_enabled = True
    label  = ''
    lw     = 3
    color  = 'Black'
    style  = 'solid'

    def __init__(self, label, is_enabled=True) -> None:
        self.label = label
        self.is_enabled = is_enabled

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