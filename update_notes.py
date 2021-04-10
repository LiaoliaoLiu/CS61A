import os
import os.path
import shutil

srcfiles = os.listdir('notes')

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if dirpath != './notes']:
        if filename in srcfiles:
            shutil.move(os.path.join('./notes', filename), os.path.join(dirpath, filename)) 
            print('replace ', os.path.join(dirpath, filename), 'with ', os.path.join('./notes', filename))