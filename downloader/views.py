from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .download_func import download_video, download_audio
from pytube import YouTube

def convert(request):
    response = None  # Initialize the response variable
    if request.method == "POST":
        link = request.POST.get("link", "")
        button_clicked = request.POST.get("submit_button")
        print(link)
        print(button_clicked)
        if button_clicked == "Download Video":
            response = download_video(request, link)
        elif button_clicked == "Download Audio":
            response = download_audio(request, link)
        # Check if the download was successful
        print(isinstance(response, HttpResponse))
        if isinstance(response, HttpResponse):
            print("loading")
            print(response)
            
            return response  # Return the response directly

        # If there was an error, you might want to handle it, e.g., by rendering an error page
        return render(request, "error.html", {"error_message": response})

    # Render the initial form
    return render(request, "home.html")


def get_youtube_info(request):
    video_url = request.GET.get('video_url', '')
    print(video_url)
    try:

        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title

        response_data = {
            'title': title,
            'thumbnail_url': thumbnail_url,
        }
        print(response_data)
        return JsonResponse(response_data)

    except Exception as e:
        error_message = str(e)
        return JsonResponse({'error': error_message}, status=500)