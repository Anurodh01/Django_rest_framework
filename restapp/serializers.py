from .models import Employee 
from rest_framework import serializers
from django.contrib.auth.models import User

#here a lot of redunduncy is coming as we are dupliating the fields what we have already typed in model
#to serialize the model we have a class modelSerializer in rest_framewhich gives a good view as 
#class EmployeeSerializer(serializers.Serializer):
    #name=serializers.CharField(max_length=20)
    #email= serializers.EmailField(max_length=30)
    #salary= serializers.IntegerField()
    #phone= serializers.CharField(max_length=10)

    #def create(self, validated_data):
    #    return Employee.objects.create(**validated_data)
    
    #def update(self, employee, validated_data):
    #    newemployee= Employee(**validated_data)
    #    newemployee.id= employee.id
    #    newemployee.save()
    #    return newemployee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields= '__all__'

    
# class UserSerializer(serializers.Serializer):
#     username= serializers.CharField(max_length=30)
#     email= serializers.EmailField(max_length= 50)
#     password= serializers.CharField(max_length= 100)
#     first_name= serializers.CharField(max_length=30)
#     last_name= serializers.CharField(max_length=30)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'