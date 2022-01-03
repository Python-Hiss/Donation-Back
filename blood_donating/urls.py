from django.urls import path
from .views import AddBloodView
urlpatterns = [
    path('add/',AddBloodView.as_view(),name= 'add_blod'),
]