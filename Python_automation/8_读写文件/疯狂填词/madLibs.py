# Read content from the txt file and find the adjective, noun and verb. Then replace them.

# the adjective panda walked to the noun and then verb. a nearby noun was unaffected by these events.
import re

# Open the file and find the adjective(形容词), noun(名词) and verb(动词)
with open('madlibs.txt') as f:

    contects = f.read()
    while True:
        search = re.compile(r'adjective|noun|verb')
        ret = search.search(contects)
        if ret:
            print("Enter an {}".format(ret.group()))
            replace = input()
            contects = search.sub(replace, contects, count=1)
        else:
            break

# let user input the adjective(形容词), noun(名词) and verb(动词)

targetFile = open("TargetMadLibs.txt", 'w')
targetFile.write(contects)
targetFile.close()
