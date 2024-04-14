from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ilan.views import about,create,dashboard,detail,delete,update

app_name = "ilan"

urlpatterns = [
    path('dashboard',dashboard,name="dashboard"),
    path('create',create,name="create"),
    path('detail/<int:id>',detail,name="detail"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)