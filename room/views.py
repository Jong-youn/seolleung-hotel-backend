import json

from .models import Room, RoomDatePrice, Branch

from django.core.exceptions import ValidationError
from django.db.models       import Avg, DecimalField, ExpressionWrapper, F
from django.views           import View
from django.http            import HttpResponse, JsonResponse

class DetailView(View):
    def get(self, request, room_id):
        room_data = (
            Room
            .objects
            .select_related('branch')
            .prefetch_related(
                'roomimage_set',
                'view_set',
                'comfort_set',
                'bathroom_set',
                'entertainment_set',
                'bedding_set',
                'furnishing_set',
                'fnbservice_set',
                'laundry_set',
                'safety_set'
            )
            .get(id = room_id)
        )

        details = {
            'images' : list(room_data.roomimage_set.values_list('image', flat = True)),

            'iconic_info' : {
                'free_parking'         : room_data.free_parking,
                'free_wifi'            : room_data.free_wifi,
                'non_smoking'          : room_data.non_smoking,
                'room_square_meter'    : room_data.room_square_meter,
                'room_square_meter_py' : room_data.room_square_meter_py,
                'tv'                   : room_data.tv,
                'refrigerator'         : room_data.refrigerator,
                'bed_type'             : list(room_data.bed.values_list('name', flat = True)),
            },

            'room_info' : {
                'view'          : list(room_data.view_set.values_list('name',flat = True)),
                'comfort'       : list(room_data.comfort_set.values_list('name',flat = True)),
                'bathroom'      : list(room_data.bathroom_set.values_list('name',flat = True)),
                'entertainment' : list(room_data.entertainment_set.values_list('name',flat = True)),
                'bedding'       : list(room_data.bedding_set.values_list('name',flat = True)),
                'furnishing'    : list(room_data.furnishing_set.values_list('name',flat = True)),
                'fnbservice'    : list(room_data.fnbservice_set.values_list('name',flat = True)),
                'laundry'       : list(room_data.laundry_set.values_list('name',flat = True)),
                'safety'        : list(room_data.safety_set.values_list('name',flat = True)),
            },

            'facility_info' : {
                'neighbour' : list(room_data.branch.neighbour_set.values_list('name', flat = True)),
                'dining'    : list(room_data.branch.dining_set.values_list('name', flat = True)),
                'transport' : list(room_data.branch.transport_set.values_list('name', flat = True)),
                'service'   : list(room_data.branch.service_set.values_list('name', flat = True)),
                'entry'     : list(room_data.branch.entry_set.values_list('name', flat = True)),
                'facility'  : list(room_data.branch.facility_set.values_list('name', flat = True)),
                'language'  : list(room_data.branch.language_set.values_list('name', flat = True)),
            }
        }

        return JsonResponse({'details' : details}, status = 200)

class RoomListView(View):
    def get(self, request):
        try :
            check_in  = request.GET.get('CheckIn', None)
            check_out = request.GET.get('CheckOut', None)

            date_filter = (
                RoomDatePrice
                .objects
                .filter(date__date__range=(check_in, check_out))
            )

            rooms = list(
                date_filter
                .values_list('room_id','room__name')
                .distinct()
            )

            stay_nights = list(
                date_filter
                .values_list('date_id', flat = True)
                .distinct()
            )

            room_list = [
                {
                    'id': room[0],
                    'image' : list(
                        Room.objects.filter(id = room[0])
                        .values_list('roomimage__image'))[0],
                    'name' : room[1],
                    'price': (
                        date_filter
                        .filter(room__id = room[0])
                        .annotate(
                            total_price = ExpressionWrapper(
                                F('room__price') * F('date__custom_price')
                                ,output_field = DecimalField(10,2)
                            )
                        )
                        .aggregate(
                            Avg('total_price')
                    )
                )['total_price__avg'],
                    'stay_nights' : len(stay_nights)-1
            } for room in rooms ]

            return JsonResponse({'room_list': room_list}, status = 200)
        except ValidationError:
            return JsonResponse({'Message':'Invalid Date'}, status = 400)
    
class BranchListView(View) : 
    def get(self, request) :
        branch = Branch.objects.all().values('id', 'name')
        return JsonResponse({'Branch' : list(branch)}, status = 200)
