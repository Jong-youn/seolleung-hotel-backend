from .views import ReservationView

from django.urls import path

urlpatterns = [
    path('', ReservationView.as_view()),
    path('/<slug:reservation_code>', ReservationView.as_view())
]
