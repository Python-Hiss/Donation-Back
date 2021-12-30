# accounts/urls.py
from django.urls import path
from .views import CreateUserView, HospitalDetail
from .views import CustomObtainAuthToken

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path("<int:pk>/", HospitalDetail.as_view(), name="hospital_detail"),
    path('authenticate/', CustomObtainAuthToken.as_view())
]