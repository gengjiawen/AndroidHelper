import os
import shutil
import tempfile
import zipfile

from utils.file_util import get_files_by_re, gen_new_file_extension


def get_aar_files(proj_dir, des_dir):
    rel_aar_dir = r"build\outputs\aar"
    aar_dirs = [os.path.join(proj_dir, i) for i in os.listdir(proj_dir) if os.path.isdir(os.path.join(proj_dir, i))]
    aar_dirs = [os.path.join(i, rel_aar_dir) for i in aar_dirs if os.path.exists(os.path.join(i, rel_aar_dir))]
    for i in aar_dirs:
        file = os.listdir(i)[0]
        debug_aar = os.path.join(i, file)
        print(debug_aar)
        os.makedirs(des_dir, exist_ok=True)
        shutil.copyfile(debug_aar, os.path.join(des_dir, file))


def using_local_aar(aar_dir):
    # http://stackoverflow.com/a/24894387/1713757
    # or you can just do it in android studio ui
    s = 'configurations.maybeCreate("default")'
    for i in os.listdir(aar_dir):
        if i.endswith("aar"):
            print("aar:", i)
            t = "artifacts.add(\"default\", file('{}'))\n".format(i)
            s += t
    print(s)
    build_script = os.path.join(aar_dir, "build.gradle")
    open(build_script, mode='w', encoding='utf-8').write(s)
    aar_module_name = os.path.basename(aar_dir)
    print("add this to setting.gradle: ")
    print("include ':{}'".format(aar_module_name))
    print("\nadd this to mudule using aars: ")
    print("compile project(':{}')".format(aar_module_name))


def extract_aar2jar(aar_dir):
    aar_files = get_files_by_re(aar_dir, ".*aar")
    for i in aar_files:
        jar_name = gen_new_file_extension(i, "jar")
        with zipfile.ZipFile(i, "r") as z:
            temp_dir = tempfile.mkdtemp()
            z.extract("classes.jar", temp_dir)
            if os.path.exists(jar_name):
                os.remove(jar_name)
            shutil.move(os.path.join(temp_dir, "classes.jar"), jar_name)

