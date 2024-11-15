from django.urls import path
from . import views

app_name= 'cars'

urlpatterns = [
    path('', views.cars_list,name="list"), 
    # path('<slug:slug>', views.post_page,name="page"), 
    path('new-car/', views.car_new,name="new-car"), 
    path('<int:id>', views.car_page,name="car-page"), 
]