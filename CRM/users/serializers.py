from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'company' ]

    
    def create(self, validated_data):
        user =  User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )

        user.email = validated_data('email')
        user.role = validated_data.get('role', 'member')
        user.company = validated_data.get('company')
        user.save()
        return user
    


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    data["user"] = user
                    return data
                else:
                    raise serializers.ValidationError("Incorrect password.")
            except User.DoesNotExist:
                raise serializers.ValidationError("User does not exist.")
        else:
            raise serializers.ValidationError("Email and password must be entered.")

    
    
    