import os
import re


def unify_build(project_dir):
    module_list = [os.path.join(project_dir, i) for i in next(os.walk(project_dir))[1] if
                   not i.startswith((".", "build", "gradle", "capture"))]
    compileSdkVersion = r"androidCompileSdkVersion"
    buildVersion = r"androidBuildToolsVersion"
    minSdkVersion = r"androidMinSdkVersion"
    targetSdkVersion = r"androidTargetSdkVersion"
    for i in module_list:
        gradle_file = os.path.join(i, "build.gradle")
        if os.path.exists(gradle_file):
            s = open(gradle_file, mode='r', encoding='utf-8').read()
            s = re.sub(r"buildToolsVersion ('|\")(.*)('|\")", r"buildToolsVersion {}".format(buildVersion), s)
            s = re.sub(r"compileSdkVersion \d+", r"compileSdkVersion {}".format(compileSdkVersion), s)
            s = re.sub(r"minSdkVersion \d+", r"minSdkVersion {}".format(minSdkVersion), s)
            s = re.sub(r"targetSdkVersion \d+", r"targetSdkVersion {}".format(targetSdkVersion), s)
            s = open(gradle_file, mode='w', encoding='utf-8').write(s)
        else:
            print("{} not exist".format(gradle_file))



