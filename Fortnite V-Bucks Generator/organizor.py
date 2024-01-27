import os
from pathlib import Path

subdir = {
    "Documents:"[".pdf", ".docx", ".txt"],
    "Audio:"[".m4a", ".m4b", ".mp3"],
    "Video:"[".mkv", ".mov", ".mp4"],
    "Images:"[".jpg", ".jpeg", ".png"]
}

def pickDir(value):
    for category, ekstensi in subdir.items():
        for suffix in ekstensi:
            if suffix == value:
                return category

def organizeDir():
    for item in os.scandir(): # When for loop is ran with OS function of scanning directory, script will loop and scan directories of a computer

        if item.is_dir():
            continue

        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)

        if directory == None:
            continue

        