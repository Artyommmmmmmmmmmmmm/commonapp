from django_filters import FilterSet
from .models import New
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import New, Category
from django import forms

class ProductFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='made_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="Не выбрано",
        label="Категории",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = New
        fields = {
            'title': ['icontains'],
        }
