import os
import sys
import fileinput






def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext


# pour exclure tout ce qui est pas du std
def check_mod(osu_file):
    pass
    """
    StackLeniency: 0.7
    Mode: 0
    LetterboxInBreaks: 1
    """

def editAR(osuFile, newAR):
    print(osuFile)
    
    for line in fileinput.FileInput(osuFile, inplace=1):
        if line.split(':')[0] == 'ApproachRate':
            AR = line.split(':')[1]
            print(AR)
            line = line.replace(AR, newAR)      # marche pas wtf


osu_path = "C:\\Games\\osu!"
songs_dir = osu_path + "\\Songs"
beatmaps_path  = [x for x in os.listdir(songs_dir) if x != "fr.txt"]        # la langue peux varier edit ça



for bmp in beatmaps_path:
    #print(bmap)

    # seulement les fichiers en .osu nous interesse
    difficulties = [d for d in os.listdir(songs_dir + "\\" + bmp) if check_extension(d, "osu")]
    # il y en a une par difficulté
    for diff in difficulties:
        osuFile = songs_dir + "\\" + bmp + "\\" +diff
        editAR(osuFile, 8)



# peut être faire un cli