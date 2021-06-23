from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_as_view, name ='login'),
    path('logout/', views.logout_as_view, name ='logout'),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^register/", views.register, name="register")

]