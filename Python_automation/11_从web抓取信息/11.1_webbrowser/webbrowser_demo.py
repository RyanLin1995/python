# webbrowser_demo - Launches a map in the browser using a address from the command line or clipboard
# example "webbrowser_demo.py 12345678 1234567 1a"

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address_number = sys.argv[1:]

else:
    address_number = pyperclip.paste().split(",")


webbrowser.open(r"https://map.baidu.com/@{},{},{}".format(address_number[0], address_number[1], address_number[2]))