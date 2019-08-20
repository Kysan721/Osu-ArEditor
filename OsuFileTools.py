import os

def cat(filePath):
    with open(filePath, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()
        for line in lines:
            print(line.strip())

def isFileAlreadyEdited(filePath):
    # il est déjà edité si il comptiens le champs 'backupAR:'
    with open(filePath, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()
        for line in lines:
            if 'backupAR:' in line:
                return True
        return False


def editAR(filePath, newAR):
    newAR = str(newAR)
    needBackup = not isFileAlreadyEdited(filePath)
    
    with open(filePath, 'rt', encoding='utf-8') as rFile:
        tmp = rFile.readlines()

    # on réecrit sur ce qu'il y a modifier
    with open(filePath, 'wt', encoding='utf-8') as file:
        for line in tmp:
            #  on trouve la ligne de l'approche rate on modifie
            if 'ApproachRate:' in line:
                # on fait une sauvegarde si besoin
                if needBackup:
                    backupAR = line.split('ApproachRate:')[1].strip()
                    file.write('backupAR:{}\n'.format(backupAR))
                
                file.write('ApproachRate:{}\n'.format(newAR))
            
            else:
                # si non on réecrit juste ce qu'il y avait déjà et qu'on a en mémoire (tmp)
                file.write(line)

def getBackupAR(filePath):
    ar = ""
    with open(filePath, 'rt', encoding='utf-8') as rf:
        lines = rf.readlines()
    for line in lines:                  # on lis chaque ligne jusqu'a trouvé le champs qui nous interesse
        if "backupAR:" in line.strip():
            ar = str(line.split('backupAR:')[1])        # on retrouve l'ancienne ar sur la ligne
            return ar
    return ''



def restoreAR(filePath):
    if isFileAlreadyEdited(filePath):
        backupedAR = getBackupAR(filePath)

    # on lis le fichier et on fait une copie en mémoire
    with open(filePath, 'r', encoding='utf-8') as rf:
        copy = rf.readlines()

    with open(filePath, 'w', encoding='utf-8')as wf:
        for line in copy:
            if 'backupAR:' in line:      # on écrit rien pour supprimer le champs
                pass
            if 'ApproachRate:' in line:
                wf.write('ApproachRate:{}\n'.format(backupedAR))
            else:
                wf.write(line)




# (0=osu!, 1=osu!taiko, 2=osu!catch, 3=osu!mania)
def getMod(osu_file):
    with open(osu_file, 'r',  encoding='utf-8') as f:
        for line in f.readlines():
            if 'Mode:' in line or 'mode:' in line:

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




class OsuFile:
    def __init__(self, path):
        self.path = path
    
    def mod(self):
        with open(self.path, 'r',  encoding='utf-8') as f:
            for line in f.readlines():
                if 'Mode:' in line or 'mode:' in line:

                    return line.split(':')[1].strip()
            return -1
