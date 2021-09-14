from django.contrib import admin
from . import models

admin.site.site_header = 'BIFoR Data: Admin Dashboard'


def publish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish.short_description = "Publish (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish.short_description = "Unpublish (will not appear on main site)"


class DataLinkAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of DataLinks in the Django admin
    """
    list_display = ('name',
                    'description_short',
                    'filepath',
                    'category',
                    'admin_published')
    list_filter = ('admin_published', 'category')
    search_fields = ('name', 'description', 'filepath')
    list_per_page = 50
    ordering = ('name', 'id')
    actions = (publish, unpublish)


class DataLinkCategoryAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of DataLinkCategories in the Django admin
    """
    list_display = ('name',
                    'description_short',
                    'admin_published')
    list_filter = ('admin_published',)
    search_fields = ('name', 'description')
    list_per_page = 50
    ordering = ('name', 'id')
    actions = (publish, unpublish)


# Register
admin.site.register(models.DataLink, DataLinkAdminView)
admin.site.register(models.DataLinkCategory, DataLinkCategoryAdminView)
