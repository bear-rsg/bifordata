from django.db import models


class DataLinkCategory(models.Model):
    """
    Categories of data files (approx. 100 in total)
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=True)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    @property
    def description_short(self):
        return self.description[:75]

    class Meta:
        ordering = ['name', 'id']
        verbose_name_plural = "Data link categories"


class DataLink(models.Model):
    """
    A link to a data file
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    filepath = models.TextField()

    # Foreign Key fields
    category = models.ForeignKey(DataLinkCategory, on_delete=models.SET_NULL, blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=True)
    admin_notes = models.TextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    @property
    def description_short(self):
        return self.description[:75]

    class Meta:
        ordering = ['name', 'id']
