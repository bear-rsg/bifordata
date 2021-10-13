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

    # root_path = "/Users/michaelallaway/Desktop/bifordatasample"

    for root, dirs, files in os.walk(settings.DATA_ROOT):
        path = root.split(os.sep)
        print((len(path) - 1) * '--', os.path.basename(root))
        for file in files:
            if file[0] != '.':
                print(len(path) * '--', file)
    
    models.Folder.objects.create(id=1, name='synctestdir')
    models.File.objects.create(id=1, name='synctestfile', parent_folder = models.Folder.objects.get(pk=1))
