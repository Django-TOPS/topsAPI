from django.urls import path
from apiapp import views

urlpatterns = [
    path('getstudall/',views.getstudall),
    path('getstud/<int:pk>/',views.getstud),
    path('createstud/',views.createstud),
    path('deletestud/<int:pk>',views.deletestud),
    path('',views.index),
]