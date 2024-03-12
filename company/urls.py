from django.urls import path
from .views import ListCompany, DetailCompany, ListBuilding, DetailBuilding, ListOffice, DetailOffice, ListUserOffice, DetailUserOffice, BulkCreateOfficeAPIView, BulkCreateUserOfficeAPIView

urlpatterns = [

    # Company:
    path('<str:name>/', DetailCompany.as_view()),
    path('', ListCompany.as_view()),

    # Building:
    path('<str:company_name>/building/<str:name>/', DetailBuilding.as_view()),
    path('<str:company_name>/building/', ListBuilding.as_view()),

    # Office:
    path('<str:company_name>/building/<str:name>/office/floor/<int:floor>/<int:number>',
         DetailOffice.as_view()),
    path('<str:company_name>/building/<str:name>/office/',
         ListOffice.as_view()),

    # User Office:
    path('<str:company_name>/building/<str:name>/office/floor/<int:floor>/<int:number>/user-office/<str:email>/',
         DetailUserOffice.as_view()),
    path('<str:company_name>/building/<str:name>/office/floor/<int:floor>/<int:number>/user-office/',
         ListUserOffice.as_view()),

    # Bulk:
    path('bulk-create/office/', BulkCreateOfficeAPIView.as_view(),
         name='bulk_create_office'),
    path('bulk-create/useroffice/', BulkCreateUserOfficeAPIView.as_view(),
         name='bulk_create_useroffice'),

]
