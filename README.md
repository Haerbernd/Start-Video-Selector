# Video Start Selector

This Program allows you to start a video that was previously assigned an id and also print Tags that were edited to it.

## Prerequsites
- VLC Media Player (Alternatively another video player also works, but I recommend using VLC)

## What you have to do before you can use the Video Start Selector
For the Video Start Selector to work you have to use a specific naming scheme for your videos and also do a few more steps for it to properly work.

1. All videos have to be in a folder that starts with `vid-` and all those folders have to be in the same folder
2. The video file in the `vid-` folder has to be called `video.mp4`
3. Besides the `video.mp4` file there has to be a file called `meta.json` in the `vid-` folder
4. The `meta.json` file has to have the following structure, whereby the values that start with # have to be replaced with the values that you need/want:
   
   ``{"videoName": "#NameOfTheVideo", "tags": ["#tag1", "#tag2", "#tag3"]}``

## Setup
The setup is very easy as you can't do much wrong when you simply follow the following steps:
1. Make sure the `Start Video Selector.exe` and the `config.json` are in the same folder
2. Open the `config.json` and edit it as follows
   1. Enter as value for `path:` the path of the folder in which the `vid-` folders are stored (*!Make sure you replace every* \ *in the path with* \\\\)
   2. Enter as value for `vlc-path:` the path to your `vlc.exe` (or the video player you want to use) (*!Make sure you replace every* \ *in the path with* \\\\)
3. Now you can simply start the `Start Video Selector.exe` and everything should work

## How to use
When the Start Video Selector is started it will display all found videos in this format ``ID (i.e. 1) Video-Name Tags`` afterwards you will be promted to input a value.
If this value is 0 than the program will close and for any other value the video with the ID will start.

But Please note however that the inputted value **must** be an integer (a whole number)!

## Questions, Ideas and Problems
If you have any questions, ideas for another program or for improvement of the Video Start Selector or problems with any of my programs please contact me. You can do that by either writing me on Discord (*Haerbernd#9465*) or sending me a message on GitHub.
But if you want an answer quickly I would recommend writing me on Discord.