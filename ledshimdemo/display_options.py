import click

from .effect_parade import AbstractEffectParade


DISPLAY_OPTIONS = [
    click.option('-p', '--effect-parade', 'parade', type=click.Choice(AbstractEffectParade.get_parade_options()),
                 help="How the effects are displayed.", default=AbstractEffectParade.get_default_option(),
                 show_default=True),
    click.option('-d', '--effect-duration', 'duration', type=click.IntRange(1, 180),
                 help="How long to display each effect for, in seconds (1-180).", default=10, show_default=True),
    click.option('-r', '--repeat-run', 'run', type=click.IntRange(1, 240),
                 help="How many times to run the effects before stopping (1-240).", default=1, show_default=True),
    click.option('-b', '--brightness', type=click.IntRange(1, 10),
                 help="How bright the effects will be (1-10).", default=8, show_default=True),
    click.option('-i', '--invert', is_flag=True, help="Change the display orientation.")
]


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options