"""
This file is a local settings file that's specifically used
to store setting(s) about the data directory.

It's kept separate from the general local_settings.py file
so that it can be more easily managed by Salt.
"""

# The path of the root data folder
DATA_ROOT = "/path/to/local/data/folder"
# The name of the dir inside data root where the data files are stored
DATA_ROOT_FILES = "files"
