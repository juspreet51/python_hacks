import os

BestOfEminemPath = r"E:\BestOfEminem"
BestOfEminemSongs =  os.listdir(BestOfEminemPath)

BestOfEminem2Path= r"E:\BestOfEminem2"
BestOfEminem2Songs =  os.listdir(BestOfEminem2Path)

for song in BestOfEminemSongs:
    if song in BestOfEminem2Songs:
        commonSong = os.path.join(BestOfEminem2Path,song)
        os.remove(commonSong)


print("Done!!!")
