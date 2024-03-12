from rest_framework import serializers
from .models import Company, Building, Office, UserOffice


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'phone',)


class BuildingSerializer(serializers.ModelSerializer):
    # To get the company's name not the id.
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Building
        fields = '__all__'


# This code defines two serializers: `OfficeSerializer` for the `Office` model with specified fields,
# and `BulkOfficeSerializer` for handling a list of office data.
# The `BulkOfficeSerializer` has a `create` method that creates
# multiple Office instances based on the validated data received.
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class BulkOfficeSerializer(serializers.ListSerializer):
    child = OfficeSerializer()

    def create(self, validated_data):
        offices_data = validated_data
        offices = [self.child.create(attrs) for attrs in offices_data]
        return offices

###########


class UserOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOffice
        fields = '__all__'


class BulkUserOfficeSerializer(serializers.ListSerializer):
    child = OfficeSerializer()

    def create(self, validated_data):
        user_offices_data = validated_data
        user_offices = [self.child.create(attrs)
                        for attrs in user_offices_data]
        return user_offices
