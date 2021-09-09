from django.views.generic import (ListView,)
from . import models


class DataListView(ListView):
    """
    Data: List
    Class-based view to show the data list template
    """

    template_name = 'data/data-list.html'
    queryset = models.Data.objects.filter(admin_published=True)
