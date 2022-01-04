from django.urls import path
from .views import PostViewSet , GetViewSet,UpdateDestroyViewSet, EditBlood, AddBloodView
urlpatterns = [
    path('addtype/', AddBloodView.as_view(), name='add_blood'),
    path('add/', PostViewSet.as_view(), name='add_post'),
    path('show/',GetViewSet.as_view(),  name= "show-post"),
    path('update-delete/<int:pk>/',UpdateDestroyViewSet.as_view(),name= "update-delete-post"),
    path('update-blood/<int:pk>/',EditBlood.as_view(),name= "update-delete-post")
]