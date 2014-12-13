import string
import mess_string
from collections import Counter

"""
    Find the rare characters in the mess message.
    Author@muzixing
"""


class Find(object):
    """Find rare characters in the mess message"""
    def __init__(self):
        super(Find, self).__init__()
        self.msg = []

    def find_rare(self):
        self.msg = mess_string.string  # raw_input("Enter the massage\n")
        result = ''
        for letter in self.msg:
            if letter in string.letters:
                result += letter
        print result

    def find_by_counter(self):
        count_map = Counter(mess_string.string)
        soap = count_map.most_common()
        for k in soap:
            print k[0]


def main():
    test = Find()
    test.find_rare()
    #test.find_by_counter()

if __name__ == '__main__':
    main()
