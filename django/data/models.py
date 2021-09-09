from django.db import models
from datetime import date


class Data(models.Model):
    """
    A project-related event, e.g. a conference, seminar, etc.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events-images', blank=True, null=True)
    location = models.CharField(max_length=255)

    start_datetime = models.DateTimeField(verbose_name='Event start date/time')
    finish_datetime = models.DateTimeField(verbose_name='Event finish date/time')

    booking_email = models.CharField(max_length=255, blank=True, null=True)
    booking_url = models.TextField(blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    @property
    def is_upcoming(self):
        return date.today() <= self.finishdate

    @property
    def is_past(self):
        return self.finishdate < date.today()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_datetime', '-finish_datetime', 'name', 'id']
