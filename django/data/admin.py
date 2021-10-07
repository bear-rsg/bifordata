from django.contrib import admin
from . import models

admin.site.site_header = 'BIFoR Data: Admin Dashboard'


def make_public(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to be public
    """
    queryset.update(is_public=True)


make_public.short_description = "Make Public (visible to all users)"


def make_private(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not be public
    """
    queryset.update(is_public=False)


make_private.short_description = "Make Private (only visible to select users)"


class FileAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of DataLinks in the Django admin
    """
    list_display = ('name',
                    'extension',
                    'parent_folder',
                    'is_public',
                    'filepath')
    list_filter = ('is_public',)
    search_fields = ('name',)
    list_per_page = 50
    ordering = ('name', 'id')
    actions = (make_public, make_private)


class FolderAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of DataLinkCategories in the Django admin
    """
    list_display = ('name',
                    'parent_folder',
                    'is_public',
                    'filepath')
    list_filter = ('is_public',)
    search_fields = ('name',)
    list_per_page = 50
    ordering = ('name', 'id')
    actions = (make_public, make_private)


# Register
admin.site.register(models.File, FileAdminView)
admin.site.register(models.Folder, FolderAdminView)
