import datetime, os, shutil

# Directory of the My Clippings.txt file
file_dir = "/media/{your username}/Kindle/documents/My Clippings.txt"
# Directory where you want the notes to be saved to
notes_dir = "/home/{your username}/Documents/Kindle Notes/"
"""
Directory to which you wish to move the My Clippings.txt file. This is done primarily
to avoid the same notes being re-written each time you run this script
"""
hist_dir = "/home/{your username}/Documents/Kindle Notes/history/"

notes = open(file_dir, mode='r').read()

# Kindle ends each note with '=========='
each_note = notes.split('==========')

"""
Dissecting each note into various components
You'll probably understand this bit better if you look at the My Clippings.txt :P
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
