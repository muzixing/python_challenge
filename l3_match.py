import re
import string_example

"""
    One small letter,
    surrounded by EXACTLY three big bodyguards on each of its sides.
"""


class StingMatch(object):
    """String match """
    def __init__(self):
        self.msg = string_example.string

    def match(self):
        Pattern = '[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'
        result = re.findall(Pattern, self.msg)

        print (''.join(x[4:5] for x in result))


def main():
    test = StingMatch()
    test.match()

if __name__ == '__main__':
    main()
