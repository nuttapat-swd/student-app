from django.db import models
from django_softdelete.models import SoftDeleteModel
# from softdelete.models import SoftDeletionModel


class BaseModel(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Address(BaseModel):
    """Address of student object"""
    detail = models.TextField(null=False)
    sub_district = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    zip_code = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.detail + ", " + self.sub_district + ", " + self.district + ", " + self.city + ", " + self.zip_code

class Student(BaseModel):
    """Student object"""
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING,null=True,blank=True)
    student_id = models.CharField(max_length=13,null=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.student_id + ": " + self.first_name + " " + self.last_name