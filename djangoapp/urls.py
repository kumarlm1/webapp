from django.urls import path
from . import views
from rest_framework import routers,serializers,viewsets
from djangoapp.models import posts
from djangoapp.serializers import PostSerializer


urlpatterns = [
    path('',views.create),
    path('s',views.show_data),
    path('ss',views.show_datas)
]
