# from django.shortcuts import render
from rest_framework import generics, permissions
# from .serializer import BloodSerializer,AddDonaterSerializer,MyTokenObtainPairSerializer,EditDonaterSerializer,EditHospitalUser,AddHospitalUser
from .serializer import AddDonaterSerializer
from .models import CustomUser
# from rest_framework import permissions
# from django.shortcuts import get_object_or_404
# from rest_framework_simplejwt.views import TokenObtainPairView

# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView


# # Create your views here.

# class CustomObtainAuthToken(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer



class AddListView(generics.CreateAPIView):
    serializer_class = AddDonaterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

# class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = EditDonaterSerializer
#     queryset = CustomUser.objects.all()
   
    
#     # def get_object(self):
#     #     UserName= self.kwargs.get("username")
#     #     return get_object_or_404(CustomUser, username=UserName)
# class ListView(generics.ListAPIView):
#     serializer_class = EditDonaterSerializer
#     queryset = CustomUser.objects.filter(roles="Donater")
    

# class countview(APIView):
#     """
#     A view that returns the count of active users.
#     """
#     permission_classes = [permissions.AllowAny]
#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         print(request.data)
#         user_count = CustomUser.objects.filter(roles="Donater").count()
#         content = {'user_count': user_count}
#         return Response(content)


# ## hospital 


# class CreateHospitalUserView(generics.CreateAPIView):
#     """
#     A view that signup hospital.
#     """
#     model = CustomUser
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = AddHospitalUser

# class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     A view that returns the detail of hospital 
#     """
#     queryset = CustomUser.objects.all()
#     serializer_class = EditHospitalUser
#     # def get_object(self):
#     #     UserName= self.kwargs.get("username")
#     #     return get_object_or_404(CustomUser, username=UserName)

# class HospitalListView(generics.ListAPIView):
#     serializer_class = EditHospitalUser
#     queryset = CustomUser.objects.filter(roles="hospital")

# class counthospitalview(APIView):
#     """
#     A view that returns the count of active users.
#     """
#     permission_classes = [permissions.AllowAny]
#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         print(request.data)
#         user_count = CustomUser.objects.filter(roles__in=['hospital','Donater']).count()
#         content = {'user_count': user_count}
#         return Response(content)





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