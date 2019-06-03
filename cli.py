from main import *      # idk si c'est légal

print("---------------------------")
print("| Osu! Beatmaps AR editor |")
print("---------------------------")

while 1:
    cmd = input(">>")
    args = input.split()[1:]        
    cmd = input.split()[0]  # osef de l'opti
    if cmd == 'help':
        print('avalliable commands:')
        print(' - editAR <new ar> : modifie l\'AR de toutes vos map en std, irréversible pour le moment attention)
        print(' - exit/quit : pour quitter le cli')
    elif cmd in ['exit','quit']:
        break
    else:
        print('unknow command type help for help')


