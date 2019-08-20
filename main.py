import OsuFileTools



def editAllBeatmapAR(songs_dir, ar):
    ar = str(ar)
    
    paths = OsuFileTools.getAllBeatmapsFolderPath(songs_dir)

    for bm_path in paths:
        for diff_file in OsuFileTools.BMlistDifficulties(bm_path):
            # on veux changer l'AR de seulement les maps en std

            if OsuFileTools.getMod(diff_file) == '0':     # si c'est du std
                #print(diff_file)
                OsuFileTools.editAR(diff_file, ar)       # on change l'AR

def restoreAllBeatmapAR(songs_dir):
    paths = OsuFileTools.getAllBeatmapsFolderPath(songs_dir)

    for bm_path in paths:
        for diff_file in OsuFileTools.BMlistDifficulties(bm_path):
            # on veux changer l'AR de seulement les maps en std
            
            if OsuFileTools.getMod(diff_file) == '0':     # si c'est du std
                OsuFileTools.restoreAR(diff_file)