import json
import os
import sys
import utils

file = open('config.json', 'r+', encoding='UTF-8')
config = json.load(file)
file.close()

path = config['path']

iD = 0
iDs = {"id": {"1": ""}}

print(utils.Color.red + '0' + utils.Color.reset + ' Exit Program\n---------------')
for i in os.listdir(path):
    if i.startswith('vid-'):
        filepath = path + '\\' + i + '\\meta.json'
        iD = iD + 1
        iDs['id'][iD] = i
        file = open(filepath, 'r+', encoding='UTF-8')
        meta = json.load(file)
        print(utils.Color.red + str(iD) + utils.Color.reset + ' ' + meta['videoName'] + "\t" +
              utils.Color.green + str(meta['tags']).replace("'", '') + utils.Color.reset)
        file.close()

print('\nWhat Video do you want to start? [id]')

video_to_start_id = input('>')
video_to_start_id = int(video_to_start_id)
if video_to_start_id == 0:
    sys.exit(0)

video_to_start_path = path + '\\' + iDs['id'][video_to_start_id] + '\\video.mp4'
os.system(config['vlc-path'] + ' ' + video_to_start_path)
