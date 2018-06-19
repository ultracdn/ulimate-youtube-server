import pychromecast
import pafy
chromecasts = pychromecast.get_chromecasts()
for x in chromecasts:
    x.wait()
def pause():
    for x in chromecasts:
        x.media_controller.pause()
def play():
    for x in chromecasts:
        x.media_controller.play()
def yt(url):
    v=pafy.new(url)
    aud = v.getbest(preftype="mp4")
    #print(v.audiostreams)
    u=aud.url
    for x in chromecasts:
        x.media_controller.play_media(u,"video/mp4")
def vol(i):
    for x in chromecasts:
        x.set_volume(i)
        
