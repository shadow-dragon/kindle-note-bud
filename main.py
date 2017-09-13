import datetime, os, shutil

file_dir = "/media/batman/Kindle/documents/My Clippings.txt"
notes_dir = "/home/batman/Documents/Kindle Notes/"
hist_dir = "/home/batman/Documents/Kindle Notes/history/"

"Read contents of My Clippings.txt"
notes = open(file_dir, mode='r').read()

"Each note ends with =========="
each_note = notes.split('==========')

"Dissecting each note"
for n in range(len(each_note)-2):
    book_name = each_note[n].split('\n')[-5]
    point = each_note[n].split('\n')[-2]
    file_name = os.path.join(notes_dir, book_name+'.txt')

    f = open(file_name, mode='a+')
    f.write(point)
    f.write('\n\n')
    f.close()

"Move the notes"
shutil.move(file_dir, hist_dir+'notefile'+str(datetime.datetime.now())+'.txt')