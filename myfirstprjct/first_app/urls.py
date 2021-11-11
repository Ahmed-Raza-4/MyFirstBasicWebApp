from django.urls import path
from first_app import views

urlpatterns = [
     path('game/', views.project, name='project'),
     path('',views.index, name= 'access_record'),
     path('AccessRecord/',views.accrec, name= 'access_record')

]
