from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserRegister,UserDataSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status


# Create your views here.


class register(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registerd'
            data['username']=account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            token,create =Token.objects.get_or_create(user=account)
            data['token']=token.key
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            # data=serializer.errors
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

class welcome(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content = {'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)

class userDetails(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format =None):
        userData = self.get_object(pk)
        serializer = UserDataSerializer(userData)
        return Response(serializer.data)


    def put(self,request,pk,format = None):
        userData = self.get_object(pk)
        serializer = UserDataSerializer(userData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'error','error':serializer.data})


    def delete(self,request,pk,format = None):
        userData = self.get_object(pk)
        userData.delete()
        return Response({'message':'user deleted'})

