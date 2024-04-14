from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user.views import register_User,login_User,logout_User

app_name = "user"

urlpatterns = [
    path('register',register_User,name="register"),
    path('login',login_User,name="login"),
    path('logout',logout_User,name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)