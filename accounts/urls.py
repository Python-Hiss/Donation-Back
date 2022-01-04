from django.urls import path,include
from django.views.generic import TemplateView
from .views import SendFormEmail,ChangePasswordView, AddListView,DetailAddView,ListView,CustomObtainAuthToken,countview,CreateHospitalUserView,HospitalDetail,HospitalListView,counthospitalview,Blood_O_Positive_List,Blood_A_Nigative_List,Blood_A_Positive_List,Blood_AB_Positive_List,Blood_O_Nigative_List,Blood_B_Nigative_List,Blood_B_Positive_List,Blood_AB_Nigative_List, AddPatientView,ListPatientView,DetailPatientView,countPatientview


urlpatterns = [
    path('donater/signup/',AddListView.as_view(),name= 'add_data'),
    path('donater/<int:pk>/',DetailAddView.as_view(),name = 'detail_data'),
    path("donater/auth/", CustomObtainAuthToken.as_view()),
    path('donater/view/',ListView.as_view(),name = 'list_data'),
    path('donater/count/',countview.as_view(),name = 'countview'),

    
    path('hospital/signup/', CreateHospitalUserView.as_view(), name='signup'),
    path("hospital/<int:pk>/", HospitalDetail.as_view(), name="hospital_detail"),
    path("hospital/view/", HospitalListView.as_view(), name="hospital_list"),
    path('hospital/count/',counthospitalview.as_view(),name = 'counthospitalview'),

    path('templates/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send-form-email/',SendFormEmail.as_view(), name='send_email'),

    path('blood/O+/',Blood_O_Positive_List.as_view(),name = 'blood_O_Po'),
    path('blood/O-/',Blood_O_Nigative_List.as_view(),name = 'blood_O_Ne'),
    path('blood/A-/',Blood_A_Nigative_List.as_view(),name = 'blood_A_Ne'),
    path('blood/A+/',Blood_A_Positive_List.as_view(),name = 'blood_A_Po'),
    path('blood/B-/',Blood_B_Nigative_List.as_view(),name = 'blood_B_Ne'),
    path('blood/B+/',Blood_B_Positive_List.as_view(),name = 'blood_B_Po'),
    path('blood/AB+/',Blood_AB_Positive_List.as_view(),name = 'blood_AB_Po'),
    path('blood/AB-/',Blood_AB_Nigative_List.as_view(),name = 'blood_AB_Ne'),

    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    
    
    path('patient/signup/',AddPatientView.as_view(),name= 'add_data'),
    path('patient/<int:pk>/',DetailPatientView.as_view(),name = 'detail_data'),
    path('patient/view/',ListPatientView.as_view(),name = 'list_data'),
    path('patient/count/',countPatientview.as_view(),name = 'countview'),


]