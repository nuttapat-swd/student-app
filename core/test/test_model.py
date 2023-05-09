from django.test import TestCase

from core.models import Student, Address


class AddressTestCase(TestCase):
    def test_create_address(self):
        payload = {
            'detail':'99/723 M.312',
            'sub_district':'Napa',
            'district':'Main city',
            'city':'Chonburi',
            'zip_code':'20000',
        }
        address = Address.objects.create(**payload)
        self.assertEqual(address.detail, payload['detail'])
        self.assertEqual(address.sub_district, payload['sub_district'])
        self.assertEqual(address.district, payload['district'])
        self.assertEqual(address.city, payload['city'])
        self.assertEqual(address.zip_code, payload['zip_code'])

class StudentTestCase(TestCase):
    def test_create_student(self):
        student_payload = {
            'first_name':'John',
            'last_name':'Doe',
            'student_id':'TH12321',
            'description':'Test description'
        }
        address_ob = Address.objects.create(
            detail='44/534 M.312',
            sub_district='Pataya',
            district='Pataya',
            city='Chonburi',
            zip_code='20000',
        )
        student = Student.objects.create(address=address_ob,**student_payload)
        self.assertEqual(student.first_name, student_payload['first_name'])
        self.assertEqual(student.last_name, student_payload['last_name'])
        self.assertEqual(student.student_id, student_payload['student_id'])
        self.assertEqual(student.description, student_payload['description'])
        self.assertEqual(str(student.address), "44/534 M.312, Pataya, Pataya, Chonburi, 20000")



