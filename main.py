import OsuFileTools

songs_dir = "C:/Games/osu!/Songs"
paths = OsuFileTools.getAllBeatmapsFolderPath(songs_dir)

for bm_path in OsuFileTools.getAllBeatmapsFolderPath(songs_dir):
    for diff_file in OsuFileTools.BMlistDifficulties(bm_path):
        # on veux changer l'AR de seulement les maps en std
        print(diff_file)
        if OsuFileTools.getMod(diff_file) == 0:
            print(diff_file)
            OsuFileTools.editAR(diff_file, 8)


# peut être faire un cli