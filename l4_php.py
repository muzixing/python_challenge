import re
import urllib
import time

"""
    This application use to retrive the answer by urllib.
    when nothing == 16044,the message shows that
    you should devide by two and keep going.
"""
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
reply = "and the next nothing is (\d+)"
nothing = "8022"

while True:
    try:
        source = urllib.urlopen(uri % nothing).read()
        nothing = re.search(reply, source).group(1)
    except:
        print "except"
        break
    print nothing
