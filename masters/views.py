from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
# _________________________________________Masters_______________________________________
@csrf_exempt
@swagger_auto_schema(methods=['post'], request_body=SerializeWeighbridge)
@api_view(["GET","POST"])
def weighbridge(request):
    if request.method=="GET":
        data=Weighbridge.objects.all()
        serialized_data = SerializeWeighbridge(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=="POST":
        postdata=SerializeWeighbridge(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)

@swagger_auto_schema(methods=['put'], request_body=SerializeWeighbridge)
@api_view(["GET","PUT","DELETE"])
@csrf_exempt
def weighbridgeid(request,id):
    if request.method=="GET":
        data=Weighbridge.objects.get(pk=id)
        serialized_data = SerializeWeighbridge(data)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=='PUT':
        get_data = Weighbridge.objects.get(wbid=id)
        updated_data = SerializeWeighbridge(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    elif request.method=="DELETE":
        get_data = Weighbridge.objects.get(wbid=id)
        deleted_data = SerializeWeighbridge(get_data)
        get_data.delete()
        return Response(deleted_data.data)
    
@swagger_auto_schema(methods=['post'], request_body=SerializeVehicles)
@api_view(["GET","POST"])
def vehicles(request):
    if request.method=="GET":
        data=Vehicles.objects.all()
        serialized_data = SerializeVehicles(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=="POST":
        postdata=SerializeVehicles(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
        
@swagger_auto_schema(methods=['put'], request_body=SerializeVehicles)           
@api_view(["GET","PUT","DELETE"])
def vehiclesid(request,id):
    if request.method=="GET":
        data=Vehicles.objects.get(pk=id)
        serialized_data = SerializeVehicles(data)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=='PUT':
        get_data = Vehicles.objects.get(wbid=id)
        updated_data = SerializeVehicles(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    elif request.method=="DELETE":
        get_data = Vehicles.objects.get(wbid=id)
        deleted_data = SerializeVehicles(get_data)
        get_data.delete()
        return Response(deleted_data.data)
    
@swagger_auto_schema(methods=['post'], request_body=SerializeDrivers)
@api_view(["GET","POST"])
def drivers(request):   
    if request.method=="GET":
        data=Drivers.objects.all()
        serialized_data = SerializeDrivers(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=="POST":
        postdata=SerializeDrivers(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
        
@swagger_auto_schema(methods=['put'], request_body=SerializeDrivers)
@api_view(["GET","PUT","DELETE"])
def driversid(request,id):
    if request.method=="GET":
        data=Drivers.objects.get(pk=id)
        serialized_data = SerializeDrivers(data)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=='PUT':
        get_data = Drivers.objects.get(wbid=id)
        updated_data = SerializeDrivers(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    elif request.method=="DELETE":
        get_data = Drivers.objects.get(wbid=id)
        deleted_data = SerializeDrivers(get_data)
        get_data.delete()
        return Response(deleted_data.data)
    
@swagger_auto_schema(methods=['post'], request_body=SerializeLocatios)
@api_view(["GET","POST"])
def locations(request):    
    if request.method=="GET":
        data=Locations.objects.all()
        serialized_data = SerializeLocatios(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=="POST":
        postdata=SerializeLocatios(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
        
@swagger_auto_schema(methods=['put'], request_body=SerializeLocatios)
@api_view(["GET","PUT","DELETE"])
def locationsid(request,id):
    if request.method=="GET":
        data=Locations.objects.get(pk=id)
        serialized_data = SerializeLocatios(data)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=='PUT':
        get_data = Locations.objects.get(wbid=id)
        updated_data = SerializeLocatios(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    elif request.method=="DELETE":
        get_data = locations.objects.get(wbid=id)
        deleted_data = SerializeLocatios(get_data)
        get_data.delete()
        return Response(deleted_data.data)
    
@swagger_auto_schema(methods=['post'], request_body=SerializeOwners)
@api_view(["GET","POST"])
def owners(request):    
    if request.method=="GET":
        data=Owners.objects.all()
        serialized_data = SerializeOwners(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=="POST":
        postdata=SerializeOwners(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
        
@swagger_auto_schema(methods=['put'], request_body=SerializeOwners)
@api_view(["GET","PUT","DELETE"])
def ownersid(request,id):
    if request.method=="GET":
        data=Owners.objects.get(pk=id)
        serialized_data = SerializeOwners(data)
        sdata = serialized_data.data
        return Response(sdata)
    elif request.method=='PUT':
        get_data = Owners.objects.get(wbid=id)
        updated_data = SerializeOwners(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    elif request.method=="DELETE":
        get_data = Owners.objects.get(wbid=id)
        deleted_data = SerializeOwners(get_data)
        get_data.delete()
        return Response(deleted_data.data)