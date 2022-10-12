import os
import sys
from pydub import AudioSegment

def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    allfiles = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            allfiles.append(os.path.join(path, name))
    return allfiles

def mp3_2_wav(filelist):
    """Return a list of converted .wav files given a list of fully-qualified mp3 files
    """
    for file in filelist:
        sound = AudioSegment.from_mp3(file)
        dst = os.path.join('wav',os.path.basename(file).replace('mp3', 'wav'))
        sound.export(dst, format = 'wav')

# take in the list of files
mp3_folder = sys.argv[1]
mp3_files = filelist(mp3_folder)
mp3_2_wav(mp3_files)