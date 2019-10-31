"""Python program to print colored text and background"""


class Colors:
    """Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold"""
    def __init__(self):
        self.reset = '\033[0m'
        self.bold = '\033[01m'
        self.disable = '\033[02m'
        self.underline = '\033[04m'
        self.reverse = '\033[07m'
        self.strikethrough = '\033[09m'
        self.invisible = '\033[08m'
        self.fg_black = '\033[30m'
        self.fg_red = '\033[31m'
        self.fg_green = '\033[32m'
        self.fg_orange = '\033[33m'
        self.fg_blue = '\033[34m'
        self.fg_purple = '\033[35m'
        self.fg_cyan = '\033[36m'
        self.fg_lightgrey = '\033[37m'
        self.fg_darkgrey = '\033[90m'
        self.fg_lightred = '\033[91m'
        self.fg_lightgreen = '\033[92m'
        self.fg_yellow = '\033[93m'
        self.fg_lightblue = '\033[94m'
        self.fg_pink = '\033[95m'
        self.fg_lightcyan = '\033[96m'
        self.bg_black = '\033[40m'
        self.bg_red = '\033[41m'
        self.bg_green = '\033[42m'
        self.bg_orange = '\033[43m'
        self.bg_blue = '\033[44m'
        self.bg_purple = '\033[45m'
        self.bg_cyan = '\033[46m'
        self.bg_lightgrey = '\033[47m'


# print(Colors().bg_black, "SKk", Colors().fg_red, "Amartya")
# test = Colors().underline_print('bonjour')
# print('')
# print(Colors().bg_red, Colors().fg_black, "SKk", Colors().fg_black, "Amartya")

print(Colors().bg_red, ';')
print(Colors().bg_black, ';')