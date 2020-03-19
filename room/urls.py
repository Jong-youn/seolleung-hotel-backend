from .views import DetailView, RoomListView, BranchListView

from django.urls import path

urlpatterns = [
    path('/detail/<int:room_id>', DetailView.as_view()),
    path('', RoomListView.as_view()),
    path('/branch', BranchListView.as_view()),
]
