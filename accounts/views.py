# from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import AddDonerSerializer,MyTokenObtainPairSerializer,EditDonerSerializer,EditHospitalUser,AddHospitalUser,AddPatientSerializer,EditPatientSerializer
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


## hospital 


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


class HospitalListView(generics.ListAPIView):
    serializer_class = EditHospitalUser
    queryset = Hospital.objects.filter(roles="hospital")

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




# ## filter Blood
# class Blood_O_List(generics.ListAPIView):
#     typeBlood=['O+','O-']
#     serializer_class = BloodSerializer
#     queryset = CustomUser.objects.filter(blood_type__in=typeBlood)
#     permission_classes = [permissions.AllowAny]

# class Blood_A_List(generics.ListAPIView):
#     typeBlood=['O+','O-','A+','A-']
#     serializer_class = BloodSerializer
#     queryset = CustomUser.objects.filter(blood_type__in=typeBlood)
#     permission_classes = [permissions.AllowAny]
# class Blood_B_List(generics.ListAPIView):
#     typeBlood=['O+','O-','B+','B-']
#     serializer_class = BloodSerializer
#     queryset = CustomUser.objects.filter(blood_type__in=typeBlood)
#     permission_classes = [permissions.AllowAny]
# class Blood_AB_List(generics.ListAPIView):
#     typeBlood=['O+','O-','B+','B-','A+','A-','AB+','AB-']
#     serializer_class = BloodSerializer
#     queryset = CustomUser.objects.filter(blood_type__in=typeBlood)
#     permission_classes = [permissions.AllowAny]