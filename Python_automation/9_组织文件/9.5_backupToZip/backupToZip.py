import os
import zipfile


def backupToZip(folder):
    # A function to backup the folders and files to a zip file

    folder = os.path.abspath(folder)  # make sure the folder path is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:

        zipFileName = "{}_{}.zip".format(os.path.basename(folder), number)
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create the ZIP file
    print("Creating the {}".format(zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, "w")

    # Walk the entire folder tree and compress the files in each folder
    for foldernames, subfolders, filenames in os.walk(folder):

        print("Adding files in {}".format(foldernames))

        # ALl the files in this folder to the zip file
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldernames, filename))
    backupZip.close()


backupToZip(".")


