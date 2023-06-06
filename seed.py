from core.models import Student
from schedule.models import Task


student1 = Student.objects.create(first_name='Test', last_name='EIEI',student_id=1)
task1 = Task.objects.create(owner=student1, task_id=1, title='testDB', parent_id=0)