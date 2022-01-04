# from django.shortcuts import render
from django.http import response
from rest_framework import generics, permissions
from .serializer import AddDonerSerializer,MyTokenObtainPairSerializer,EditDonerSerializer,EditHospitalUser,AddHospitalUser,AddPatientSerializer,EditPatientSerializer,BloodSerializer
from .models import Patient,Hospital,Doner
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

### doner 

class AddListView(generics.CreateAPIView):
    serializer_class = AddDonerSerializer
    queryset = Doner.objects.all()
    permission_classes = [permissions.AllowAny]


class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditDonerSerializer
    queryset = Doner.objects.all()
    permission_classes = [permissions.AllowAny]



class ListView(generics.ListAPIView):
    serializer_class = EditDonerSerializer
    queryset = Doner.objects.all()
    

class countview(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        print(request.data)
        user_count = Doner.objects.count()
        content = {'user_count': user_count}
        return Response(content)




## filter Blood
class Blood_O_Nigative_List(generics.ListAPIView):
    # typeBlood=['O+','O-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type = 'O-')
    permission_classes = [permissions.AllowAny]
class Blood_O_Positive_List(generics.ListAPIView):
    typeBlood=['O+','O-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in = typeBlood)
    permission_classes = [permissions.AllowAny]

class Blood_A_Nigative_List(generics.ListAPIView):
    typeBlood=['O-','A-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]
class Blood_A_Positive_List(generics.ListAPIView):
    typeBlood=['O+','O-','A+','A-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]
class Blood_B_Nigative_List(generics.ListAPIView):
    typeBlood=['O-','B-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]
class Blood_B_Positive_List(generics.ListAPIView):
    typeBlood=['O+','O-','B+','B-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]


class Blood_AB_Positive_List(generics.ListAPIView):
    typeBlood=['O+','O-','B+','B-','A+','A-','AB+','AB-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]
class Blood_AB_Nigative_List(generics.ListAPIView):
    typeBlood=['O-','B-','A-','AB-']
    serializer_class = BloodSerializer
    queryset = Doner.objects.filter(blood_type__blood_type__in=typeBlood)
    permission_classes = [permissions.AllowAny]





from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################################################################
#######################################################################
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from pandas import json_normalize,read_json

# from django.core.mail import send_mail
# send_mail('Example Subject', 'from django backend', '21025560@student.ltuc.com', ['koute47@gmail.com'])
import json


class SendFormEmail(View):


    def post(self,request):
        body_unicode = request.body
    #    dataGet = request.GET.get('name',None)
        email = json.loads(body_unicode)['email']
        print(email)
        send_mail(
            'Subject - Donate Blood', 
            'Hello our super hero we need you for save life',
            '21025560@student.ltuc.com', # Admin
            [
                email
            ]
        ) 
        return response.JsonResponse({'email':'send correct'})



from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    
    # ['koute47@gmail.com']
    
    send_mail(
            'Subject - Donate Blood', 
            'Hello our super hero we need you for save life',
            '21025560@student.ltuc.com', # Admin
            [
                'koute47@gmail.com'
            ]
    )
    print(reset_password_token.user.email)
    return response.JsonResponse({'email':'send correct'})
class CreateHospitalUserView(generics.CreateAPIView):
    """
    A view that signup hospital.
    """
    model = Hospital
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = AddHospitalUser

class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view that returns the detail of hospital 
    """
    queryset = Hospital.objects.all()
    serializer_class = EditHospitalUser
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]

class HospitalListView(generics.ListAPIView):
    serializer_class = EditHospitalUser
    queryset = Hospital.objects.all()

class counthospitalview(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        print(request.data)
        user_count = Hospital.objects.count()
        content = {'user_count': user_count}
        return Response(content)


# Patient

class AddPatientView(generics.CreateAPIView):
    serializer_class = AddPatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [permissions.AllowAny]


class DetailPatientView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditPatientSerializer
    queryset = Patient.objects.all()


class ListPatientView(generics.ListAPIView):
    serializer_class = EditPatientSerializer
    queryset = Patient.objects.all()
    

class countPatientview(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        print(request.data)
        user_count = Patient.objects.count()
        content = {'user_count': user_count}
        return Response(content)


