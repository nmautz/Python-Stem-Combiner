import os

from pydub import AudioSegment
import sys
from os.path import exists


def extractAudio(fileName):
    if not fileName is str:
        fileName = str(fileName)
    if fileName[len(fileName) - 1] == "v":
        return AudioSegment.from_wav(fileName)
    if fileName[len(fileName) - 1] == "3":
        return AudioSegment.from_mp3(fileName)


fileExists = True

if len(sys.argv) < 3:
    print("More arguments required... eg\n python3 stemcombine.py file1.wav file2.wav ")
else:
    for i in range(1, len(sys.argv)):
        if not exists(sys.argv[i]):
            fileExists = False

    if fileExists:
        combined_sounds = extractAudio(sys.argv[1])
        print(type(combined_sounds))
        for i in range(2, len(sys.argv)):
            combined_sounds = combined_sounds.overlay(extractAudio(sys.argv[i]))

        if not exists("result.wav"):
            os.system("touch result.wav")

        combined_sounds.export("result.wav", format="wav")

    else:
        print("One or more files do not exist!!!")
