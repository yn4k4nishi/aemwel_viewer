from cgitb import enable


class YAxisProperty():

    enable = True
    label  = ''
    lw     = 3
    color  = 'black'
    type   = 'Solid'


    def __init__(self, label) -> None:
        self.label = label