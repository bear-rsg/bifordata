"""
The purpose of this script is to sync folders and files in the
data folder (e.g. a folder on the RDS) with the Folder and File data models
in the website's database.

A few helpful points:
- Running this script wipes the current model objects and rebuilds from scratch
- Any files/folders in the data folder that start with _ will be private and not shown on the website
"""

import os
from . import models
from django.db import transaction
from django.conf import settings


def set_public_or_private(objectname):
    """
    If an object (file/folder) starts with a specified character(s),
    then make it private (False/0), otherwise make public (True/1)
    """

    private_identifier = "_"
    if objectname.startswith(private_identifier):
        return 0
    else:
        return 1


@transaction.atomic
def data_sync():
    """
    Syncronise the folders and files in the data directory
    with the 'Folder' and 'File' data models
    """

    # Delete all objects to start from scratch each time
    # Note: order must satisfy foreign key relationships (child first)
    models.File.objects.all().delete()
    models.Folder.objects.all().delete()

    id_folder = 0
    id_file = 0

    for root, dirs, files in os.walk(settings.DATA_ROOT):

        #
        # FOLDERS
        #

        path_inside_data_root = str(root)[len(settings.DATA_ROOT):]
        path_inside_data_root_parent = os.sep.join(path_inside_data_root.split(os.sep)[:-1])
        parent_folder_obj = models.Folder.objects.filter(filepath=path_inside_data_root_parent).first()

        # skip root folder
        if root != settings.DATA_ROOT:
            id_folder += 1
            name_folder = os.path.basename(root)
            models.Folder.objects.create(id=id_folder,
                                         name=name_folder,
                                         filepath=path_inside_data_root,
                                         is_public=set_public_or_private(name_folder),
                                         parent_folder=parent_folder_obj)

        #
        # FILES
        #

        folder_obj = models.Folder.objects.filter(filepath=path_inside_data_root).first()

        for file in files:
            # skip hidden files
            if file[0] != '.':
                id_file += 1
                models.File.objects.create(id=id_file,
                                           name=file.split('.')[0],
                                           extension=file.split('.')[1],
                                           is_public=set_public_or_private(file),
                                           parent_folder=folder_obj)
