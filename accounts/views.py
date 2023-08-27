from django.shortcuts import HttpResponse, get_object_or_404
from . import serializers
from rest_framework import generics, mixins, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class Register ( generics.GenericAPIView, mixins.CreateModelMixin ) : 
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    def post (self, request) : 
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
        
            serializer.save()
        
            username = serializer.validated_data['username']
            user = User.objects.get(username = username)
            token = Token.objects.get(user=user).key
        
            data = {'token':token}
            return Response(data, status = status.HTTP_201_CREATED )
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )


class Login ( generics.GenericAPIView, mixins.CreateModelMixin ) : 
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer

    def post (self, request) : 
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
        
            s = serializer.save()

            if s['msg'] : 
                return Response(data = {'msg':s['msg']}, status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            data = {'token':s['token']}
            return Response(data, status = status.HTTP_201_CREATED )
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )

