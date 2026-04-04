from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register),
    path('verify-email/<int:uid>/<str:token>/', verify_email),
    path('login/', login_view),
    path('logout/', logout_view),
    path('me/', get_me),
    path('password-reset/', password_reset),
    path('password-reset-confirm/', password_reset_confirm),
]