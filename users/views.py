import json
import jwt
import bcrypt
import re
import random
import string
import requests

from django.views                      import View
from django.http                       import HttpResponse, JsonResponse

from .models                           import Grade, Job, User, Gender
from my_settings                       import SECRET_KEY, ALGORITHM, SMS_AUTH
from .utils                            import user_authentication

ID_VALID = r'^(?=.*[a-z])[a-z0-9]{6,20}$'

class IdVerificationView(View) :
    def post(self, request) :
        try :
            user_id  = json.loads(request.body)
            print('user', user_id['account'])           
            if User.objects.filter(account = user_id['account']).exists():
                return JsonResponse({'message' : 'id_repetition'}, status = 400)

            if not re.match(ID_VALID, user_id['account']):
                return JsonResponse({'message' : 'INVALID_ID'}, status = 400)
            return HttpResponse(status=200)  
        except KeyError :
            return HttpResponse(status=400)

class SignUpView(View) : 
    ID_OFFSET = 10147747
    def post(self, request):
        user_data = json.loads(request.body)
        try :
            hashed_password = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())

            if User.objects.filter(account = user_data['account']).exists() :
                return JsonResponse({'message' : 'id_duplication'}, status = 400)
            account_number = self.ID_OFFSET + User.objects.count()
            User(
                grade            = Grade.objects.get(id = 1),
                account_number   = account_number,
                account          = user_data['account'],
                password         = hashed_password,
                name_kr          = user_data['name_kr'],
                name_eng         = user_data['name_eng'],
                birth            = user_data['birth'],
                gender           = Gender.objects.get(id = user_data['gender']),
                mobile           = user_data['mobile'],
                telephone        = user_data['telephone'],
                zip_code         = user_data['zip_code'],
                address          = user_data['address'],
                detailed_address = user_data['detailed_address'],
                email            = user_data['email'],
                job              = Job.objects.get(id = user_data['job']),
                marketing_agree  = user_data['marketing_agree']
            ).save()
            return JsonResponse({
                'name_kr'        : user_data['name_kr'],
                'account'        : user_data['account'],
                'account_number' : account_number}, status = 200)

        except KeyError :
            return HttpResponse(status=400)

class LoginView(View) :
    def post(self, request):
        try :
            login_data = json.loads(request.body)
            if User.objects.filter(account = login_data['account']).exists() :
                saved_data = User.objects.get(account = login_data['account'])

                if bcrypt.checkpw(login_data['password'].encode('utf-8'), saved_data.password.encode('utf-8')):
                    token = jwt.encode({'email' : saved_data.email}, SECRET_KEY['secret'], algorithm=ALGORITHM).decode()
                    return JsonResponse({'Authorization' : token}, status=200)  
                return JsonResponse({'message' : "Wrong password"}, status=401)
            else :
                return JsonResponse({'message' : 'UNEXISTING_USER'}, status = 401)
        except KeyError :
            return HttpResponse(status=400)

class UserInfoChangeView(View) :
    @user_authentication
    def get(self, request) :
        data = json.loads(request.body)
        user = User.objects.get(account = data['account'])
        user_information = {       
            'account_number'    : user.account_number,
            'grade'             : user.grade,
            'name_kr'           : user.name_kr,
            'name_eng'          : user.name_eng,
            'birth'             : user.birth,
            'gender'            : user.gender,
            'mobile'            : user.mobile,
            'telephone'         : user.telephone,
            'zip_code'          : user.zip_code,
            'address'           : user.address,
            'detailed_address'  : user.detailed_address,
            'email'             : user.email,
            'job'               : user.job,
            'marketing_agree'   : user.marketing_agree,
        }
        return JsonResponse({"data" : user_information}, status = 200)

    @user_authentication
    def post(self, request) :
        data = json.loads(request.body)
        user = User.objects.get(account = data['account'])
        User(
            name_eng            = data['name_eng'],
            telephone           = data['telephone'],
            zip_code            = data['zip_code'],
            address             = data['address'],
            detailed_address    = data['detailed_address'],
            email               = data['email'],
            job                 = Job.objects.get(id = data['job']),
            marketing_agree     = data['marketing_agree']
        ).save()
        return HttpResponse(status=200)  

class AccountFindView(View) :
    def exist_user(self, data, user) :
        validate_condition = [
                lambda i, c: i['mobile'] == c.mobile,
                lambda i, c: i['name_kr'] == c.name_kr,
                lambda i, c: i['birth'] == str(c.birth)
                ]
        is_valid = True
        for validator in validate_condition:
            if not validator(data, user):
                return False
        return is_valid

    def post(self, request) : 
        try : 
            data = json.loads(request.body)
            if User.objects.filter(account_number = data['account_number']).exists() :
                user = User.objects.get(account_number = data['account_number'])

                if self.exist_user(data, user) :
                    return JsonResponse({'account' : user.account}, status = 200)
                else :
                    return JsonResponse({'message' : 'WRONG_INFORMATION'}, status = 401)
            else : 
                return JsonResponse({'message' : 'INVALID_ACCOUNT_NUMBER'}, status = 401)

        except KeyError :
            return HttpResponse(status=400)
        
class PasswordFindView(View) :
    def exist_user(self, data, user) :
        user_verification = [
                lambda i, c: i['account'] == c.account,
                lambda i, c: i['name_kr'] == c.name_kr
                ]
        is_valid_user = True
        for verification in user_verification:
            if not verification(data, user):
                return False
        return is_valid_user

    def post(self, request) : 
        try : 
            data = json.loads(request.body)
            if User.objects.filter(account_number = data['account_number']).exists() :
                user = User.objects.get(account_number = data['account_number'])

                if self.exist_user(data, user) :
                    return HttpResponse(status = 200)
                else :
                    return JsonResponse({'message' : 'WRONG_INFORMATION'}, status = 401)
            else : 
                return JsonResponse({'message' : 'INVALID_ACCOUNT_NUMBER'}, status = 401)

        except KeyError :
            return HttpResponse(status=400)

class SmsAuthenticationView(View) :
    def post(self, request) :
        try : 
            data = json.loads(request.body)  
            headers = {
                'Content-Type'          : 'application/json; charset=utf-8',
                'x-ncp-auth-key'        : SMS_AUTH['auth_key'],
                'x-ncp-service-secret'  : SMS_AUTH['service_secret']
            }      
            auth_num = random.randrange(100000, 1000000)
            body = {
                "type"          : "SMS",
                "contentType"   : "COMM",
                "countryCode"   : "82",
                "from"          : SMS_AUTH['from'],
                "to"            : [data['mobile']],
                "content"       : f"[LAHAN] 인증번호를 입력해 주세요 [{auth_num}]"
            }
            URL = SMS_AUTH['url']
            requests.post(URL, headers = headers, json = body)
            return JsonResponse({'AUTHENTICATION' : auth_num}, status = 200)
        
        except KeyError :
            return HttpResponse(status = 400)