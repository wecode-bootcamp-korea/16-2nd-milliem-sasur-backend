import json
import bcrypt
import re
import requests

from twilio.rest  import Client
from django.views import View
from django.http  import JsonResponse
from random       import randint
from users.models import User, PhoneCheck
from my_settings  import ACCOUNT_SID, AUTH_TOKEN

class SendSmSView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            input_mobile = data['mobile']

            if not re.match(r"(010)\d{4}\d{4}",input_mobile):
                return JsonResponse({'message':'INVALID_PHONE_NUMBER'}, status=401)
            to_mobile = '+82'+ input_mobile[1:]
            check_number = randint(1000,9999)

            if not PhoneCheck.objects.filter(check_id=input_mobile).exists():
                PhoneCheck.objects.create(check_id=input_mobile, check_number=check_number)
            PhoneCheck.objects.filter(check_id=input_mobile).update(check_number=check_number)
        
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            client.messages.create(
                body  =f'milliem의사서 인증을 위해 [{check_number}]을 입력해주세요.' ,
                from_ ='+14078716367',
                to    = to_mobile
            )
            return JsonResponse({'message': 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=401)

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