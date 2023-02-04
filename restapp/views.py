from django.shortcuts import render
from rest_framework import serializers
from django.http import  Http404
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import ViewSet, ModelViewSet
# Create your views here.

#this is the function view for the serializers
'''
@api_view(['GET','POST'])
def getEmployeeList(request):
    if request.method=="GET":
        employees= Employee.objects.all()
        serializer= EmployeeSerializer(employees, many= True)
        print(serializer.data)
        return Response(serializer.data)


    elif request.method=="POST":
        # jsondata= JSONParser().parse(request)
        # print(jsondata)
        serializer= EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


#this is another function for the primary key requirement serializer

'''
@api_view(['DELETE','GET','PUT'])
def getEmployeeDetail(request, pk):
    try:
        employee= Employee.objects.get(pk=pk)
    except:
        return Response(status= 404)
        
    if request.method=="GET":
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method=="DELETE":
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    elif request.method=="PUT":
        # jsondata= JSONParser().parse(request)
        serializer= EmployeeSerializer(employee, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
''' 


'''
@api_view(['GET'])
def getUserList(request):
    user= User.objects.all()
    serializer= UserSerializer(user, many = True)
    return Response(serializer.data)
'''


#class based views

# using the APIView we can create the class based Views

'''class getEmployeeList(APIView):
    def get(self, request):
        employees= Employee.objects.all()
        serializer= EmployeeSerializer(employees, many= True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

'''

'''
class getEmployeeDetail(APIView):
    def getemployee(self, pk):
        try:
            employee= Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee= self.getemployee(pk)
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee= self.getemployee(pk)
        serializer= EmployeeSerializer(employee, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, reqeust, pk):
        employee= self.getemployee(pk)
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
'''

#using mixins and generic APIView 
'''
class getEmployeeList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class getEmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

    def get(self, request ,*args, **kwargs):
        return self.retrieve(request ,*args, **kwargs)

    def delete(self, request ,*args, **kwargs):
        return self.destroy(request ,*args, **kwargs)
    
    def put(self, request ,*args, **kwargs):
        return self.update(request ,*args, **kwargs)

'''


#using the genreric class based views

'''
class getEmployeeList(generics.ListCreateAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

class getEmployeeDetail(generics.RetrieveDestroyAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer
'''

#using the viewset
'''
class EmployeeViewSet(ViewSet):
    def list(self, request):

        employee = Employee.objects.all()
        serializer= EmployeeSerializer(employee, many= True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            employee= Employee.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        serializer= EmployeeSerializer(data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    
    def destroy(self, request, pk):
        try:
            employee= Employee.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

class EmployeeListView(generics.ListCreateAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer
