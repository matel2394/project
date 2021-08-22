from django.urls import path,include
from.import views
urlpatterns = [
    path('index',views.index),
    path('footer',views.footer),
path('login',views.login),
path('signup',views.signup),
    ]
