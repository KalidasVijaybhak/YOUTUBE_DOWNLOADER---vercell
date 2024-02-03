# myapp/urls.py
from django.urls import path
from .views import convert, get_youtube_info

# Define URL patterns for the 'myapp' application
urlpatterns = [
    # Create a URL pattern for the 'my_view' view
    path('', convert, name='convert'),
    path('get_video_info/', get_youtube_info, name='get_video_info'),

    # You can add more URL patterns for other views as needed
    # For example:
    # path('another_view/', another_view, name='another_view'),
]