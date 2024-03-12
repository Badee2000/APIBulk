# NOTE: I know you didn't mention to do all of that, but in case you are interested.
# Kindly use Swagger to know all the functionality :)
from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView
from .models import Company, Building, Office, UserOffice
from .serializers import CompanySerializer, OfficeSerializer, BuildingSerializer, UserOfficeSerializer, BulkUserOfficeSerializer, BulkOfficeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# Company Views:
class ListCompany(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DetailCompany(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        name = self.kwargs['name']
        return Company.objects.get(name=name)


# Building Views:
class ListBuilding(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
        company_name = self.kwargs.get('company_name')
        company = get_object_or_404(Company, name=company_name)
        return Building.objects.filter(company=company)


class DetailBuilding(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_object(self):
        company_name = self.kwargs.get('company_name')
        building_name = self.kwargs.get('name')
        company = get_object_or_404(Company, name=company_name)
        return get_object_or_404(Building, company=company, name=building_name)


# Office Views:
class ListOffice(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class DetailOffice(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def get_object(self):
        company_name = self.kwargs['company_name']
        building_name = self.kwargs['name']
        floor = self.kwargs['floor']
        number = self.kwargs['number']

        company = get_object_or_404(Company, name=company_name)
        building = get_object_or_404(
            Building, company=company, name=building_name)
        office = get_object_or_404(
            Office, building=building, floor=floor, number=number)

        return office


class BulkCreateOfficeAPIView(ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    serializer_class.bulk_serializer_class = BulkOfficeSerializer


# User Office Views:
class ListUserOffice(generics.ListAPIView):
    queryset = UserOffice.objects.all()
    serializer_class = UserOfficeSerializer


class DetailUserOffice(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = UserOffice.objects.all()
    serializer_class = UserOfficeSerializer

    def get_object(self):
        user_office = get_object_or_404(
            UserOffice, user__email=self.kwargs['email'])
        return user_office


class BulkCreateUserOfficeAPIView(ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = UserOffice.objects.all()
    serializer_class = UserOfficeSerializer
    serializer_class.bulk_serializer_class = BulkUserOfficeSerializer
