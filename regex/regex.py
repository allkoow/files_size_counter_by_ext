import re

message = """file.mp3 100b
movie.mp4 200b
mov.mp3ie.mp4 200b
music.flac 100b
tenor.mkv 200b
data.7z 150b
errno.zip 150b"""

musicExts = re.compile('(.mp3$|.flac$)')
movieExts = re.compile('(.mp4$|.mkv$)')
otherExts = re.compile('(.+$)')

musicCount = 0
movieCount = 0
otherCount = 0

lines = re.split('\n+',message)
lines = [re.split(' ', line) for line in lines]

for line in lines:
    line[1] = re.sub('b','',line[1])
    
    if musicExts.search(line[0]):
        musicCount += int(line[1])
    elif movieExts.search(line[0]):
        movieCount += int(line[1])
    elif otherExts.search(line[0]):
        otherCount += int(line[1])

list = "music " + str(musicCount) + "b\n"
list += "movie " + str(movieCount) + "b\n"
list += "other " + str(otherCount) + "b\n"

print(list)