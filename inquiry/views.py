import json
import jwt
import bcrypt
import re
import random
import string
import requests

from django.views                      import View
from django.http                       import HttpResponse, JsonResponse

from .models                           import InquiryType, Inquiry
from users.models                      import Grade, Job, User, Gender
from room.models                       import Branch
from my_settings                       import SECRET_KEY, ALGORITHM, SMS_AUTH
from users.utils                       import user_authentication

class InquiryView(View) :
    @user_authentication
    def post(self, request) :
        try : 
            data = json.loads(request.body)
            Inquiry(
                user            = request.user,
                branch          = Branch.objects.get(id = data['branch']),
                inquiry_type    = InquiryType.objects.get(id = data['inquiry_type']),
                title           = data['title'],
                content         = data['content']
            ).save()
            return HttpResponse(status=200)
        
        except KeyError :
            return HttpResponse(status=400) 

    @user_authentication
    def get(self, request) :
        inquiry = Inquiry.objects.filter(user_id = request.user.id).values().order_by('-created_at')
    
        return JsonResponse({'data' : list(inquiry)}, status = 200)

    @user_authentication
    def delete(self, request) :
        data = json.loads(request.body)
        Inquiry.objects.get(id = data['id']).delete()    
            
        return HttpResponse(status = 200)
    
class InquiryUpdateView(View) :
    @user_authentication
    def post(self, request, inquiry_id) :
        try : 
            data = json.loads(request.body)
            if Inquiry.objects.filter(id = inquiry_id).exists(): 
                inquiry = Inquiry.objects.filter(id = inquiry_id)
                inquiry.update(
                    branch          = Branch.objects.get(id = data['branch']),
                    inquiry_type    = InquiryType.objects.get(id = data['inquiry_type']),
                    title           = data['title'],
                    content         = data['content']
                )
                return JsonResponse({'message' : '은미님 수고했어요^_^'}, status=200)
            
            else :
                return JsonResponse({'message' : 'WRONG INQUIRY ID'}, status = 400)
        
        except KeyError :
            return HttpResponse(status=400) 
            
class InquiryTypeView(View) : 
    def get(self, request) :
        inquiry = [
            {
                'id'    : inquiry.id,
                'name'  : inquiry.inquiry_type
            }
            for inquiry in InquiryType.objects.all()
        ]
        return JsonResponse({'Inquiry_type' : list(inquiry)}, status = 200)
