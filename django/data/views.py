from django.views.generic import (ListView, DetailView)
from django.db.models import Q
from django.db.models.functions import Lower
from . import models


class DataHomeView(ListView):
    """
    Class-based view to show the data 'home' (i.e. root folder)
    The 'home' is for all folders and files without a parent folder,
    as these are assumed to be at the home/root level
    """

    template_name = 'data/data.html'
    model = models.Folder
    paginate_by = 100

    def get_queryset(self):
        """
        Customise the returned queryset based on
        user's choices of search, filter, and order.
        """

        # Start with all published objects,
        queryset = self.model.objects.filter(parent_folder__isnull=True).exclude(is_public=False)

        # Return the searched, filtered, and sorted queryset
        return queryset

    def get_context_data(self, **kwargs):
        """
        Customise context data passed to template
        """
        # Get current view's context
        context = super(DataHomeView, self).get_context_data(**kwargs)
        # Also pass through files that have no parent_folder
        context['file_list'] = models.File.objects.filter(parent_folder__isnull=True).exclude(is_public=False)
        # Return context
        return context


class DataFolderView(DetailView):
    """
    Class-based view to show the data folder template
    This shows all items (files and folders)
    that have the current folder object as their parent_folder
    """

    template_name = 'data/data.html'
    model = models.Folder

    def get_context_data(self, **kwargs):
        context = super(DataFolderView, self).get_context_data(**kwargs)
        # Subfolders
        context['folder_list'] = models.Folder.objects.filter(parent_folder=self.kwargs.get('pk')).exclude(is_public=False)
        # Files
        context['file_list'] = models.File.objects.filter(parent_folder=self.kwargs.get('pk')).exclude(is_public=False)
        return context
