import os
from django.conf import settings
from webapp.models import Video

# get the video object
video = Video.objects.get(title='your_video_title')

# set the input and output file paths
input_path = os.path.join(settings.BASE_DIR, f'media/{video.title}.mp4')
output_path = os.path.join(settings.BASE_DIR, f'media/{video.title}.mp3')

# execute the ffmpeg command
command = f"ffmpeg -i {input_path} {output_path}"
os.system(command)
