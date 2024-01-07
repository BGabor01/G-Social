from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    """
    A serializer for user registration.

    Fields:
        - email (EmailField): An email field required for user registration.
        - password (CharField): A write-only password field. The password is hashed before
                              saving the user instance.
        - first_name (CharField): A required field for the user's first name.
        - last_name (CharField): A required field for the user's last name.

    Meta:
        - model (Model): The User model from Django's authentication system.
        - fields (list): Fields included in the serializer and the User model creation.

    Methods:
        - create: Overridden to hash the user's password before creating the User instance.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'},validators=[validate_password])
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password',
                  'first_name', 'last_name', 'email']
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data) -> User:
        """
        Overridden create method.

        This method ensures that the user's password is hashed using Django's
        make_password function before the User instance is created and saved to the database.

        Parameters:
            - validated_data (dict): The validated data passed from the request.

        Returns:
            - User: The newly created User instance with a hashed password.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegistrationSerializer, self).create(validated_data)
