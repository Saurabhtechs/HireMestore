import django_filters
from .models import *  
class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    citytext = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.ModelChoiceFilter(queryset=Cities.objects.all(), label='city', distinct=True, empty_label=('Choose City'))
    state = django_filters.ModelChoiceFilter(queryset=States.objects.all(), label='state', distinct=True)
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='category', distinct=True, empty_label=('Choose Category'))

    class Meta:
        model = User_Detail
        fields = ['city','category','state','citytext']
        