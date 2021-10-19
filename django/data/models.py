from django.db import models
import os
from django.utils.text import slugify


class Folder(models.Model):
    """
    Folder to contain files and other folders (aka subfolders)
    """

    name = models.CharField(max_length=255)
    filepath = models.TextField(unique=True)
    parent_folder = models.ForeignKey("Folder", on_delete=models.SET_NULL, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField()

    @property
    def name_short(self):
        if len(self.name) > 26:
            return f"{self.name[0:13]}...{self.name[-13:]}"
        else:
            return self.name

    def __str__(self):
        return self.filepath

    def save(self, *args, **kwargs):
        self.slug = slugify(self.filepath.replace('/', '-'))
        super(Folder, self).save(*args, **kwargs)

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
    slug = models.SlugField()

    @property
    def name_full(self):
        if self.extension:
            return f"{self.name}.{self.extension}"
        else:
            return self.name

    @property
    def name_short(self):
        if len(self.name) > 22:
            return f"{self.name[0:13]}...{self.name[-9:]}.{self.extension}"
        else:
            return self.name_full

    @property
    def filepath(self):
        if self.parent_folder:
            return os.path.join(self.parent_folder.filepath, self.name_full)
        else:
            return self.name_full

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.filepath)
        super(File, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name', 'id']
