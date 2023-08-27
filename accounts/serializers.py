from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterSerializer ( serializers.ModelSerializer ) :
    password = serializers.CharField(write_only=True)
    class Meta : 
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        
        u = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )

        return u



class LoginSerializer ( serializers.ModelSerializer ) : 
    
    class Meta : 
        model = User
        fields = ['email','password']
    

    def create(self, validated_data):
        
        email = validated_data['email']
        password = validated_data['password']

        check_email = User.objects.filter(email=email)

        response = {'msg':''}

        if check_email.count() != 1 : 
            response['msg'] = 'invalid Email'
            return response
        
        user = check_email.first()

        if not user.check_password(password) : 
            response['msg'] = 'invalid Password'
            return response
        
        token = Token.objects.get( user = user ).key

        response['token'] = token

        return response
    