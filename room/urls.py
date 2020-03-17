from .views import DetailView

from django.urls import path

urlpatterns = [
    path('/detail/<int:room_id>', DetailView.as_view()),
]
