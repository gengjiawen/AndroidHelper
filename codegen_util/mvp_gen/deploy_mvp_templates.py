import os
import platform

import shutil

from utils import file_util


template_dir = r"your_location"
if platform.system() == "Darwin":
    template_dir = r"/Applications/Android Studio.app/Contents/plugins/android/lib/templates/other/MVP Pattern"

if os.path.exists(template_dir):
    shutil.rmtree(template_dir)
file_util.copy_folder(r"MVPFromAndroidBoilerplate", template_dir)
