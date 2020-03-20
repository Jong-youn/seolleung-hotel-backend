from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('room', include('room.urls')),
    path('reservation', include('reservation.urls')),
    path('inquiry', include('inquiry.urls'))
]
