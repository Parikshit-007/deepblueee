import os
from django.conf import settings
from webapp.models import Video
import whisper
from django.http import HttpResponse

def process_video(request):
    video = Video.objects.get(title='your_video_title')

    # set the input and output file paths for mp3 conversion
    input_path_mp3 = os.path.join(settings.BASE_DIR, f'media/{video.title}.mp4')
    output_path_mp3 = os.path.join(settings.BASE_DIR, f'media/{video.title}.mp3')

    # execute the ffmpeg command to convert video to mp3
    command_mp3 = f"ffmpeg -i {input_path_mp3} {output_path_mp3}"
    os.system(command_mp3)

    # set the input and output file paths for transcription
    input_path_transcription = output_path_mp3
    output_path_transcription = os.path.join(settings.BASE_DIR, f'media/{video.title}.txt')

    # execute the whisper transcription command
    model = whisper.load_model("base")
    result = model.transcribe(input_path_transcription)
    transcript = result["text"]

    # save the transcription to a file
    with open(output_path_transcription, 'w') as file:
        file.write(transcript)

    # return a response with the transcription text
    return HttpResponse(transcript)
