from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from .models import *


class HomeAPIView(APIView):
    def get(self,request):
        return Reponse()
    def post(self,request):
        return Response()


class SignupAPIView(APIView):
    def get(self,request):
        return Response()
    def post(self,request):
        email = request.data['email'].lower()
        first_name = request.data['firstname']
        last_name = request.data['lastname']
        password = request.data['password']
        if User.objects.filter(username=email):
            response = 'error'
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=email,email=email,password=password)
            token =  Token.objects.get(user=user)
            response = {'first_name':user.first_name,'last_name':user.last_name,'email':user.email,'token':token.key,}
            print(response)
        return Response(response)

class LoginAPIView(APIView):
    def get(self,request):
        return Response()
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        if User.objects.filter(email = email):
            user = authenticate(username = email, password=password)
            if user is not None:
                login(request,user)
                token = Token.objects.get(user=request.user)
                response = {'first_name':request.user.first_name, 'last_name':request.user.last_name, email:request.user.email, 'token':token.key}
            else:
                response = 'Incorrect password'
        else:
            response = 'Incorrect Email Address'
        return Response(response)

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        user = request.user
        all_interests = []
        if Interest.objects.filter(user = user):
            for interest in Interest.objects.filter(user = user):
                all_interests.append(interest.interest)
            response = {'interests':all_interests}
        else:
            response = 'no interests'
        return Response(response)
    def post(self,request):
        user = request.user
        all_interests = []
        if Interest.objects.filter(user = user):
            for interest in Interest.objects.filter(user = user):
                all_interests.append(interest.interest)
            response = {'interests':all_interests}
        else:
            response = 'no interests'
        return Response(response)
        return Response()

class InterestsAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        user = request.user
        all_interests = []
        if Interest.objects.filter(user = user):
            for interest in Interest.objects.filter(user = user):
                all_interests.append(interest.interest)
            response = {'interests':all_interests}
        else:
            response = 'no interests'
        return Response(response)

    def post(self,request):
        user = request.user
        all_interests = []
        interests = request.data['interests']
        for interest in interests:
            if Interest.objects.filter(user=user, interest=interest):
                continue
            else:
                Interest.objects.create(user=request.user, interest=interest)
        if Interest.objects.filter(user = user):
            for interest in Interest.objects.filter(user = user):
                all_interests.append(interest.interest)
            response = {'interests':all_interests}
        return Response(response)

class PostsAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        return Response()
    def post(self,request):
        return Response()
