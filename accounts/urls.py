from django.urls import path
from .views import AddListView,DetailAddView,ListView,CustomObtainAuthToken

urlpatterns = [
    path('signup',AddListView.as_view(),name= 'add_data'),
    path('<str:username>',DetailAddView.as_view(),name = 'detail_data'),
    path("auth/", CustomObtainAuthToken.as_view()),
    path('view',ListView.as_view(),name = 'list_data')
]