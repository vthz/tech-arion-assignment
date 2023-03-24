import json
from random import randint

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.
# Account views

def testFunction(request):
    return JsonResponse({"STATUS": "Working"})


# post
@csrf_exempt
def createNewUser(request):
    json_body = json.loads(request.body)
    newUser = User()
    newUser.email = json_body["email"]
    newUser.phone_number = json_body["phone_number"]
    newUser.is_admin = json_body["is_admin"]
    newUser.is_customer = json_body["is_customer"]
    newUser.save()
    print("New User Id:", newUser.id)
    return JsonResponse({"something": newUser.email})


# get
def getAllUser(request):
    userList = User.objects.all()
    user_dict = []
    for user in userList:
        user_dict.append({"email": user.email})

    return JsonResponse({"data": user_dict})


def generate_otp_for(email, active):
    user = User.objects.filter(email=email).values()
    user_id = 0
    for d in user:
        user_id = d["id"]
    otpInstance = loginTopModel()
    otpInstance.owner = user_id
    otpInstance.otp = randint(100000, 999999)
    otpInstance.active = active
    otpInstance.save()
    print(otpInstance.id)
    return otpInstance.otp


# post
@csrf_exempt
def sendOTPtoEmail(request):
    json_body = json.loads(request.body)
    otp = generate_otp_for(json_body["email"], json_body["active"])
    return JsonResponse({"otp": otp, "email": json_body["email"]})


def checkCredentials(otp, email):
    user = User.objects.filter(email=email).values()
    user_id = 0
    for d in user:
        print(d)
        user_id = d["id"]
        break
    single_row = loginTopModel.objects.filter(otp=otp, owner=user_id, active=True).values()
    if len(single_row) > 0:
        single_row.update(active=False)
        return True
    return False


# post
@csrf_exempt
def loginWithOtpAndEmail(request):
    json_body = json.loads(request.body)
    otp = json_body["otp"]
    email = json_body["email"]
    flag = checkCredentials(otp, email)
    if flag:
        return JsonResponse({"status": "Login Success"})
    return JsonResponse({"status": "Login Failed"})
