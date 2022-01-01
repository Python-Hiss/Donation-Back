# accounts/urls.py
from django.urls import path
from .views import CreateUserView, HospitalDetail,ListView,countview
from .views import CustomObtainAuthToken

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path("<str:username>", HospitalDetail.as_view(), name="hospital_detail"),
    path("auth/", CustomObtainAuthToken.as_view()),
    path('view/',ListView.as_view(),name = 'list_hospital'),
    path('count/',countview.as_view(),name = 'countview')
]