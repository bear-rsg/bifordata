from django.views.generic import (ListView,)
from django.db.models import Q
from django.db.models.functions import Lower
from . import models


class DataListView(ListView):
    """
    Data: List
    Class-based view to show the data list template
    """

    template_name = 'data/data-list.html'
    model = models.DataLink
    paginate_by = 100

    def get_queryset(self):
        """
        Customise the returned queryset based on
        user's choices of search, filter, and order.

        Also add other objects, e.g. DataLinkCategories, to use in the page
        """

        # Start with all published objects,
        queryset = self.model.objects.filter(admin_published=True)

        # Search
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.filter(
                Q(id__contains=search) |
                Q(name__contains=search) |
                Q(description__contains=search) |
                Q(filepath__contains=search) |
                Q(category__name__contains=search)
            )

        # Filter
        filter_category = self.request.GET.get('filter_category', '')
        if filter_category != '':
            queryset = queryset.filter(category=filter_category)

        # Order
        order = self.request.GET.get('order_direction', '') + self.request.GET.get('order_by', 'name')
        # If starts with a '-' then it means order descending
        if order[0] == '-':
            queryset = queryset.order_by(Lower(order[1:]).desc())
        else:
            queryset = queryset.order_by(Lower(order))

        # Return the searched, filtered, and ordered queryset
        return queryset

    def get_context_data(self, **kwargs):
        # Get current view's context
        context = super(DataListView, self).get_context_data(**kwargs)
        # Add DataLinkCategories to filter on
        context['categories'] = models.DataLinkCategory.objects.filter(admin_published=True)
        # Return context
        return context
