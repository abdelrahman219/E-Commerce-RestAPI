from rest_framework import serializers
from django.conf import settings
from .models import UserModel
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
    def create(self, validation_data):
        password = validation_data.pop('password', None) 
        instance = self.Meta.model(**validation_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

    def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            instance = super().update(instance, validated_data)
            if password is not None:
                instance.set_password(password)
                instance.save()
            
            return instance
    



# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         token = self.get_token(self.user)
#         response = Response()
#         response.set_cookie(key='jwt' , value= token ,  httponly= True)
#         print("stored in the cookie")
#         return response    