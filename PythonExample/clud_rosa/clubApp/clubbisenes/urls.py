from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name="clublist"),
    path('test/', views.Test.as_view(), name="test")
]
