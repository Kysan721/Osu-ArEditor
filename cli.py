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
        print(' -nothing')
        print(' -nothing again')
    elif cmd == 'nothing':
        print('ahah no')
    elif cmd in ['exit','quit']:
        break
    elif cmd == 'help':
        print('not yet implemented ')
    else:
        print('unknow command type help for help')


