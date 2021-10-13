import os
from . import models
from django.db import transaction
from django.conf import settings


@transaction.atomic
def data_sync():
    """
    Syncronise the folders and files in the data directory
    with the 'Folder' and 'File' data models
    """

    # Delete all objects.
    # Note: order must satisfy foreign key relationships (child first)
    models.File.objects.all().delete()
    models.Folder.objects.all().delete()

    for root, dirs, files in os.walk(settings.DATA_ROOT):

        #
        # FOLDERS
        #

        path_inside_data_root = str(root)[len(settings.DATA_ROOT):]
        path_inside_data_root_parent = os.sep.join(path_inside_data_root.split(os.sep)[:-1])
        parent_folder_obj = models.Folder.objects.filter(filepath=path_inside_data_root_parent).first()

        # skip root folder
        if root != settings.DATA_ROOT:
            models.Folder.objects.create(name=os.path.basename(root),
                                         filepath=path_inside_data_root,
                                         parent_folder=parent_folder_obj)

        #
        # FILES
        #

        folder_obj = models.Folder.objects.filter(filepath=path_inside_data_root).first()

        for file in files:
            # skip hidden files
            if file[0] != '.':
                models.File.objects.create(name=file.split('.')[0],
                                           extension=file.split('.')[1],
                                           parent_folder=folder_obj)
