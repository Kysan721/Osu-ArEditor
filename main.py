import os
import sys
import fileinput




osu_path = "C:\\Games\\osu!"
songs_dir = osu_path + "\\Songs"
beatmaps_path  = [x for x in os.listdir(songs_dir) if x != "fr.txt"]        # la langue peux varier edit ça


def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext


def editAR(osuFile, newAR):
    for line in fileinput.FileInput(osuFile, inplace=1):
        if line.split(':')[0] == 'ApproachRate':
            ar = line.split(':')[1]
            line = line.replace(ar, newAR)


for bmp in beatmaps_path:
    #print(bmap)

    # seulement les fichiers en .osu nous interesse
    difficulty = [d for d in os.listdir(songs_dir + "\\" + bmp) if check_extension(d, "osu")]
    # il y en a une par difficulté
    print(difficulty)
    editAR(difficulty, 8)



# peut être faire un cli