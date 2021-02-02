import json
import requests
import bcrypt

from django.test    import TestCase, Client
from users.models   import User, UserType
from library.models import Library
from my_settings    import SECRET_KEY
from unittest.mock  import Mock, MagicMock, call

client = Client()
class MobileSignUpIn(TestCase):

    @classmethod
    def setUpTestData(cls):
        newlibrary = Library.objects.create(name = '손문의 서재')
        usertype   = UserType.objects.create(name = 'mobile')

        user= User.objects.create(
            mobile      = '01072700002',
            password    = bcrypt.hashpw("a1234567".encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
            nickname    = '손문',
            birth       = 911004,
            gender      = 2,
            usertype_id = usertype.id,
            library_id  = newlibrary.id
        )
    def setUp(self):
        pass

    def tearDown(self):
        User.objects.all().delete()
        Library.objects.all().delete()
        UserType.objects.all().delete()

    def test_signup_success(self):
        newlibrary = Library.objects.create(name = '돈큐의 서재')
        usertype   = UserType.objects.create(name='mobile')

        user = {
            'mobile'      : '01072700001',
            'password'    : 'a1234567',
            'nickname'    : '돈큐',
            'birth'       : 880930,
            'gender'      : 1,
            'usertype_id' : usertype.id,
            'library_id'  : newlibrary.id
        }
        response = client.post('/users/mobile_signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'],'SIGNUP_SUCCESS')
        
    def test_signup_exist_mobile(self):
        user   = {
            'mobile'      : '01072700002',
            'password'    : 'a1234567',
            'birth'       : 911004,
            'gender'      : 1,
            'nickname'    : '손문',
            'usertype_id' : 1,
            'library_id'  : 1
        }
        response = client.post('/users/mobile_signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'EXIST_MOBILE')
    
    def test_invalid_password(self):
        newlibrary = Library.objects.create(name = '돈큐의 서재')
        usertype   = UserType.objects.get(name='mobile')

        user       = {
            'mobile'      : '01072700001',
            'password'    : 'a',
            'nickname'    : '돈큐',
            'birth'       : 880930,
            'gender'      : 1,
            'usertype_id' : usertype.id,
            'library_id'  : newlibrary.id
        }
        response = client.post('/users/mobile_signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'], 'INVALID_PASSWORD')
    
    def test_exist_nickname(self):
        user   = {
            'mobile'      : '01072700001',
            'password'    : 'a1234567',
            'birth'       : 911004,
            'gender'      : 2,
            'nickname'    : '손문',
            'usertype_id' : 1,
            'library_id'  : 1
        }
        response = client.post('/users/mobile_signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'EXIST_NICKNAME')

    def test_signin_success(self):
        user   = {
            'mobile'      : '01072700002',
            'password'    : 'a1234567'
            }
        response = client.post('/users/mobile_signin', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'SIGNIN_SUCCESS')
    
    def test_invalid_phonenumber(self):
        user   = {
            'mobile'      : 'aa',
            'password'    : 'a1234567'
            }
        response = client.post('/users/mobile_signin', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'INVALID_PHONE_NUMBER')
    
    def test_wrong_password(self):
        user   = {
            'mobile'      : '01072700002',
            'password'    : 'a123456227'
            }
        response = client.post('/users/mobile_signin', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'WRONG_PASSWORD')