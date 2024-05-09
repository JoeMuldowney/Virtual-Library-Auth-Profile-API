import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import MemberProfile


# Create your views here.

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
        return JsonResponse({'success': True})

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
@require_GET
def log_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'is_authenticated': True})
    else:
        return JsonResponse({'is_authenticated': False})


@csrf_exempt
@require_POST
def member_logout(request):

    if request.user.is_authenticated:
        # log user out
        logout(request)
        return JsonResponse({'success': True}, status=200)
    else:
        return JsonResponse({'Error': "Not logged in"}, status=400)


@csrf_exempt
@login_required
@require_POST
def create_member_profile(request):
    data = json.loads(request.body)

    profile_description = data.get('profileDesc', None)
    fav_book = data.get('favoriteBook', None)
    cur_book = data.get('currentBook', None)
    fav_author = data.get('favoriteAuthor', None)
    fav_genres = data.get('favoriteGenre',None)
    public = data.get('publicProfile', False)

    if data is None:
        return JsonResponse({"Error": "No fields are field out"}, status=400)

    try:
        # Get the current user
        user = request.user
        profile=MemberProfile( user=user,
            profile_description=profile_description, fav_book=fav_book, cur_book=cur_book, fav_author=fav_author, fav_genres=fav_genres, public=public
        )
        profile.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'Error': str(e)})


@login_required
@require_GET
@csrf_protect
def member_profile(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            member_profile = MemberProfile.objects.get(user=user)
            data = {
            'profileDesc': member_profile.profile_description,
            'favoriteBook': member_profile.fav_book,
            'currentBook': member_profile.cur_book,
            'favoriteAuthor': member_profile.fav_author,
            'favoriteGenre': member_profile.fav_genres,
            'publicProfile': member_profile.public
            }
            return JsonResponse(data)
        except MemberProfile:
            return JsonResponse({'error': 'Member profile does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'User not logged in'}, status=400)


@require_GET
@csrf_protect
@login_required
def member_account(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            member = User.objects.get(username=user)
            return JsonResponse({
                'first_name': member.first_name,
                'last_name': member.last_name,
                'username': member.username,
                'email': member.email,
                'member_since': member.date_joined

            })
        except:
            return JsonResponse({'error': 'User account does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'User not logged in'}, status=400)




