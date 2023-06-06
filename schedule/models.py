from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from core.models import Student
# from softdelete.models import SoftDeletionModel


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    original_objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseModel):
    """Task MongoDB"""
    task_id = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(default=None, null=True, blank=True)
    parent_id = models.IntegerField(blank=True, null=True)
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    # owner = models.CharField( max_length=50, blank=True, null=True)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
