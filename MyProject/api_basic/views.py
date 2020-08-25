from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from .serializers import LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


    def get(self, request, id = None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.dsetroy(request, id)


# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def user_list(request):


    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login

class Genericlogin(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = LoginSerializer
    queryset = User.objects.all()



    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
'''
   def post(self, request):
        return self.create(request)

    def put(self, request):
        return self.update(request)

    def delete(self, request):
        return self.dsetroy(request)'''


# Create your views here.
class LoginAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def login_list(request):


    if request.method == 'GET':
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
