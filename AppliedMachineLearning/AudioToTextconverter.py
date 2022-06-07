from re import T
import sys
from youtube_transcript_api import YouTubeTranscriptApi as yta
from time import sleep
from urllib import response
from requests import session
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import random

characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'

youtubeurl = ''

for i in range(0, 11):
    youtubeurl += random.choice(characters)


print(youtubeurl)

video_id = youtubeurl

try:
    data = yta.get_transcript(video_id)
    transcript = ''
    for value in data:
        for key, val in value.items():

            if key == 'text':
                val=str(val)
                newVal=val.strip('\n')
                print(newVal,end="")
                transcript += newVal+" "




    transcript=transcript.strip()
    transcript=transcript.replace("\n"," ").replace("\r"," ")

   

    print(transcript)

    sys.stdout.flush()
except:
    print(video_id,'error')
