"""
This script reads the MyClippings.txt file from one's Kindle and sorts the notes based on the book name.
The script also moves the MyClippings.txt file to a history directory on your computer. This is done so
that the same notes aren't created everytime this script is run.
"""


import datetime, os, shutil, sys


# Directory of the My Clippings.txt file
file_dir = "/media/{add_your_username_here}/Kindle/documents/My Clippings.txt"

# Directory where you want the notes to be saved to
notes_dir = "/home/{add_your_username_here}/Documents/Kindle Notes/"

"""
Directory to which you wish to move the notes from the My Clippings.txt file. This is done primarily
to avoid the same notes being re-written each time you run this script
"""
hist_dir = "/home/{add_your_username_here}/Documents/Kindle Notes/history/"

try:
        notes = open(file_dir, mode='r').read()
except FileNotFoundError:
        print("No MyClippings.txt found!")
        sys.exit()

# Kindle ends each note with '=========='
each_note = notes.split('==========')

"""
Dissecting each note into various components
You'll probably understand this bit better if you look at the My Clippings.txt
"""
for n in range(len(each_note)-2):
    book_name = each_note[n].split('\n')[-5]
    point = each_note[n].split('\n')[-2]
    file_name = os.path.join(notes_dir, book_name+'.txt')

    f = open(file_name, mode='a+')
    f.write(point)
    f.write('\n\n')
    f.close()

"Move the notes to local drive to prevent multiple versions of the same notes"
shutil.move(file_dir, hist_dir+'notefile'+str(datetime.datetime.now())+'.txt')
print("All done!")
