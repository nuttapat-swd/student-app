import django_filters
from core import models

from django.db.models import Q

class StudentFilter(django_filters.FilterSet):
    """Filter for students"""
    first_name = django_filters.CharFilter(field_name='first_name',lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name',lookup_expr='icontains')
    student_id = django_filters.CharFilter(field_name='student_id',lookup_expr='icontains')
    address = django_filters.CharFilter(method='address_search')
    search = django_filters.CharFilter(method='search_details')

    def address_search(self, queryset, name, value):
        return queryset.filter(Q(address__city__icontains=value)|Q(address__zip_code__icontains=value)|
                               Q(address__sub_district__icontains=value)|Q(address__district__icontains=value)|
                               Q(address__detail__icontains=value))
    
    def search_details(self, queryset, name, value):
        return queryset.filter(Q(first_name__icontains=value)|Q(last_name__icontains=value)|Q(student_id__icontains=value))
    
    class Meta:
        model = models.Student
        fields = ['first_name', 'address', 'last_name', 'student_id',]