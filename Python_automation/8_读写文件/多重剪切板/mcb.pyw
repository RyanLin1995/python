#! python3
# mcb.py - Save and loads pieces of the clipboard
# Usage: pv.exe mcb.py save <keyword> - Saves clipboard to keyword
#        py.exe mcb.py <keyword> - Loads keyword to clipboard
#        py.exe mcb.py list - Loads all keywords to clipborad
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
print(sys.argv)
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and list content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()