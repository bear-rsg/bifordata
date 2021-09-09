from django.contrib import admin
from . import models


def publish_event(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish_event.short_description = "Publish selected events (will appear on main site)"


def unpublish_event(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish_event.short_description = "Unpublish selected events (will not appear on main site)"


class EventAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Responses in the Django admin
    """
    list_display = ('name',
                    'start_datetime',
                    'finish_datetime',
                    'location',
                    'booking_email',
                    'booking_url',
                    'admin_published')
    list_filter = ('admin_published', )
    search_fields = ('name', 'description', 'location', 'booking_email', 'booking_url')
    list_per_page = 30
    ordering = ('-id',)
    actions = (publish_event, unpublish_event)


# Register
admin.site.register(models.Event, EventAdminView)
