import json
import bcrypt
import re
import requests
import jwt

from twilio.rest    import Client
from django.views   import View
from django.http    import JsonResponse
from random         import randint
from users.models   import User, PhoneCheck, UserType
from library.models import Library
from my_settings    import algorithm, SECRET_KEY 

#class SendSmSView(View):
#    def post(self, request):
#        try:
#            data         = json.loads(request.body)
#            input_mobile = data['mobile']
#
#            if not re.match(r"(010)\d{4}\d{4}",input_mobile):
#                return JsonResponse({'message':'INVALID_PHONE_NUMBER'}, status=401)
#            to_mobile = '+82'+ input_mobile[1:]
#            check_number = randint(1000,9999)
#
#            if not PhoneCheck.objects.filter(check_id=input_mobile).exists():
#                PhoneCheck.objects.create(check_id=input_mobile, check_number=check_number)
#            PhoneCheck.objects.filter(check_id=input_mobile).update(check_number=check_number)
#        
#            client = Client(ACCOUNT_SID, AUTH_TOKEN)
#            client.messages.create(
#                body  =f'milliem의사서 인증을 위해 [{check_number}]을 입력해주세요.' ,
#                from_ ='+14078716367',
#                to    = to_mobile
#            )
#            return JsonResponse({'message': 'SUCCESS'}, status=200)
#        except KeyError:
#            return JsonResponse({'message':'KEY_ERROR'}, status=401)

class VerificationView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            input_mobile = data['mobile']
            input_code   = data['code']

            if User.objects.filter(mobile=input_mobile).exists():
                return JsonResponse({'message' : 'EXIST_USER'}, status=401)

            if PhoneCheck.objects.filter(check_id=input_mobile).exists():
                id = PhoneCheck.objects.get(check_id=input_mobile).check_number
                if not id == input_code:
                    return JsonResponse({'message': 'INVALID_CODE_NUMBER'}, status=401)
                return JsonResponse({'message': 'CODE_SUCCESS'}, status=200)
                
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

class MobileSignUp(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            mobile   = data['mobile']
            password = data['password']     
            birth    = data['birth']
            gender   = data['gender']
            nickname = data['nickname']
           
            if not re.match(r'^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$',password):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            if User.objects.filter(mobile=mobile).exists():
                return JsonResponse({'message' : 'EXIST_MOBILE'}, status=401)
            if User.objects.filter(nickname=nickname).exists():
                return JsonResponse({'message' : 'EXIST_NICKNAME'}, status=401)
            
            encrypt_pw  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_library = Library.objects.create(name=f'{nickname}의 서재')
            usertype    = UserType.objects.get(name='mobile')

            User.objects.create(
                mobile      = mobile,
                password    = encrypt_pw,
                nickname    = nickname,
                birth       = birth,
                gender      = gender,
                library_id  = new_library.id,
                usertype_id = usertype.id
                )
            return JsonResponse({'message': 'SIGNUP_SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

class MobileSignIn(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            mobile   = data['mobile']
            password = data['password']

            if not re.match(r"(010)\d{4}\d{4}",mobile):
                return JsonResponse({'message':'INVALID_PHONE_NUMBER'}, status=401)
            signin_user = User.objects.get(mobile=mobile)
            if bcrypt.checkpw(password.encode(), signin_user.password.encode()):
                token = jwt.encode({'id':signin_user.id}, SECRET_KEY, algorithm)
                return JsonResponse({'message':'SIGNIN_SUCCESS', 'TOKEN':token.decode()}, status=200)
            return JsonResponse({'message':'WRONG_PASSWORD'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

class KakaoView(View):
    def post(self, request): 
        try:
            access_token = request.headers['Authorization']
            headers      = ({'Authorization' : f'Bearer {access_token}'})
            url          = 'https://kapi.kakao.com/v2/user/me'
            data         = requests.get(url, headers=headers).json()

            if not User.objects.filter(social_id = data['id']).exists():
                new_library = Library.objects.create(name=f'{data["properties"]["nickname"]}의 서재')
                usertype    = UserType.objects.get(name='kakao')
                new_user    = User.objects.create(
                    social_id   = data['id'],
                    nickname    = data['properties']['nickname'],
                    library     = new_library,
                    usertype    = usertype
                    )
                token = jwt.encode({'id': new_user.id}, SECRET_KEY, algorithm)
                return JsonResponse({'message':'KAKAO_SIGNUP_SUCCESS', 'TOKEN':token.decode()}, status=200)
            exist_user = User.objects.get(social_id=data['id'])
            token      = jwt.encode({'id': exist_user.id}, SECRET_KEY, algorithm)
            return JsonResponse({'message':'KAKAO_SIGNIN_SUCCESS', 'TOKEN':token.decode()}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=401)
