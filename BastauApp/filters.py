import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class CaseFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Case
        fields = ['category', 'region']