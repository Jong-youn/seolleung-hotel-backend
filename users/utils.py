import jwt                                                
import json                 

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist 

from my_settings import SECRET_KEY                      
from users.models import User

def user_authentication(func):
    def wrapper_func(self, request, *args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({"error_code":"INVALID_LOGIN"}, status=401)

        encode_token = request.headers["Authorization"]

        try:
            data = jwt.decode(encode_token, SECRET_KEY['secret'], algorithm='HS256')
            user = User.objects.get(account = data['account'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"error_code":"INVALID_TOKEN"}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({"error_code":"UNKNOWN_USER"}, status = 401)

        return func(self, request, *args, **kwargs)
    return wrapper_func