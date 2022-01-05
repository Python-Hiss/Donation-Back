from django.urls import path
from .views import AddAeraView,AddCityView,AddAddressView,viewAddressView
urlpatterns = [
    path('area/',AddAeraView.as_view(),name= 'area'),
    path('city/',AddCityView.as_view(),name= 'city'),
    path('address/',AddAddressView.as_view(),name= 'address'),
    path('address/<int:pk>/',viewAddressView.as_view(),name= 'addressview'),
]