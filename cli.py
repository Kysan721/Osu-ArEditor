from main import *      # idk si c'est légal
import os.path

print("---------------------------")
print("| Osu! Beatmaps AR editor |")
print("---------------------------")


def saveSongDir(path):
    with open('config.kys', 'w', encoding='utf-8') as f:
        f.write(path)


def getSavedSongDir():
    with open('config.kys', 'r', encoding='utf-8') as f:
        return f.readlines()[0].strip()


# si le fichier configuration existe
if os.path.isfile('config.kys'):
    path = getSavedSongDir()
else:
    path = ''

while 1:
    cmd = input("kyshell@osuAReditor>> ")
    args = cmd.split()[1:]
    cmd = cmd.split()[0]  # osef de l'opti

    # commande d'édition
    if cmd in ['edit','set']:
        # pour modifié l'emplacement des maps si il n'est pas bien configuré
        if args[0].lower() == 'path':
            path = " ".join(args[1:])
            if os.path.exists(path):
                saveSongDir(path)           # on le sauvegarde dans un fichier
                print('songs directory path saved ({})'.format(path))
            else:
                print('invalide path')

        # pour modifié l'ar des maps
        elif args[0].lower() == 'ar':
            ar = args[1]
            print('editing all beatmap to ar {}'.format(ar))
            if path != '':
                editAllBeatmapAR(path, ar)
                print('finish')
            else:
                print("can't edit beatmaps ar because osu songs directory is not configured plz use `set path <path to your osu songs directory>`")
        else:
            print('unknow command')

    elif cmd == 'get':
        if args[0] == 'path':
            print('osu songs directory path : ' + path)
        else:
            print('unknow command')

    elif cmd == 'restore':
        if path != '':
                restoreAllBeatmapAR(path)
                print('finish')
        else:
            print("can't edit beatmaps ar because osu songs directory is not configured plz use `set path <path to your osu songs directory>`")
    elif cmd == 'help':
        print('avalliable commands:')
        print(' - edit <path/ar> <valeur>')
        print('     exemple:')
        print('         `edit ar 9` vas mettre l\'ar de toute vos map à 9')
        print('         `edit path C:/Games/osu!/Songs permet de configurer le chemin d\'acces à toute les maps')
        print(' - restore   : remet toutes vos maps comme elle était avant  ')
        print(' - exit/quit : pour quitter le cli')
    elif cmd in ['exit','quit']:
        break
    else:
        print('unknow command type help for help')


