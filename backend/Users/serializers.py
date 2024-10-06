from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'password', 
            'usertype', 
            'location'
        ]

        """ The extra_kwargs attribute in the Meta class is 
        another way to specify additional settings for fields 
        in the serializer. It can be used to make fields 
        write-only or read-only without having to redefine 
        the fields explicitly in the serializer. """

        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        """
        Override the default create method to handle password hashing.
        """
        # Create the user with hashed password
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'password',
            'usertype', 
            'location'
        ]

        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }

    def update(self, instance, validated_data):
        """
        Override the default update method to handle password hashing and partial updates.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the password
        instance.usertype = validated_data.get('usertype', instance.usertype)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance