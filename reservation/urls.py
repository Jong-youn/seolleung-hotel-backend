from .views import ReservationView, PointView

from django.urls import path

urlpatterns = [
    path('', ReservationView.as_view()),
    path('/delete/<slug:reservation_code>', ReservationView.as_view()),
    path('/point', PointView.as_view())
]
