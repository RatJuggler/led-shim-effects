from .abstract_effect import AbstractEffect
from colours import Colours


class SolidColours(AbstractEffect):
    """
    A basic effect which just shows a sequence of solid colours.
    """

    def __init__(self, canvas, debug=False):
        self.__colour = 0
        super(SolidColours, self).__init__("solid_colours", 0.5, canvas, debug)

    def compose(self):
        self.canvas.set_all(Colours.COLOURS[self.__colour])
        self.__colour = (self.__colour + 1) % len(Colours.COLOURS)

    def __repr__(self):
        return "SolidColours(Step:{0})".format(self.__colour)
