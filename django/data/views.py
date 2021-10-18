from django.views.generic import (ListView, DetailView, TemplateView)
from . import models, data_sync
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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
        context['file_list'] = models.File.objects\
            .filter(parent_folder__isnull=True)\
            .exclude(is_public=False)
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
        context['folder_list'] = models.Folder.objects\
            .filter(parent_folder__slug=self.kwargs.get('slug'))\
            .exclude(is_public=False)
        # Files
        context['file_list'] = models.File.objects\
            .filter(parent_folder__slug=self.kwargs.get('slug'))\
            .exclude(is_public=False)
        return context


class DataSyncLandingView(TemplateView):
    """
    Class-based view to show the data sync landing page,
    where users can click a link to execute the DataSyncView
    """

    template_name = 'data/data-sync.html'


@login_required
def DataSyncView(request):
    """
    Functional view to run the XML importer
    Show a success page if completed successfully, else show error page
    Requires user to be logged in (via the Django dashboard)
    """

    try:
        data_sync.data_sync()
        return render(request, 'data/data-sync-success.html')

    except Exception as e:
        print(e)
        return render(request, 'data/data-sync-fail.html')
