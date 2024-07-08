from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Member

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import generics
from .models import *
from .serializers import *

    
def hell (request):
  # Create a new document
  doc = DynamicDocument(data={"field1": "value1", "field2": 123})
  doc.save()

  # Retrieve documents
  for doc in DynamicDocument.objects:
    print(doc.data)
  return HttpResponse("Done")


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers" : mymembers
    }

    return HttpResponse(template.render(context,request))

def details(request, id):
  try:
    mymember = Member.objects.get(id=id)
  except:
     return HttpResponse("<h1>No valid data!!</h1>")

  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main (request):
  temp = loader.get_template("main.html")
  return HttpResponse(temp.render())   

def test(request):

  mymembers = Member.objects.filter()

  template = loader.get_template('template.html')
  
  context = {
    'mymembers': mymembers,   
    "greetings" : 123,
  }
  return HttpResponse(template.render(context, request))

# from pydantic import BaseModel

# class NameItem(BaseModel):
#     name: str
#     firstName: str

@api_view(['POST'])
def fun(request):#,item: NameItem):
    print("#####################################")
    serll=MemberSerializer(data=request.data)

    print("####", request.data)
    
    if serll.is_valid():
        print("#####################################")
        return HttpResponse(serll.data)

    else:
       print(serll.errors)  # Print the validation errors
       return Response(serll.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return HttpResponse(serll.data)


@api_view(['POST'])
def fun2(request):#,item: NameItem):
  return HttpResponse("sadfasdfasdgasdgfasdf")
