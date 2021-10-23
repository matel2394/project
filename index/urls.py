from django.urls import path,include
from.import views
urlpatterns = [
    path('index',views.index),
    path('footer',views.footer),
path('login',views.login),
path('signup',views.signup),
path('comu',views.comu),
path('약관',views.약관),
path('고객센터',views.고객센터),
path('write',views.write),
path('tetrible',views.tetrible),
path('write1',views.write1),
path('news',views.news),
path('online',views.onlien),
path('event',views.event),
path('game_event',views.game_event),
path('gong',views.gong),
path('mobile',views.mobile),
path('cal',views.cal),
path('company',views.comapny),
path('vote',views.vote),

    ]
