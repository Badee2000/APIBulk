# IMPORTANT:
# Here I didn't use the generic serializers (The detailed way).
from rest_framework import serializers
from .models import User, Worker


#    - This serializer is used to serialize individual user instances.
#    - It specifies the model as `User` and includes specific fields to be serialized
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'first_name', 'last_name', 'role',)


#    - This serializer is used for validating and processing bulk user creation data.
#    - It contains a `ListField` named `users` with child serializer `UserSerializer`.
#    - The `create` method is overridden to handle the creation of multiple user instances in bulk.
#    - When `create` is called with validated data, it extracts the user data, creates user objects for each entry, and bulk creates these user instances using `User.objects.bulk_create`.
#    - Finally, it returns a dictionary with the created users.
class BulkUserSerializer(serializers.Serializer):
    users = serializers.ListField(child=UserSerializer())

    def create(self, validated_data):
        user_data = validated_data.get('users')
        users = [User(**user_entry) for user_entry in user_data]
        User.objects.bulk_create(users)
        return {'users': users}


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('user', 'worker_type', 'is_busy')


class BulkWorkerSerializer(serializers.Serializer):
    workers = serializers.ListField(child=WorkerSerializer())

    def create(self, validated_data):
        worker_data = validated_data.get('workers')
        workers = [Worker.objects.create(**worker_entry)
                   for worker_entry in worker_data]

        # I prefer the bulk_create() but an error occured.
        serialized_workers = WorkerSerializer(workers, many=True).data

        return {'workers': serialized_workers}
