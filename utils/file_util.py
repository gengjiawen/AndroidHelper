import os
import re
import shutil

import time


def get_files_by_extensions(folder, extensions=None, sort_by=None):
    files = list()
    for i in os.listdir(folder):
        f = os.path.abspath(os.path.join(folder, i))
        if os.path.isfile(f):
            if extensions:
                if f.endswith(extensions):
                    files.append(f)
            else:
                files.append(f)
    if sort_by:
        files = sorted(files, key=sort_by)
    return files

