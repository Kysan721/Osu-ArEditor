import os
import sys



osu_path = "C:\\Games\\osu!"
songs_dir = osu_path + "\\Songs"
beatmaps_path  = [x for x in os.listdir(songs_dir) if x != "fr.txt"]        # la langue peux varier edit ça


def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext


def editAR(osuFile, newAR):
    with open(osuFile, "rw"):
        """
        parse le fichier trouve la ligne ou il est écrit
        ApproachRate: X
        la modifie en changant X par newAR
        """



for bmp in beatmaps_path:
    #print(bmap)

    # seulement les fichiers en .osu nous interesse
    difficulty = [d for d in os.listdir(songs_dir + "\\" + bmp) if check_extension(d, "osu")]
    # il y en a une par difficulté
    print(difficulty)



# peut être faire un cli