import django_filters
from django import forms

from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = django_filters.CharFilter(lookup_expr='icontains',
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    created_at = django_filters.DateFilter(lookup_expr='gt',
                                           widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    # active = django_filters.BooleanFilter(widget=forms.)

    class Meta:
        model = Category
        fields = ['name', 'description', 'created_at', 'active']

