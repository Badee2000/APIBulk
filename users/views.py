from .serializers import BulkUserSerializer
from rest_framework import status
from rest_framework.response import Response
# Used APIView instead of generic views.
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import User, Worker
from .serializers import UserSerializer, BulkWorkerSerializer

# Create your views here.


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#    - This view is used for bulk creation of users.
#    - It requires admin user permissions for access.
#    - On receiving a POST request, it validates the data using `BulkUserSerializer`.
#    - If the data is valid, it creates a user for each instance provided in the request data.
#    - It returns a success response with the IDs of the created users if the creation is successful.
class BulkUserCreationAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = BulkUserSerializer(data=request.data)
        # If inserted data is valid
        if serializer.is_valid():
            user_data = serializer.validated_data.get('users')
            users = []
            for data in user_data:
                # Create a user for each inserted instance.
                user_instance = User.objects.create(**data)
                users.append(user_instance.id)
            return Response({'message': 'Users created successfully', 'user_ids': users}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkWorkerCreationAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = BulkWorkerSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            # Not the same response as the previous one.
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
