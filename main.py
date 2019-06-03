import OsuFileTools

songs_dir = "C:/Games/osu!/Songs"
paths = OsuFileTools.getAllBeatmapsFolderPath(songs_dir)

for bm_path in OsuFileTools.getAllBeatmapsFolderPath(songs_dir):
    print(bm_path)
    for diff_file in OsuFileTools.BMlistDifficulties(bm_path):
        # on veux changer l'AR de seulement les maps en std
        if OsuFileTools.getMod(diff_file) == 0:
            OsuFileTools.editAR(diff_file, 8)


# peut être faire un cli