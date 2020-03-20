from .views import DetailView, RoomListView

from django.urls import path

urlpatterns = [
    path('/detail/<int:room_id>', DetailView.as_view()),
    path('', RoomListView.as_view()),
]
