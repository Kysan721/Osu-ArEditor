import os


def editARInOsuFile(filePath, newAR):
    newAr = str(newAR)      # au cas ou on passe un int
    # on lis le fichier
    with open(filePath, 'rt') as rFile:
        tmp = rFile.readlines()

    # on réecrit sur ce qu'il y a modifier
    with open(filePath, 'wt') as wFile:
        for line in tmp:
            print(line)
            if 'ApproachRate:' in line[:13]:
                wFile.write('ApproachRate:{}\n'.format(newAr))
            else:
                wFile.write(line)



# (0=osu!, 1=osu!taiko, 2=osu!catch, 3=osu!mania)
def getMod(osu_file):
    with open(osu_file, 'r', errors='ignore') as f:
        for line in f.readlines():
            if 'Mode:' in line or 'mode:' in line:
                print(line)
                return line.split(':')[1].strip()
        return -1


# retourne une liste avec le chemin d'acces a tout les dossiers de map
def getAllBeatmapsFolderPath(osuSongsDir):
    # pour chaque element du dossier osuSongDir on recupère osuSongsdir+/+element si l'element est bien un dossier
    return [osuSongsDir+'/'+e for e in os.listdir(osuSongsDir) if os.path.isdir(osuSongsDir+'/'+e)]


# pour vérifié si l'extention d'un fichier est bien la bonne
def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext


def BMlistDifficulties(bm_folder_path):
    return [bm_folder_path+'/'+f for f in os.listdir(
        bm_folder_path) if check_extension(bm_folder_path+'/'+f, "osu")]


# pour les tests
# editARInOsuFile('test.txt', '9')
