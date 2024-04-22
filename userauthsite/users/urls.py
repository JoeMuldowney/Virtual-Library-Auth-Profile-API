from django.urls import path
from . import views



urlpatterns = [

    path("membership/", views.membership, name="membership"),
    path("memberlogin/", views.member_login, name="memberlogin"),
    path("memberlogout/", views.member_logout, name="memberlogout"),
    path("memberprofile/", views.member_profile, name="memberprofile"),
]
