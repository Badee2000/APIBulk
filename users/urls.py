from django.urls import path
from .views import BulkUserCreationAPIView, BulkWorkerCreationAPIView, ListUsers


urlpatterns = [

    path('', ListUsers.as_view()),

    path('bulk_create_users/', BulkUserCreationAPIView.as_view(),
         name='bulk_create_users'),
    path('bulk_create_workers/', BulkWorkerCreationAPIView.as_view(),
         name='bulk_create_workers'),
]
