import os

print("started...")

osu_path = "C:\\Games\\osu!"
songs_dir = osu_path + "\\Songs"
bmaps  = [x for x in os.listdir(songs_dir) if x != "fr.txt"]        # la langue peux varier edit ça


def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext

print(check_extension("caca.py", "py"))

for bmap in bmaps:
    #print(bmap)

    difficulty = [m for m in os.listdir(songs_dir + "\\" + bmap) if check_extension(m, "osu")]
    print(difficulty)