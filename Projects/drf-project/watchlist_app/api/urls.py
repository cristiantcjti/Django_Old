from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV
#Function views
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='move-list'),
#     path('<int:pk>', movie_detail, name='move-detail'),
# ]

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='move-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='move-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
]
