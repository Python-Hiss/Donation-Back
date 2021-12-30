from django.urls import path
from .views import AddListView,DetailAddView,ListView

urlpatterns = [
    path('',AddListView.as_view(),name= 'add_data'),
    path('<str:username>',DetailAddView.as_view(),name = 'detail_data'),
    # path('<int:pk>',DetailAddView.as_view(),name = 'detail_dataint'),
    path('view',ListView.as_view(),name = 'list_data')
]