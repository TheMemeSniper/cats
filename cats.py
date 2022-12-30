import vlc
import os
import time
import requests
import random
import climage
from io import BytesIO

SCRDIR = os.path.dirname(os.path.realpath(__file__)) # define exactly where this script is

def Sound(sound): # handy function that sleeps for the duration of a sound
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    duration = player.get_length() / 1000
    time.sleep(duration)

goofy = [] # create a new list full of our goofy sounds in SCRDIR/sound
for i in os.listdir(f"{SCRDIR}/sound"):
    goofy.append(f"{SCRDIR}/sound/{i}")

while True:
    gatoreq = requests.get("https://api.thecatapi.com/v1/images/search") # get a random skrunkly from the interwebz
    gatodata = gatoreq.json()
    gato = requests.get(gatodata[0]["url"])
    print(climage.convert(BytesIO(gato.content)))
    Sound(random.choice(goofy))
    time.sleep(random.randint(120,500))





