import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST, require_GET


@csrf_exempt
@require_POST
def membership(request):
    data = json.loads(request.body)

    username = data.get('username')
    email = data.get('email')
    password1 = data.get('password1')
    password2 = data.get('password2')
    first_name = data.get('firstname')
    last_name = data.get('lastname')
    # confirm password and insert a user object
    if password1 != password2:
        return JsonResponse({'success': False})
    else:
        user = User.objects.create_user(
            username=username, email=email, password=password1, first_name=first_name, last_name=last_name
        )
        return JsonResponse({'success':True})

@require_POST
@csrf_exempt
def member_login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({"Error": "You must fill out username and password fields"}, status=400)
    # if user exists log in
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user, backend=None)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({"Error": "invalid credentials"}, status=400)

@csrf_exempt
@require_POST
def member_logout(request):
    # log user out
    logout(request)
    return JsonResponse({'success': True})


@csrf_exempt
@login_required
@require_GET
def member_profile(request):
    return JsonResponse({'success': True})

# Create your views here.

