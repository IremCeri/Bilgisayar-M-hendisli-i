import pytube
from pytube import YouTube
import time

url=input("YouTube Url Giriniz")
YouTube1=YouTube(url)

print(YouTube1.title)
print(YouTube1.views)
print(YouTube1.author)
print(time.strftime("%H: %M: %S",time.gmtime(YouTube1.length)))
print(YouTube1.captions)
print(YouTube1.description)
print(YouTube1.keywords)
print(YouTube1.publish_date)


print(YouTube1.streams.get_highest_resolution())
videos= YouTube1.streams.filter(progressive=True)
for video in videos:
    print(video.resolution,"indiriliyorrr....")
    video.download()