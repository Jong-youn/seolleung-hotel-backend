import json
import re
import bcrypt
import jwt

from .models              import User,  Grade, Gender, Job
from django.test          import TestCase
from django.test          import Client



class SignupTest(TestCase) :
    def setUp(self) :
        Gender.objects.create(
            id   = 1,
            name = 'F'
        )
        Gender.objects.create(
            id   = 2,
            name = 'M'
        )
        Grade.objects.create(
            id           = 1,
            name         = 'SILVER',
            point_rate   = '0.03'
        )
        Grade.objects.create(
            id           = 2,
            name         = 'GOLD',
            point_rate   = '0.04'
        )
        Job.objects.create(
            id   = 1,
            name = 'developer'
        )
        Job.objects.create(
            id   = 2,
            name = 'painter'
        )
        User.objects.create(
            grade            = Grade.objects.get(id = 1),
            account          = 'ljy6816',
            password         = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()),
            name_kr          = 'jay',
            name_eng         = 'jayjay',
            birth            = '1505-03-13',
            gender           =  Gender.objects.get(id = 1),
            mobile           = '01012345677',
            telephone        = '576786786',
            zip_code         = '09765',
            address          = 'seoul ',
            detailed_address = 'dongjak',
            email            = '1234@gmail.com',
            job              =  Job.objects.get(id = 1),
            marketing_agree  = 'True'
        )

    def tearDown(self) :
        Gender.objects.all().delete()
        Job.objects.all().delete()
        Grade.objects.all().delete()
        User.objects.all().delete()

    def test_signupview_post_success(self) : 
        user = {
            'account'            : 'ljy68168',
            'password'           : '1234',
            'name_kr'            : 'jay',
            'name_eng'           : 'jayjay',
            'birth'              : '1505-03-13',
            'gender'             :  1,
            'mobile'             : '01012345677',
            'telephone'          : '576786786',
            'zip_code'           : '09765',
            'address'            : 'seoul ',
            'detailed_address'   : 'dongjak',
            'email'              : '1235y4@gmail.com',
            'job'                :  1,
            'marketing_agree'    : 'True'
        }
        client = Client()
        response = client.post('/users/signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
        {
            'name_kr'            : 'jay', 
            'account'            : 'ljy68168', 
            'account_number'     : 10147748
        })

    def test_signupview_duplicated_account(self) :
        user = {
            'account'          : 'ljy6816',
            'password'         : 'jgkkj',
            'name_kr'          : 'jay',
            'name_eng'         : 'jayjay',
            'birth'            : '1505-03-13',
            'gender'           :  1,
            'mobile'           : '01012345677',
            'telephone'        : '576786786',
            'zip_code'         : '09765',
            'address'          : 'seoul ',
            'detailed_address' : 'dongjak',
            'email'            : '1235y4@gmail.com',
            'job'              :  1,
            'marketing_agree'  : 'True'
        }
        client = Client()
        response = client.post('/users/signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
        {
            'message'  : 'id_duplication'
        })

    def test_signupview_post_keyerror(self) : 
        user = {
            'password'           : '1234',
            'name_kr'            : 'jay',
            'name_eng'           : 'jayjay',
            'birth'              : '1505-03-13',
            'gender'             :  1,
            'mobile'             : '01012345677',
            'telephone'          : '576786786',
            'zip_code'           : '09765',
            'address'            : 'seoul ',
            'detailed_address'   : 'dongjak',
            'email'              : '1235y4@gmail.com',
            'job'                :  1,
            'marketing_agree'    : 'True'
        }
        client = Client()
        response = client.post('/users/signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)


class IdVerificationTest(TestCase) :

    def setUp(self) :
        Gender.objects.create(
            id   = 1,
            name = 'F'
        )
        Gender.objects.create(
            id   = 2,
            name = 'M'
        )
        Grade.objects.create(
            id         = 1,
            name       = 'SILVER',
            point_rate = '0.03'
        )
        Grade.objects.create(
            id         = 2,
            name       = 'GOLD',
            point_rate = '0.04'
        )
        Job.objects.create(
            id   = 1,
            name = 'developer'
        )
        Job.objects.create(
            id   = 2,
            name = 'painter'
        )
        User.objects.create(
            grade            = Grade.objects.get(id = 1),
            account          = 'ljy6816',
            password         = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()),
            name_kr          = 'jay',
            name_eng         = 'jayjay',
            birth            = '1505-03-13',
            gender           =  Gender.objects.get(id = 1),
            mobile           = '01012345677',
            telephone        = '576786786',
            zip_code         = '09765',
            address          = 'seoul ',
            detailed_address = 'dongjak',
            email            = '1234@gmail.com',
            job              =  Job.objects.get(id = 1),
            marketing_agree  = 'True'
        )

    def tearDown(self) :
        Gender.objects.all().delete()
        Job.objects.all().delete()
        Grade.objects.all().delete()
        User.objects.all().delete()

    def test_id_post_repetition(self) :
        user = {
            'account' : 'ljy6816'
        }
        client = Client()
        response = client.post('/users/id-verification', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
        {
            'message':'id_repetition'
        })

    def test_id_post_invalid(self) :
        user = {
            'account' : 'jay'
        }
        client = Client()
        response = client.post('/users/id-verification', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
        {
            'message':'INVALID_ID'
        })

    def test_id_post_success(self) :
        user = {
            'account' : 'jay0214'
        }
        client = Client()
        response = client.post('/users/id-verification', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_id_post_keyerror(self) :
        user = {
            'id' : 'jay0214'
        }
        client = Client()
        response = client.post('/users/id-verification', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

class LoginTest(TestCase) :
    def setUp(self) :
        Gender.objects.create(
            id   = 1,
            name = 'F'
        )
        Gender.objects.create(
            id   = 2,
            name = 'M'
        )
        Grade.objects.create(
            id           = 1,
            name         = 'SILVER',
            point_rate   = '0.03'
        )
        Grade.objects.create(
            id           = 2,
            name         = 'GOLD',
            point_rate   = '0.04'
        )
        Job.objects.create(
            id        = 1,
            name      = 'developer'
        )
        Job.objects.create(
            id        = 2,
            name      = 'painter'
        )
        User.objects.create(
            grade     = Grade.objects.get(id = 1),
            account   = 'ljy6816',
            password  = bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()),
            email     = '1234@gmail.com'
        )

    def tearDown(self) : 
        Gender.objects.all().delete()
        Job.objects.all().delete()
        Grade.objects.all().delete()
        User.objects.all().delete()

    def test_LoginView_post_success(self) : 
        user = {
            'account'          : 'ljy6816',
            'password'         : '1234',
        }
        client = Client()
        response = client.post('/users/login', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_LoginView_post_wrong_pw(self) : 
        user = {
            'account'   : 'ljy6816',
            'password'  : '12345',
        }
        client = Client()
        response = client.post('/users/login', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
        {
            'message':'Wrong password'
        })

    def test_LoginView_post_wrong_id(self) : 
        user = {
            'account'      : 'jayjayy123',
            'password'     : '1234',
        }
        client = Client()
        response = client.post('/users/login', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
        {
            'message' : 'UNEXISTING_USER'
        })

    def test_LoginView_post_keyerror(self) : 
        user = {'password' : '1234'}
        client = Client()
        response = client.post('/users/login', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

