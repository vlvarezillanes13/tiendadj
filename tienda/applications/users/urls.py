from django.urls import path
#
from . import views
#

app_name = 'users'

urlpatterns = [
    path(
        'login/', 
        views.LoginUser.as_view(),
        name = 'login'
    ),
    path(
        'api/google-login/', 
        views.GoogleLoginView.as_view(),
        name = 'user-google_login'
    ),
]