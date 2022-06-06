from datetime import datetime
from datetime import date
import validators
from validators import ValidationFailure
import requests


def is_string_an_url(url_string):
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        print(url_string,'is not available')
        return False
    print(url_string,'is available')
    return result


def check_video_url(video_id):
    checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    request = requests.get(video_url)

    return request.status_code == 200







time='06/07/22 00:56:19'
time=time.replace("\r","")

finish_time = datetime.strptime(time, '%m/%d/%y %H:%M:%S')

finish_timestamp = datetime.timestamp(finish_time)
finish_timestamp = int(finish_timestamp)






current_time = datetime.now()

current_timestamp = datetime.timestamp(current_time)
current_timestamp = int(current_timestamp)

while(current_timestamp is not finish_timestamp):
    current_time = datetime.now()


    videoID='LlkPYoxF5j0'
    valid_status=check_video_url(videoID)

    if(valid_status is True):
        print(videoID,'is valid')
    else:
        print(videoID,'is not valid')

    current_timestamp = datetime.timestamp(current_time)
    current_timestamp = int(current_timestamp)
    current_timestamp = finish_timestamp


