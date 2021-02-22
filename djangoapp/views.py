from django.shortcuts import render , redirect
from django.http import HttpResponse
from djangoapp.models import sample,posts,post
from django  import forms
import string
from django.contrib.auth.models import User , Group
from djangoapp.serializers import UserSerializer,GroupSerializer,SamplesSerializer,PostSerializer
from rest_framework import viewsets,response
from rest_framework import permissions
import requests 
from rest_framework.response import Response 
import json
from rest_framework.decorators import api_view



# Create your views here.

def postss(request):
    if request.method == "POST":
        database1 = posts(
        post_number=request.POST['user'],
        message=request.POST['number'],
        )
        print(database1.message,database1.post_number)
        database1.save()
    return render(request,'djangoapp/demo.html')        

def create(request):
    if request.method == "POST":
     name=request.POST['user']
     phone=request.POST['number']
        

     url = "http://localhost:8000/new/ss"
     data={
          'name':request.POST['user']
        }
     headers = {'content-type': 'application/json'}
     r=requests.post(url, data=json.dumps(data),headers=headers)
     
        
    return render(request,'djangoapp/demo.html')

@api_view(['GET', 'POST'])
def show_data(request):
    if request.method == "POST":
    
        serial = SamplesSerializer(data=request.data)
        
        if serial.is_valid():
            serial.save()
        print(request.data)
   
        return Response(serial.data)        

@api_view(['GET', 'POST'])
def show_data1(request):
    if request.method == "POST":
        url = "http://localhost:8000/new/s"
    data={
          'name':request.POST['user'],
          'phone':request.POST['number']

        }
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data),headers=headers)
        

    if request.method == "GET": 
        objects=sample.objects.all()
        for object in objects:
            print(object)
        return Response({"message":"cscaxaXSA AD Ad "})
    return Response({"message":"enter details"})




@api_view(['GET','POST'])
def show_datas(request):
    if request.method == "POST":
        names=request.data['name']
        if(post.objects.get(name=names)):
            print("found")
            query=post.objects.filter(name=names)
            serializer=PostSerializer(query,many=False)
            

            
        return render(request,'djangoapp/show.html',context=serializer.data)
    return render(request,'djangoapp/demo.html')    


    