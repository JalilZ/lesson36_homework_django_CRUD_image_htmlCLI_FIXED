from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from .serializers import StudentSerializer  # CRUD for Vicky
from .models import Student  # CRUD for Vicky
from rest_framework.response import Response  # CRUD for Vicky
from rest_framework.decorators import api_view  # CRUD for Vicky
from rest_framework import generics  # CRUD for Vicky



@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def students(req, id=-1):
    if req.method == 'GET':
        if id > -1:
            try:
                stu = Student.objects.get(id=id)
                return Response(StudentSerializer(stu,many=False).data)
                #return Response({'id': stu.id,'name': stu.name, 'age': stu.age, 'createdTime': stu.createdTime})
            except Student.DoesNotExist:
                return Response('Not Found')
              
        all_students = StudentSerializer(Student.objects.all(),many=True).data
        return Response(all_students)
    
        #li = []
        #all_stu = Student.objects.all()
        #for stu in all_stu:
        #    li.append({'id': stu.id,'name': stu.name, 'age': stu.age, 'createdTime': stu.createdTime})
        #return Response(li)

    elif req.method == 'DELETE':
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response('Not Found')

        temp_name = Student.objects.get(id=id).name     
        Student.objects.get(id=id).delete()
        return Response(f'Student {temp_name} was deleted.')

    elif req.method =='POST':
        stu = StudentSerializer(data=req.data)
        if stu.is_valid():
            stu.save()       # save the stu to the database table
            stu_name = stu.data.get('name')
            return Response (f'Student {stu_name} was added')
        else:
            return Response (stu.errors)
        
    elif req.method =='PUT' or req.method =='PATCH':
        try:
            Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response('Student was not Found')
        
        new_stu = StudentSerializer(req.data) # this will create a new student object with new data (there is no save() for now) - the new object is not new_stu ! its somewhere in the serializer
        old_stu = Student.objects.get(id=id)
        res = new_stu.update(old_stu, req.data) # .update() will include save()
        return Response(StudentSerializer(res,many=False).data)

    
