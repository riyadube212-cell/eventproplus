from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('queryeve',views.queryeve,name='queryeve'),
path('mayank',views.mayank,name='mayank'),
path('kushi',views.kushi,name='kushi'),
path('keshav',views.keshav,name='keshav'),
path('riya',views.riya,name='riya'),
path('kshtij',views.kshtij,name='kshtij'),

]