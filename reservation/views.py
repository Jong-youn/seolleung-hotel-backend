import json
import uuid

from .models import Reservation
from users.models import User
from room.models import Room
from .utils  import login_required

from django.views import View
from django.http import HttpResponse, JsonResponse

class ReservationView(View):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            Reservation(
                user             = request.user,
                room             = Room.objects.get(id = data['room_id']),
                room_name        = data['room_name'],
                check_in         = data['checkin'],
                stay_nights      = data['stay_nights'],
                adult            = data['adult'],
                price            = data['price'],
                reservation_code = uuid.uuid4()
            ).save()

            return JsonResponse({'Message':'Reservation Succeed'}, status = 200)
        except KeyError:
            return JsonResponse({'Message':'Invalid Keys'}, status = 400)

    @login_required
    def get(self, request):
        reservations = Reservation.objects.filter(user_id = request.user.id).values()

        return JsonResponse({'reservation_list' : list(reservations)}, status = 200)

    @login_required
    def delete(self, request, reservation_code):
        Reservation.objects.filter(reservation_code = reservation_code).delete()

        return JsonResponse({'Message':'Successfully Deleted!'}, status = 200)
