from django.urls import path
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
]