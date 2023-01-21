import json
import os
import platform
import sys
import utils

file = open('./config.json', 'r+', encoding='UTF-8')
config = json.load(file)
file.close()

file = open('./db.json', 'r+', encoding='utf-8')
db = json.load(file)
file.close()

iD = 0
iDs = {}

print(utils.Color.red + str(iD) + utils.Color.reset + '\t' + 'Quit Program')
print('----------')

for i in db['video']:
    iD = iD + 1
    iDs[iD] = i
    print(utils.Color.red + str(iD) + utils.Color.reset + '\t' + db['video'][i]['title'] + '\t\t' + utils.Color.green +
          db['video'][i]['tags'].replace("'", '') + utils.Color.reset)  # Print all Videos in db

user_input = input('\n\nInput Video ID!\n>')
user_input = int(user_input)
if user_input == 0:
    sys.exit(0)

video_to_start_id = iDs[user_input]
video_path = db['video'][video_to_start_id]['path']
if platform.system() == 'windows':
    vlc = config['VLC-path']
    os.system(vlc + ' "' + video_path + '"')
elif platform.system() == 'linux' or 'linux2':
    os.system('vlc "' + video_path + '"')
