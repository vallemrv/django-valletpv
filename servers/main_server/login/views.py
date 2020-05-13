from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt

from tokenapi.decorators import token_required
from tokenapi.http import  JsonError, JsonResponse


# Create your views here.
@csrf_exempt
def sing_up(request):
    if request.method != "POST":
        return JsonError("must be only POST request")
    else:
        username = request.POST["username"]
        if User.objects.filter(username=username):
            return JsonError("User")
        user = User.objects.create_user(request.POST["username"],
                                        request.POST["username"],
                                        request.POST["password"])
        
        user.first_name = request.POST["first_name"]
        user.is_staff = False
        user.save()
        
        return JsonResponse({})

@token_required
def test_logging(request):
    return JsonResponse({})

