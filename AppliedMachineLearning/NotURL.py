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



def is_string_an_url(url_string):
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        print(url_string,'is not available')
        return False
    print(url_string,'is available')
    return result


def check_video_url(video_id):
    checker_url = "https://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    request = requests.get(video_url)

    return request.status_code == 200




