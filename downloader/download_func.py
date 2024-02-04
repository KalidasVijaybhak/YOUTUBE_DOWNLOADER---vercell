import json
from django.http import HttpResponse
from pytube import YouTube
import io
import re
import io
from django.http import HttpResponse
from pytube import YouTube
from tqdm import tqdm

def download_video(request, url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        mp4_streams = yt.streams.filter(file_extension='mp4')

    # Get the highest resolution video stream
        video_stream = mp4_streams.get_highest_resolution()
        # Get the highest resolution video stream
   
        print(video_stream)
        # Create a buffer to hold the video content
        buffer = io.BytesIO()

        # Download the video content to the buffer
        video_stream.stream_to_buffer(buffer)

        # Create a Django HttpResponse with appropriate headers
        response = HttpResponse(buffer.getvalue(), content_type='video/mp4')
 
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
        response['X-Video-Title'] = yt.title
        return response

    except Exception as e:
        # Handle exceptions (e.g., video not found, download error)
        return HttpResponse(f"Error: {str(e)}", status=500)


def download_audio(request, url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution audio stream (only audio)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Create a buffer to hold the audio content
        buffer = io.BytesIO()

        # Download the audio to the buffer
        audio_stream.stream_to_buffer(buffer)

        # Create a Django HttpResponse with appropriate headers
        response = HttpResponse(buffer.getvalue(), content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp3"'
        response['X-Audio-Title'] = yt.title
        # Include additional information in the response header
      

        return response

    except Exception as e:
        return HttpResponse(f"Error: {e}")
