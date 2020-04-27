from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.home, name="home"),
    path('',views.info,name="info")
]
