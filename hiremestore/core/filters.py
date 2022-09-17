import django_filters
from .models import *  
class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.ModelChoiceFilter(queryset=Cities.objects.all(), label='city', distinct=True)
    sub_category = django_filters.ModelChoiceFilter(queryset=SubCategory.objects.all(), label='sub_category', distinct=True)

    class Meta:
        model = User_Detail
        fields = ['city','sub_category']
        