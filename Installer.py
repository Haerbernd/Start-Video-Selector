import json
import os
import platform
import utils
import sys
import urllib.request as url

if __name__ == '__main__':
    print('Start creating necessary files...')
    # Create necessary Files
    file = open('./config.json', 'w', encoding='utf-8')  # Creates the config.json file
    file.write('{"VLC-path": ""}')
    file.close()

    file = open('./db.json', 'w', encoding='utf-8')  # Creates the db.json file, in which the video data is saved
    file.write('{\n"video": {\n"aaa001": {\n"title": "",\n"path": "",\n"tags": []\n}\n}\n}')
    file.close()
    print('Done...')

    # Compile/Create program
    if platform.system() == 'windows':
        print('Start to compile program...')
        os.system('pyinstaller --noconfirm --onefile --console --icon "favicon.ico" --name "Start Video Selector" '
                  '--add-data "utils.py;."  ""')  # Python compile to .exe
    elif platform.system() == 'linux' or 'linux2':
        print('Start to create .sh file')
        file = open('./start-video-selector.sh', 'w', encoding='utf-8')  # Create the start .sh file
        file.write('python "' + __file__ + 'start-video-selector.py"')
        file.close()

    # VLC
    vlc_installed = utils.yesnoquestion('Do you have VLC installed?')
    if vlc_installed:
        if platform.system() == 'windows':
            vlc_path = input('Enter path to vlc.exe')
            file = open('./config.json', 'w', encoding='utf-8')
            config = json.load(file)
            config['VLC-path'] = vlc_path
            file.write(config)
            file.close()
    else:
        if platform.system() == 'windows':
            url.urlretrieve('https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe', 'vlc-installer.exe')
            os.system('"vlc-installer.exe"')
        elif platform.system() == 'linux' or 'linux2':
            way_to_install = input('In which way do you want to download VLC, snap, apt or pacman?\n>')
            if way_to_install == 'snap':
                os.system('sudo snap install vlc')
            elif way_to_install == 'apt':
                os.system('sudo apt install vlc')
            elif way_to_install == 'pacman':
                os.system('sudo pacman -S vlc')
            else:
                print('Unknown Answer!')
                sys.exit(0)

    print('Start Video Selector was successfully installed')
    sys.exit()
