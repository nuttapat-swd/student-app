from django.test import TestCase
from django.urls import reverse

from core.models import Student, Address
from studentdetail import serializers

from rest_framework.test import APIClient
from rest_framework import status

def create_student(**params):
    """Create and return a Student"""
    address_ob = create_address()
    student_payload = {
            'first_name':'John',
            'last_name':'Doe',
            'student_id':'TH12321',
            'description':'Test description'
        }
    student_payload.update(params)
    student = Student.objects.create(address=address_ob,**student_payload)
    return student

def create_address(**params):
    address_payload = {
        'detail':'44/534 M.312',
        'sub_district':'Pataya',
        'district':'Pataya',
        'city':'Chonburi',
        'zip_code':'20000',
    }
    address_payload.update(params)
    address_ob = Address.objects.create(**address_payload)
    return address_ob

class StudentAndAddressTestCase(TestCase):
    """Test Student class for Student"""
    def setUp(self):
        self.client = APIClient()

    def test_get_student_list(self):
        """Test get all student"""
        create_student()
        create_student(student_id='TH432234')
        res = self.client.get('/api/v1/students/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
    
    def test_get_student_detail(self):
        """Test get student by id"""
        student = create_student()
        res = self.client.get('/api/v1/students/'+str(student.id)+'/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_get_address(self):
        """Test get address"""
        create_address()
        create_address()
        res = self.client.get('/api/v1/addresses/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_address_detail(self):
        """Test get address by id"""
        address = create_address()
        res = self.client.get('/api/v1/addresses/'+str(address.id)+'/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_address(self):
        """Test create address"""
        payload = {
            'detail':'99/723 M.312',
            'sub_district':'Napa',
            'district':'Main city',
            'city':'Chonburi',
            'zip_code':'20000',
        }
        res = self.client.post('/api/v1/addresses/', payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['detail'], payload['detail'])