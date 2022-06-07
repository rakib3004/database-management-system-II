from datetime import datetime
from datetime import date
import validators
from validators import ValidationFailure
import requests
from re import T
import sys
from youtube_transcript_api import YouTubeTranscriptApi as yta
from time import sleep
from urllib import response
from requests import session
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import random




def autoGenerateURL(current_time):
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

        f = open("Product.txt", "a")
        f.write(video_id,'::::::',current_time)
        f.close()


        sys.stdout.flush()
    except:
        f = open("Garbage.txt", "a")
        f.write(video_id,'::::::',current_time)
        f.close()








time='06/07/22 09:54:25'
time=time.replace("\r","")

finish_time = datetime.strptime(time, '%m/%d/%y %H:%M:%S')

finish_timestamp = datetime.timestamp(finish_time)
finish_timestamp = int(finish_timestamp)






current_time = datetime.now()

current_timestamp = datetime.timestamp(current_time)
current_timestamp = int(current_timestamp)

while(current_timestamp is not finish_timestamp):
    current_time = datetime.now()


    autoGenerateURL(current_time)
    
    current_timestamp = datetime.timestamp(current_time)
    current_timestamp = int(current_timestamp)
    current_timestamp = finish_timestamp


