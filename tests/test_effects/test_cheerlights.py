import unittest
import mock

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects import CheerLights


class TestCheerLights(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_cheerlight_call(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLights(canvas)
        self.assertIsNone(effect.get_colour_from_channel("http://ejiferfneciudwedwojcmeiocnw.com"))

    @mock.patch('ledshimdemo.effects.CheerLights.get_colour_from_channel', return_value=None)
    def test_effect_failed_cheerlights(self, patch_function):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLights(canvas)
        effect.compose()
        patch_function.assert_called_once()
        for i in range(canvas.get_size()):
            self.assertEqual(canvas.get_pixel(i), canvas.BLANK_PIXEL)

    def test_effect_working_cheerlights(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLights(canvas)
        # Must check before and after in case it changes during the test.
        before = effect.get_colour_from_channel(effect.URL)
        effect.compose()
        after = effect.get_colour_from_channel(effect.URL)
        self.assertRegex(repr(effect), "^CheerLights\\(Colour:({0}|{1})\\)$".format(before, after))
