from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
# from softdelete.models import SoftDeletionModel


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    original_objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    # deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Address(BaseModel):
    """Address of student object"""
    detail = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.detail + ", " + self.sub_district + ", " + self.district + ", " + self.city + ", " + self.zip_code

class Student(BaseModel):
    """Student object"""
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING,null=True,blank=True)
    student_id = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.student_id + ": " + self.first_name + " " + self.last_name
    