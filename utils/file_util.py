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


def get_folders_by_re(folder, match_pattern=None):
    all_folders = list()
    for root, dirs, files in os.walk(folder):
        for i in dirs:
            f = os.path.abspath(os.path.join(root, i))
            all_folders.append(f)

    if match_pattern:
        all_folders = [i for i in all_folders if re.match(match_pattern, i)]

    return all_folders


def get_files_by_re(folder, match_pattern=None, time_range=None):
    """
    get list of files by re and time range
    :param folder:
    :param match_pattern:
    :param time_range: recent created or updated
    :return: files in absolute path meet with the requirement
    """
    def in_time_range(i):
        m = os.path.getmtime(i)
        return True if time.time() - m < time_range else False

    all_files = list()
    for root, dirs, files in os.walk(folder):
        for i in files:
            f = os.path.abspath(os.path.join(root, i))
            all_files.append(f)
    if match_pattern:
        all_files = [i for i in all_files if re.match(match_pattern, os.path.basename(i))]
    if time_range:
        all_files = [i for i in all_files if in_time_range(i)]

    return all_files


def get_immdiate_dir(folder):
    file_list = [os.path.abspath(os.path.join(folder, i)) for i in next(os.walk(folder))[1]]
    return file_list


def get_file_name_without_extension(file):
    file_name = os.path.basename(os.path.splitext(file)[0])
    return file_name


def gen_new_file_extension(file, new_extension):
    """
    generate new file extension for a input file
    :param file:
    :param new_extension:
    :return:
    """
    base_file, ext = os.path.splitext(file)
    return base_file + "." + new_extension


def copy_folder(src, dst, symlinks=False, ignore=None):
    os.makedirs(dst, exist_ok=True)
    try:
        from os import scandir
        for entry in os.scandir(src):
            d = os.path.join(dst, entry.name)
            if entry.is_dir():
                shutil.copytree(entry.path, d, symlinks, ignore)
            else:
                shutil.copy2(entry.path, d)
    except ImportError:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)


def move_folder(src, dst, symlinks=False, ignore=None):
    """
    move folder
    :param src:
    :param dst:
    :param symlinks:
    :param ignore:
    """
    copy_folder(src, dst, symlinks=symlinks, ignore=ignore)
    shutil.rmtree(src)

