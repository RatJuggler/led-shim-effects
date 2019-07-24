import click
from random import randint
from time import sleep

import ledshim

from .canvas import Canvas
from .effects import Candle, BinaryClock, CheerLights, GradientGraph, Rainbow, RandomBlink, SolidColours

NUM_PIXELS = 28     # The number of LEDs on the shim.

ledshim.set_clear_on_exit()


@click.command(help="Show various effects on a Pimoroni LED shim.")
@click.version_option()
@click.option('-s', '--show_effects', type=click.Choice(["CYCLE", "RANDOM"]), default="CYCLE", help="How the effects are displayed.", show_default=True)
@click.option('-t', '--effect_time', type=int, default=10, help="How long to display each effect for, in seconds.", show_default=True)
@click.option('-i', '--invert', is_flag=True, help="Change the display orientation.")
@click.option('-l', '--log', type=click.Choice(["NONE", "INFO", "EFFECT", "DEBUG"]), default="NONE", help="Show additional logging information.")
def display_effects(show_effects, effect_time, invert, log):
    """
    Show various effects on a Pimoroni LED shim.
    :param show_effects: In a CYCLE or at RANDOM
    :param effect_time: How long to display each effect for
    :param invert: Depending on which way round the Pi is
    :param log: Set a logging level; NONE, INFO, EFFECT or DEBUG
    :return: No meaningful return
    """
    canvas = Canvas(NUM_PIXELS)
    effects = [Candle(canvas),
               GradientGraph(canvas),
               SolidColours(canvas),
               BinaryClock(canvas),
               Rainbow(canvas),
               CheerLights(canvas),
               RandomBlink(canvas)]
    show_time = 0
    effect_no = len(effects) - 1
    effect = effects[effect_no]
    try:
        while True:
            if show_time <= 0:
                if show_effects == "CYCLE":
                    effect_no = (effect_no + 1) % len(effects)
                if show_effects == "RANDOM":
                    effect_no = randint(0, len(effects))
                effect = effects[effect_no]
                show_time = effect_time / effect.get_speed()
                if log == "INFO" or log == "EFFECT" or log == "DEBUG":
                    print(str(effect))
            effect.compose()
            if log == "EFFECT" or log == "DEBUG":
                print(repr(effect))
            if log == "DEBUG":
                print(repr(canvas))
            for i in range(canvas.get_size()):
                pixel = canvas.get_pixel(i)
                position = (canvas.get_size() - 1 - i) if invert else i
                ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
            ledshim.show()
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        ledshim.clear()
        ledshim.show()


if __name__ == '__main__':
    display_effects()
