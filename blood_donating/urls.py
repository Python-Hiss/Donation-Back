from django.urls import path
from .views import PostViewSet , GetViewSet,UpdateDestroyViewSet
urlpatterns = [
    path('add/', PostViewSet.as_view(), name='add_post'),
    path('show/',GetViewSet.as_view(),  name= "show-post"),
    path('update-delete/<int:pk>',UpdateDestroyViewSet.as_view(),name= "update-delete-post")
]