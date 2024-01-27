import os
from pathlib import Path

# subdir dictionary tracks extensions of files
subdir = {
    "Documents:"[".pdf", ".docx", ".txt"],
    "Audio:"[".m4a", ".m4b", ".mp3"],
    "Video:"[".mkv", ".mov", ".mp4"],
    "Images:"[".jpg", ".jpeg", ".png"]
}

def pickDir(value): # Picks directory and undergoes a for loop that checks the contents of the dictionary
    for category, ekstensi in subdir.items(): # Checks category and extensions
        for suffix in ekstensi:
            if suffix == value:
                return category # Returns to for loop and stored for later use

def organizeDir(): # Scans the directory and looks for extension  of file then moves it to the category
    for item in os.scandir(): # When for loop is ran with OS function of scanning directory, script will loop and scan directories of a computer

        if item.is_dir(): # Checks for loop is a directory before it can run through the if statement
            continue

        filePath = Path(item) # Defines path of file
        fileType = filePath.suffix.lower() # Checks string
        directory = pickDir(fileType) # Calls pickDir function from checked string

        if directory == None: # Skips if file extension is not defined
            continue

        directoryPath = Path(directory)
        if directoryPath.is_dir() != True: # Makes a new directory if the category's directory not found
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDir() # Calls function to run script 

        