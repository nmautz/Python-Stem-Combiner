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
    for i in range(1, len(sys.argv)-1):
        if not exists(sys.argv[i]):
            print("File not found! \n " + sys.argv[i])
            fileExists = False

    if fileExists:
        combined_sounds = extractAudio(sys.argv[1])
        for i in range(2, len(sys.argv)-1):
            combined_sounds = combined_sounds.overlay(extractAudio(sys.argv[i]))

        if not exists(sys.argv[len(sys.argv)-1]):
            os.system("touch " + sys.argv[len(sys.argv)-1])

        resultFile = sys.argv[len(sys.argv)-1]

        extention = resultFile[len(resultFile)-3]
        extention += resultFile[len(resultFile)-2]
        extention += resultFile[len(resultFile)-1]


        combined_sounds.export(sys.argv[len(sys.argv)-1], format=extention)

    else:
        print("One or more files do not exist!!!")
