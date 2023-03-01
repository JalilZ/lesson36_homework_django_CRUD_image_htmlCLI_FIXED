# https://www.django-rest-framework.org/api-guide/serializers/   # Serializer: django-rest-framework documentation

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['name','age', 'createdTime'] # also works

    #def create(self, validated_data):  
    #    return Student.objects.create(**validated_data) 
    # no need for create, because if we instantiate TaskSerializer object, 
    # an object will be created in the Table (but we should save() for it to be actually created)
    
    #def update(self, instance, validated_data):
    #instance.name = validated_data.get('name', instance.name)
    #instance.age = validated_data.get('age', instance.age)
    #instance.save()
    #return instance
    # no need for update ! it is already a method in StudentSerializer!!!!!!!!!!!!
