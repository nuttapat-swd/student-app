from django.urls import path
from studentdetail import views

app_name = 'student'
urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('addresses/', views.AddressView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail')
    ]