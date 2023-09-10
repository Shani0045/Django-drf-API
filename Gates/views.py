
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator
from rest_framework.schemas import SchemaGenerator
# Create your views here.
# class based api views

class RailwaySiding(APIView):
    def get(self, request):
        data=Railwaysiding.objects.all()
        serialized_data = SerializeRailwaysiding(data,many=True)
        sdata = serialized_data.data
        return Response(sdata, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
            operation_description="description Railway post api", 
            request_body=SerializeRailwaysiding,
            )
    def post(self, request):
        postdata=SerializeRailwaysiding(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
    
class RailwaySidingId(APIView):
    def get(self,request,id):
        try:
            data=Railwaysiding.objects.get(pk=id)
        except Exception as e:
            return Response(data={"error":{"message":"Id not found"}},status=status.HTTP_404_NOT_FOUND)
        serialized_data = SerializeRailwaysiding(data)
        sdata = serialized_data.data
        return Response(sdata)
    def put(self,request,id):
        try:
            get_data = Railwaysiding.objects.get(pk=id)
        except Exception:
            return Response(data={"Error":"Id not found"},status=200)
        
        updated_data = SerializeRailwaysiding(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    def delete(self,request,id):
        try:
            get_data = Railwaysiding.objects.get(pk=id)
        except Exception:
            return Response(data={"Error":"Id not found"},status=200)
        
        deleted_data = SerializeRailwaysiding(get_data)
        get_data.delete()
        return Response(deleted_data.data)

class InGate(APIView):
    def get(self,request):
        data=Ingate.objects.all()
        serialized_data = SerializeIngate(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    
    @swagger_auto_schema(
            operation_description="description ingate post api", 
            request_body=SerializeIngate,
            )
    def post(self,request):
        postdata=SerializeIngate(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response({"error":postdata.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class InGateId(APIView):
    def get(self,request,id):
        data=Ingate.objects.get(pk=id)
        serialized_data = SerializeIngate(data)
        sdata = serialized_data.data
        return Response(sdata)
    def put(self,request,id):
        get_data = Ingate.objects.get(pk=id)
        updated_data = SerializeIngate(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    def delete(self,request,id):
        get_data = Ingate.objects.get(pk=id)
        deleted_data = SerializeIngate(get_data)
        get_data.delete()
        return Response(deleted_data.data)

class OutGate(APIView):
    def get(self,request):
        data=Outgate.objects.all()
        serialized_data = SerializeOutgate(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    
    @swagger_auto_schema(
            operation_description="description outgate post api", 
            request_body=SerializeOutgate,
            )
    def post(self,request):
        postdata=SerializeOutgate(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
class OutGateId(APIView):
    def get(self,request,id):
        data=Outgate.objects.get(pk=id)
        serialized_data = SerializeRailwaysiding(data)
        sdata = serialized_data.data
        return Response(sdata)
    def put(self,request,id):
        get_data = Outgate.objects.get(pk=id)
        updated_data = SerializeOutgate(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    def delete(self,request,id):
        get_data = Outgate.objects.get(pk=id)
        deleted_data = SerializeOutgate(get_data)
        get_data.delete()
        return Response(deleted_data.data)

class FuelGate(APIView):
    def get(self,request):
        data=Fuelgate.objects.all()
        serialized_data = SerializeFuelgate(data,many=True)
        sdata = serialized_data.data
        return Response(sdata)
    
    @swagger_auto_schema(
            operation_description="description fuelgate post api", 
            request_body=SerializeFuelgate,
            )
    def post(self,request):
        postdata=SerializeFuelgate(data=request.data)
        if postdata.is_valid():
            postdata.save()
            return Response(postdata.data)
        else:
            return Response(postdata.errors)
        
class FuelGateId(APIView):
    def get(self,request,id):
        data=Fuelgate.objects.get(pk=id)
        serialized_data = SerializeFuelgate(data)
        sdata = serialized_data.data
        return Response(sdata)
    def put(self,request,id):
        get_data = Fuelgate.objects.get(pk=id)
        updated_data = SerializeFuelgate(get_data, data=request.data)
        if updated_data.is_valid():
            updated_data.save() 
        data = updated_data.data
        return Response(data)
    def delete(self,request,id):
        get_data = Fuelgate.objects.get(pk=id)
        deleted_data = SerializeFuelgate(get_data)
        get_data.delete()
        return Response(deleted_data.data)

# function based api views

# @api_view(["GET","PUT","POST","DELETE"])
# def railwaysiding(request,id=None):
#     if request.method=="GET" and id is not None:
#         data=Railwaysiding.objects.get(pk=id)
#         serialized_data = SerializeRailwaysiding(data)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="GET":
#         data=Railwaysiding.objects.all()
#         serialized_data = SerializeRailwaysiding(data,many=True)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="POST":
#         postdata=SerializeRailwaysiding(data=request.data)
#         if postdata.is_valid():
#             postdata.save()
#             return Response(postdata.data)
#         else:
#             return Response(postdata.errors)
#     elif request.method=='PUT':
#         get_data = Railwaysiding.objects.get(wbid=id)
#         updated_data = SerializeRailwaysiding(get_data, data=request.data)
#         if updated_data.is_valid():
#             updated_data.save() 
#         data = updated_data.data
#         return Response(data)
#     elif request.method=="DELETE":
#         get_data = Railwaysiding.objects.get(wbid=id)
#         deleted_data = SerializeRailwaysiding(get_data)
#         get_data.delete()
#         return Response(deleted_data.data)
# @api_view(["GET","PUT","POST","DELETE"])
# def ingate(request,id=None):
#     if request.method=="GET" and id is not None:
#         data=Ingate.objects.get(pk=id)
#         serialized_data = SerializeIngate(data)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="GET":
#         data=Ingate.objects.all()
#         serialized_data = SerializeIngate(data,many=True)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="POST":
#         postdata=SerializeIngate(data=request.data)
#         if postdata.is_valid():
#             postdata.save()
#             return Response(postdata.data)
#         else:
#             return Response(postdata.errors)
#     elif request.method=='PUT':
#         get_data = Ingate.objects.get(wbid=id)
#         updated_data = SerializeIngate(get_data, data=request.data)
#         if updated_data.is_valid():
#             updated_data.save() 
#         data = updated_data.data
#         return Response(data)
#     elif request.method=="DELETE":
#         get_data = Ingate.objects.get(wbid=id)
#         deleted_data = SerializeIngate(get_data)
#         get_data.delete()
#         return Response(deleted_data.data)

# @api_view(["GET","PUT","POST","DELETE"])
# def outgate(request,id=None):
#     if request.method=="GET" and id is not None:
#         data=Outgate.objects.get(pk=id)
#         serialized_data = SerializeOutgate(data)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="GET":
#         data=Ingate.objects.all()
#         serialized_data = SerializeOutgate(data,many=True)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="POST":
#         postdata=SerializeOutgate(data=request.data)
#         if postdata.is_valid():
#             postdata.save()
#             return Response(postdata.data)
#         else:
#             return Response(postdata.errors)
#     elif request.method=='PUT':
#         get_data = Outgate.objects.get(wbid=id)
#         updated_data = SerializeOutgate(get_data, data=request.data)
#         if updated_data.is_valid():
#             updated_data.save() 
#         data = updated_data.data
#         return Response(data)
#     elif request.method=="DELETE":
#         get_data = Outgate.objects.get(wbid=id)
#         deleted_data = SerializeOutgate(get_data)
#         get_data.delete()
#         return Response(deleted_data.data)

# @api_view(["GET","PUT","POST","DELETE"])
# def fuelgate(request,id=None):
#     if request.method=="GET" and id is not None:
#         data=Fuelgate.objects.get(pk=id)
#         serialized_data = SerializeFuelgate(data)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="GET":
#         data=Fuelgate.objects.all()
#         serialized_data = SerializeFuelgate(data,many=True)
#         sdata = serialized_data.data
#         return Response(sdata)
#     elif request.method=="POST":
#         postdata=SerializeFuelgate(data=request.data)
#         if postdata.is_valid():
#             postdata.save()
#             return Response(postdata.data)
#         else:
#             return Response(postdata.errors)
#     elif request.method=='PUT':
#         get_data = Fuelgate.objects.get(wbid=id)
#         updated_data = SerializeFuelgate(get_data, data=request.data)
#         if updated_data.is_valid():
#             updated_data.save() 
#         data = updated_data.data
#         return Response(data)
#     elif request.method=="DELETE":
#         get_data = Fuelgate.objects.get(wbid=id)
#         deleted_data = SerializeFuelgate(get_data)
#         get_data.delete()
#         return Response(deleted_data.data)
