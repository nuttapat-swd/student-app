from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Student, Address
from studentdetail import serializers

from django.http import Http404

class StudentListView(APIView):    
    def get(self, request, format=None):
        params_payload = {}
        if request.query_params :
            for key in request.query_params.keys():
                params_payload.update({'{}'.format(key):'{}'.format(request.query_params[key])})
            students = Student.objects.filter(**params_payload)
        else:
            students = Student.objects.all()

        serializer = serializers.StudentDetailSerializer(students, many=True)
        if len(serializer.data) > 0 :
            return Response(serializer.data)
        else:
            raise Http404
class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        
        student = self.get_object(pk)
        serializer = serializers.StudentDetailSerializer(student)
        return Response(serializer.data)

class AddressView(APIView):
    def get(self, request, format=None):
        addresses = Address.objects.all()
        # .values_list('address', flat=True)
        serializer = serializers.AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serializers.AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddressDetailView(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = serializers.AddressSerializer(address)
        return Response(serializer.data)

