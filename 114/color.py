import os
import sys
import urllib.request
import re

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color: str):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())

    @staticmethod
    def hex2rgb(hex_val: str):
        """Class method that converts a hex value into an rgb one"""
        is_valid_hex = re.compile("^#[A-Fa-f0-9]{6}$")

        if not isinstance(hex_val, str) or not re.search(is_valid_hex, hex_val):
            raise ValueError('Input must be a valid six-character hex string')

        return int(hex_val[1:3], 16), int(hex_val[3:5], 16), int(hex_val[5:7], 16)

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb, tuple) or not all(i in range(0, 256) for i in rgb):
            raise ValueError('Input must be a tuple containing RGB values.')

        r, g, b = rgb
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb is not None else 'Unknown'
