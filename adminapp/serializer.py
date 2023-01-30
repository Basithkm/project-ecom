from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import status


User=get_user_model()

class UserRegister(serializers.ModelSerializer):
    password2 =serializers.CharField(style={'input_type':'password'},write_only =True)
    class Meta:
        model = User
        fields=['username','email','password','password2','first_name','last_name']
        
    def save(self):
        reg = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password= self.validated_data['password']
        password2= self.validated_data['password2']

        if password !=password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg


class UserDataSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields =  ['username','email','first_name','last_name']