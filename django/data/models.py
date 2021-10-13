from django.db import models
import os


class Folder(models.Model):
    """
    Folder to contain files and other folders (aka subfolders)
    """

    name = models.CharField(max_length=255)
    filepath = models.TextField(unique=True)
    parent_folder = models.ForeignKey("Folder", on_delete=models.SET_NULL, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.filepath

    class Meta:
        ordering = ['name', 'id']


class File(models.Model):
    """
    A link to a data file (not a file directly uploaded)
    """

    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=255, blank=True, null=True)
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    @property
    def name_full(self):
        if self.extension:
            return f"{self.name}.{self.extension}"
        else:
            return self.name

    @property
    def filepath(self):
        if self.parent_folder:
            return os.path.join(self.parent_folder.filepath, self.name_full)
        else:
            return self.name_full

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'id']
