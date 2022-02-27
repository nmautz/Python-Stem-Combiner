import os

from pydub import AudioSegment
import sys
from os.path import exists

fileExists = True

if len(sys.argv) < 3:
    print("More arguments required... eg\n python3 stemcombine.py file1.wav file2.wav ")
else:
    for i in range(1, len(sys.argv)):
        if not exists(sys.argv[i]):
            fileExists = False

    if fileExists:
        combined_sounds = AudioSegment.from_wav(sys.argv[1])
        for i in range(2, len(sys.argv)):
            combined_sounds = combined_sounds.overlay(AudioSegment.from_wav(sys.argv[i]))

        if not exists("result.wav"):
            os.system("touch result.wav")

        combined_sounds.export("result.wav", format="wav")

    else:
        print("One or more files do not exist!!!")





