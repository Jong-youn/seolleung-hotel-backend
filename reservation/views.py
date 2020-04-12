import json
import uuid

from .models            import Reservation, PointRequest, Point
from users.models       import User
from room.models        import Room
from .utils             import login_required

from django.views       import View
from django.http        import HttpResponse, JsonResponse
from django.db.models   import Sum

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
            saved_one           = float(data['price']) * float(request.user.grade.point_rate)
            reserve_id          = Reservation.objects.latest('id')
            user_point          = User.objects.prefetch_related('point_set').get(id = request.user.id).point_set.all()
            total_saved_point   = user_point.aggregate(Sum('saved_point'))['saved_point__sum']
            total_used_point    = user_point.aggregate(Sum('used_point'))['used_point__sum']
            
            if User.objects.prefetch_related('point_set').get(id = request.user.id).point_set.all() :
                Point(
                    user            = request.user,
                    reservation     = reserve_id, 
                    saved_point     = saved_one,
                    total_point     = saved_one + total_saved_point - total_used_point
                ).save()
            else :
                Point(
                    user        = request.user,
                    reservation = reserve_id, 
                    saved_point = saved_one,
                    total_point = saved_one
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


class PointView(View) :
    @login_required
    def get(self, request):        
        point_data = [
            {   
                'id'            : point.id,
                'date'          : point.reservation.check_in,
                'branch'        : point.reservation.room.branch.name, 
                'saved_point'   : point.saved_point,
                'used_point'    : point.used_point,
                'total_point'   : point.total_point
            }
            for point in Point.objects.all().select_related('reservation').filter(user_id = request.user.id).order_by('-created_at')
        ]
        
        return JsonResponse({'Inquiry_type' : list(point_data)}, status = 200)
    
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            PointRequest(
                user             = request.user,
                request_img      = data['request_img'],
                request          = data['request']
            ).save()

            return JsonResponse({'Message':'Request Succeed'}, status = 200)
        
        except KeyError:
            return JsonResponse({'Message':'Invalid Keys'}, status = 400)

