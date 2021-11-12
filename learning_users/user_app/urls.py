from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns=[
 path('game/', views.game, name='game'),
 path('accessrecord/',views.accessrecord, name= 'accessrecord'),
  path('register/',views.register,name='register'),
  path('user_login/',views.user_login,name='user_login'),


]
