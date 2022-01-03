from django.urls import path
# from .views import AddListView,DetailAddView,ListView,CustomObtainAuthToken,countview,CreateHospitalUserView,HospitalDetail,HospitalListView,counthospitalview,Blood_O_List,Blood_B_List,Blood_A_List,Blood_AB_List
from .views import AddListView
urlpatterns = [
    path('donater/signup/',AddListView.as_view(),name= 'add_data'),
#     path('donater/<int:pk>/',DetailAddView.as_view(),name = 'detail_data'),
#     path("donater/auth/", CustomObtainAuthToken.as_view()),
#     path('donater/view/',ListView.as_view(),name = 'list_data'),
#     path('donater/count/',countview.as_view(),name = 'countview'),
#     path('hospital/signup/', CreateHospitalUserView.as_view(), name='signup'),
#     path("hospital/<int:pk>/", HospitalDetail.as_view(), name="hospital_detail"),
#     path("hospital/view/", HospitalListView.as_view(), name="hospital_list"),
#     path('hospital/count/',counthospitalview.as_view(),name = 'counthospitalview'),
#     path('blood/O/',Blood_O_List.as_view(),name = 'blood_O'),
#     path('blood/A/',Blood_A_List.as_view(),name = 'blood_A'),
#     path('blood/B/',Blood_B_List.as_view(),name = 'blood_B'),
#     path('blood/AB/',Blood_AB_List.as_view(),name = 'blood_AB'),
]