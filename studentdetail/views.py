from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import action

from core.models import Student, Address
from studentdetail import serializers

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend



class StudentListView(APIView):
    serializer_class = serializers.StudentSerializer
    def get(self, request, format=None):
        params_payload = {}
        if request.query_params :
            for key in request.query_params.keys():
                params_payload.update({'{}'.format(key):'{}'.format(request.query_params[key])})
            students = Student.objects.filter(**params_payload)
        else:
            students = Student.objects.all()

        serializer = serializers.StudentSerializer(students, many=True)
        return Response(serializer.data)
            # raise Http404
    
    def post(self, request, format=None):
        """Create a new Student"""
        serializer = serializers.StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = serializers.StudentSerializer(student)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk, format=None):
        """Patch student"""
        student = self.get_object(pk)
        serializer = serializers.StudentSerializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AddressGenericsView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    filterset_fields = ['detail', 'sub_district', 'district', 'city', 'zip_code']
    serializer_class = serializers.AddressSerializer
    filter_backends = [DjangoFilterBackend]


class AddressView(APIView):
    """View for Address model."""
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = serializers.AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serializers.AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddressDeletedView(APIView):
    def get(self, request, format=None):
        addresses = Address.deleted_objects.all()
        serializer = serializers.AddressSerializer(addresses, many=True)
        return Response(serializer.data)
        
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
    
    def drop_address_student(self, address):
        students = Student.objects.filter(address=address)
        for student in students:
            student.address = None
            student.save()

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        self.drop_address_student(address)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk, format=None):
        """Patch address"""
        address = self.get_object(pk)
        serializer = serializers.AddressSerializer(address, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
   

