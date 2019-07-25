from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Snippet


class SnippetFilter(FilterSet):
    created_at = DateFromToRangeFilter(
        widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Snippet
        fields = ['created_at']
