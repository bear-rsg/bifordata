from django.db import models


class Folder(models.Model):
    """
    Folder to contain files and other folders (aka subfolders)
    """

    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey("Folder", on_delete=models.SET_NULL, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    @property
    def filepath(self):
        if self.parent_folder:
            return f"{self.parent_folder.filepath}/{self.name}"
        else:
            return self.name

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
    def full_name(self):
        if self.extension:
            return f"{self.name}.{self.extension}"
        else:
            return self.name

    @property
    def filepath(self):
        if self.parent_folder:
            return f"{self.parent_folder.filepath}/{self.full_name}"
        else:
            return self.full_name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'id']
