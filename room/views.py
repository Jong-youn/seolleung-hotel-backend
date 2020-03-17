import json

from .models import Room

from django.views import View
from django.http  import HttpResponse, JsonResponse

class DetailView(View):
    def get(self, request, room_id):
        room_data = (
            Room
            .objects
            .select_related('room_type')
            .get(id = room_id)
        )
        details = {
            'images' : list(
                room_data
                .room_type
                .roomimage_set
                .values_list('image', flat = True)
            ),

            'iconic_info' : {
                'free_parking'         : room_data.room_type.iconic_info.free_parking,
                'free_wifi'            : room_data.room_type.iconic_info.free_wifi,
                'non_smoking'          : room_data.room_type.iconic_info.non_smoking,
                'room_square_meter'    : room_data.room_type.iconic_info.room_square_meter,
                'bed_type'             : room_data.room_type.iconic_info.bed_type.values('name')[0]['name'],
                'room_square_meter_py' : room_data.room_type.iconic_info.room_square_meter_py,
                'tv'                   : room_data.room_type.iconic_info.tv,
                'refrigerator'         : room_data.room_type.iconic_info.refrigerator
            },

            'room_info' : {
                'view'          : room_data.room_type.room_information.view.name,
                'comfort'       : room_data.room_type.room_information.comfort.name,
                'bathroom'      : room_data.room_type.room_information.bathroom.name,
                'entertainment' : room_data.room_type.room_information.entertainment.name,
                'bedding'       : room_data.room_type.room_information.bedding.name,
                'furnishing'    : room_data.room_type.room_information.furnishing.name,
                'fnb_service'   : room_data.room_type.room_information.fnb_service.name,
                'laundry'       : room_data.room_type.room_information.laundry.name,
                'safety'        : room_data.room_type.room_information.safety.name
            },

            'facility_info' : room_data.branch.facility.name
}

        return JsonResponse({'details' : details}, status = 200)
