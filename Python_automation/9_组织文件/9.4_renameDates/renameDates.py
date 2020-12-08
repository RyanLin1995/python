import shutil
import re
import os

euroPath = "./euroFilename"
amerPath = "./amerFilename"
try:
    os.makedirs(euroPath)

except:
    pass

# Create a regex that matches files with the American data format.
datePattern = re.compile(r"""^(.*?) # all the text before date
(([01])?\d)- # one or two digits for the month
(([0123])?\d)- # one or two digits for the day
(([1920])?\d\d) # four digits for the year
(.*?)$ # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir(amerPath):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo is None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    datePart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename
    euroFilename = "{}{}-{}-{}{}".format(beforePart, datePart, monthPart, yearPart, afterPart)

    # Get the full, absolute file paths
    euroAbsWorkingDir = os.path.abspath(euroPath)
    amerAbsWorkingDir = os.path.abspath(amerPath)
    amerAbsFilename = os.path.join(amerAbsWorkingDir, amerFilename)
    euroAbsFilename = os.path.join(euroAbsWorkingDir, euroFilename)

    # Rename the file
    print("Change the name from {} to {}".format(amerAbsFilename, euroAbsFilename))
    shutil.move(amerAbsFilename, euroAbsFilename)
