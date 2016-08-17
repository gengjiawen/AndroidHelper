import os
import re


def format_setting_file(project_dir):
    f = os.path.join(project_dir, "settings.gradle")
    s = open(f, mode='r', encoding="utf-8").read()
    s = s.replace("include", "").strip()
    print(s)
    modules = re.split("\s*,\s*", s)
    module_list = list()
    print(modules.__len__())
    for i in sorted(modules):
        m = "include {}".format(i)
        module_list.append(m)
    open(f, mode='w', encoding='utf-8').write("\n".join(module_list))

