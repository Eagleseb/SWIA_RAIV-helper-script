import sys
import os, os.path
import shutil
import numpy as np
import glob

def shuffle_files(pattern):
    files = glob.glob(pattern)
    np.random.shuffle(files)
    return files

def shuffle_dir(dir):
    files = os.listdir(dir)
    for f in files:
        shutil.move(os.path.join(dir, f), os.path.join(dir, f + '.tmp'))
    for i, f in enumerate(os.listdir(dir)):
        shutil.move(os.path.join(dir, f), os.path.join(dir, str(i) + '.jpg'))

def copy_all(files, dest):
    for f in files:
        shutil.copy(f, os.path.join(dest, os.path.split(f)[1]))

def remove_all(files):
    for f in files:
        os.remove(f)

def draw(pattern, dest, count=1, remove=False):
    drawn = shuffle_files(pattern)[:count]
    copy_all(drawn, dest)
    if remove:
        remove_all(drawn)

if __name__ == '__main__':
    print('Choose option:')
    print('1) setup campaign ( /!\ first delete any previous campaign)')
    print('2) add rebel aid to event deck')
    print('3) add imperial agenda to event deck')
    print('4) shuffle event deck')

    option = int(input())
 
    if option == 1:
        events_pattern = "./cards/Events/*/*.jpg"

        os.makedirs('./campaign/event_deck')
        os.makedirs('./campaign/imperial_agenda')
        os.makedirs('./campaign/rebel_aid')
            
        copy_all(shuffle_files(events_pattern)[:25], './campaign/event_deck')
        copy_all(glob.glob('./cards/Imperial Agenda/*.jpg'), './campaign/imperial_agenda')
        copy_all(glob.glob('./cards/Rebel Aid/*.jpg'), './campaign/rebel_aid')

        draw('./campaign/imperial_agenda/*.jpg', './campaign/event_deck', remove=True)
        draw('./campaign/rebel_aid/*.jpg', './campaign/event_deck', remove=True)
        shuffle_dir('./campaign/event_deck')
    elif option == 2:
        draw('./campaign/rebel_aid/*.jpg', './campaign/event_deck', remove=True)
        shuffle_dir('./campaign/event_deck')
    elif option == 3:
        draw('./campaign/imperial_agenda/*.jpg', './campaign/event_deck', remove=True)
        shuffle_dir('./campaign/event_deck')
    elif option == 4:
        shuffle_dir('./campaign/event_deck')


