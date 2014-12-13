import string
import mess_string
"""
    Letter rotate application.
    Author@muzixing
"""


class letter_rotate(object):
    def __init__(self):
        self.msg = []
        self.result = ''

    def rotate(self):
        self.msg = raw_input("Enter string\n")
        for letter in self.msg:
            if letter >= 'a' and letter <= 'z':
                ascii = (ord(letter) - 96 + 2) % 26 + 96
                self.result += chr(ascii)
            else:
                self.result += ' '
        print '\n' + self.result

    def trans(self):
        intable = "abcdefghijklmnopqrstuvwxyz"
        outtable = "cdefghijklmnopqrstuvwxyzab"

        self.msg = mess_string.string  # raw_input("Enter string\n")
        table = string.maketrans(intable, outtable)

        print self.msg.translate(table)

if __name__ == "__main__":
    test = letter_rotate()
    test.rotate()
    test.trans()
