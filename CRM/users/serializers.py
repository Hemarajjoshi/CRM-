from rest_framework import serializers
from .models import User
from company.models import Company




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    company_data = CompanySerializer(write_only = True)
    company = CompanySerializer(read_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'company_data', 'company' ]


    
    def create(self, validated_data):

        company_data = validated_data.pop('company_data')
        company1 = Company.objects.create(**company_data)
        validated_data['company'] = company1

        user =  User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email']
        )
        user.role = validated_data.get('role', '')
        user.company = company1
        user.save()
        company1.save()
        return user
    

    def validate_email(self, value):
        if User.objects.filter(email= value):
            raise serializers.ValidationError("Email Already Registered")
        return value
    
    def validate_username(self,value):
        if User.objects.filter(username = value):
            raise serializers.ValidationError("Username Already Registered!! Try Another Username")
        return value
    

    


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

    
    
    