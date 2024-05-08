from django.urls import path
from . import views



urlpatterns = [

    path("membership/", views.membership, name="membership"),
    path("memberlogin/", views.member_login, name="memberlogin"),
    path("memberlogout/", views.member_logout, name="memberlogout"),
    path("memberprofile/", views.create_member_profile, name="creatememberprofile"),
    path("viewprofile/", views.member_profile, name="viewmemberprofile"),
    path("viewaccount/", views.member_account, name="viewmemberaccount"),
    path("logstatus/", views.log_status, name="logstatus"),

]
